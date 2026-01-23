"""
bootstrap.py
Generador de repositorio (monorepo) para:
- Backend: Node.js + Express + PostgreSQL + JWT
- Frontend: React + Vite + PWA (vite-plugin-pwa) + IndexedDB (idb) + Sync (outbox) + Excel (xlsx) + PDF (jsPDF)

Diseñado para:
- Multi-proyecto
- Multiusuario (inspectores con login)
- Offline-first (datos locales + cola de eventos outbox)
- Sync automático cuando hay internet

NOTAS IMPORTANTES:
- Esto es un MVP: funciona y es extensible, pero NO es el producto final.
- La PWA cachea el "app shell" (para abrir sin internet). Los datos se guardan localmente (IndexedDB) y se sincronizan.
- Para producción: usar HTTPS, configurar CORS, endurecer auth, crear endpoint admin para alta de inspectores, etc.

TÉCNICA:
- Este script crea carpetas y escribe archivos en UTF-8 usando pathlib.
  Path.write_text permite escribir texto y especificar encoding. (En docs se muestra read_text/write_text) [web:114]
"""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent


def write_file(path: str, content: str) -> None:
    """
    Crea directorios padre y escribe el contenido como UTF-8.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    # write_text con encoding explícito recomendado para evitar problemas de encoding [web:105]
    p.write_text(content, encoding="utf-8")


def main() -> None:
    files: dict[str, str] = {}

    # ---------------------------
    # ROOT
    # ---------------------------
    files[".gitignore"] = dedent(
        """\
        node_modules
        dist
        .env
        *.log
        .DS_Store
        .vscode
        """
    )

    files["README.md"] = dedent(
        """\
        # WPQ PWA (offline-first) + Sync (MVP)

        App web tipo PWA instalable en móvil/PC, con datos offline (IndexedDB) y sincronización automática al detectar conexión.

        ## Requisitos
        - Node 18+
        - PostgreSQL
        - Git

        ## Backend
        1) Copia `backend/.env.example` a `backend/.env` y edita valores.
        2) Crea DB en Postgres (ej. `wpq`) y aplica schema:
           - `cd backend`
           - `psql "$DATABASE_URL" -f schema.sql`
        3) Ejecuta:
           - `cd backend`
           - `npm i`
           - `npm run dev`

        ## Frontend
        1) (Opcional) define `VITE_API_URL` en `frontend/.env` (si tu API no está en localhost:4000).
        2) Ejecuta:
           - `cd frontend`
           - `npm i`
           - `npm run dev`

        ## Flujo offline/sync
        - Capturas sin internet: se guarda local y se encola evento en `outbox`.
        - Al volver internet: `startAutoSync()` empuja eventos y hace pull de cambios del servidor.
        """
    )

    # ---------------------------
    # BACKEND
    # ---------------------------
    files["backend/.env.example"] = dedent(
        """\
        PORT=4000
        DATABASE_URL=postgres://usuario:password@localhost:5432/wpq
        JWT_SECRET=CAMBIA_ESTA_LLAVE
        """
    )

    files["backend/package.json"] = dedent(
        """\
        {
          "name": "wpq-backend",
          "type": "module",
          "scripts": {
            "dev": "node src/server.js"
          },
          "dependencies": {
            "bcrypt": "^5.1.1",
            "cors": "^2.8.5",
            "dotenv": "^16.4.5",
            "express": "^4.19.2",
            "jsonwebtoken": "^9.0.2",
            "pg": "^8.13.0",
            "zod": "^3.23.8"
          }
        }
        """
    )

    files["backend/schema.sql"] = dedent(
        """\
        create table if not exists users (
          id serial primary key,
          username text unique not null,
          password_hash text not null,
          role text not null default 'INSPECTOR', -- ADMIN | INSPECTOR
          active boolean not null default true,
          created_at timestamptz not null default now()
        );

        create table if not exists projects (
          id serial primary key,
          code text unique not null,
          name text not null,
          created_at timestamptz not null default now(),
          updated_at timestamptz not null default now()
        );

        create table if not exists wps (
          id serial primary key,
          project_id int references projects(id) on delete cascade,
          codigo text not null,
          proceso text,
          material text,
          posicion text,
          espesor_rango text,
          diametro_rango text,
          aporte text,
          gas text,
          observaciones text,
          updated_at timestamptz not null default now(),
          unique(project_id, codigo)
        );

        create table if not exists welders (
          id serial primary key,
          project_id int references projects(id) on delete cascade,
          matricula text not null,
          nombre text not null,
          activo boolean not null default true,
          updated_at timestamptz not null default now(),
          unique(project_id, matricula)
        );

        create table if not exists qualifications (
          id serial primary key,
          project_id int references projects(id) on delete cascade,
          fecha date not null,
          welder_matricula text not null,
          welder_nombre text not null,
          wps_codigo text not null,
          material_capturado text,
          posicion_capturada text,
          raiz_resultado text not null,  -- OK | R | N/A
          vista_resultado text not null, -- OK | R | N/A
          observaciones text,
          status text not null,          -- APROBADO | REPROBADO | PENDIENTE
          created_by text not null,
          updated_at timestamptz not null default now()
        );

        create table if not exists certificates (
          id serial primary key,
          project_id int references projects(id) on delete cascade,
          qualification_id int references qualifications(id) on delete cascade,
          folio text unique not null,
          issued_at timestamptz not null default now(),
          issued_by text not null,
          pdf_base64 text not null
        );

        -- DEMO: proyecto y admin
        insert into projects(code, name)
        values ('OBRA-001', 'Proyecto demo')
        on conflict do nothing;

        -- admin / admin123 (hash de ejemplo; cambia en producción)
        insert into users (username, password_hash, role)
        values (
          'admin',
          '$2b$12$3x3m0W/0tH0Xo8oY4x0xPOfWqKx8hFQq6m5v2zjYtKf7GQe0K9pCe',
          'ADMIN'
        )
        on conflict do nothing;
        """
    )

    files["backend/src/db.js"] = dedent(
        """\
        import pg from "pg";
        import dotenv from "dotenv";
        dotenv.config();

        export const pool = new pg.Pool({
          connectionString: process.env.DATABASE_URL
        });

        export async function q(text, params) {
          return pool.query(text, params);
        }
        """
    )

    files["backend/src/auth.js"] = dedent(
        """\
        import jwt from "jsonwebtoken";
        import bcrypt from "bcrypt";
        import { q } from "./db.js";

        export async function login(username, password) {
          const r = await q("select * from users where username=$1 and active=true", [username]);
          if (r.rowCount === 0) return null;

          const u = r.rows[0];
          const ok = await bcrypt.compare(password, u.password_hash);
          if (!ok) return null;

          const token = jwt.sign(
            { sub: u.id, username: u.username, role: u.role },
            process.env.JWT_SECRET,
            { expiresIn: "12h" }
          );

          return { token, user: { username: u.username, role: u.role } };
        }

        export function requireAuth(req, res, next) {
          const h = req.headers.authorization || "";
          const token = h.startsWith("Bearer ") ? h.slice(7) : null;
          if (!token) return res.status(401).json({ error: "No token" });

          try {
            req.user = jwt.verify(token, process.env.JWT_SECRET);
            next();
          } catch {
            return res.status(401).json({ error: "Invalid token" });
          }
        }

        export function requireRole(role) {
          return (req, res, next) => {
            if (req.user?.role !== role) return res.status(403).json({ error: "Forbidden" });
            next();
          };
        }
        """
    )

    files["backend/src/server.js"] = dedent(
        """\
        import express from "express";
        import cors from "cors";
        import dotenv from "dotenv";
        import { z } from "zod";
        import { q } from "./db.js";
        import { login, requireAuth, requireRole } from "./auth.js";

        dotenv.config();
        const app = express();

        app.use(cors());
        app.use(express.json({ limit: "10mb" }));

        app.get("/health", (_, res) => res.json({ ok: true }));

        app.post("/auth/login", async (req, res) => {
          const body = z.object({ username: z.string(), password: z.string() }).safeParse(req.body);
          if (!body.success) return res.status(400).json({ error: "Bad body" });

          const result = await login(body.data.username, body.data.password);
          if (!result) return res.status(401).json({ error: "Invalid credentials" });
          res.json(result);
        });

        // Proyectos
        app.get("/api/projects", requireAuth, async (req, res) => {
          const r = await q("select * from projects order by id desc", []);
          res.json(r.rows);
        });

        app.post("/api/projects", requireAuth, requireRole("ADMIN"), async (req, res) => {
          const body = z.object({ code: z.string(), name: z.string() }).safeParse(req.body);
          if (!body.success) return res.status(400).json({ error: "Bad body" });

          const r = await q("insert into projects(code,name) values ($1,$2) returning *", [body.data.code, body.data.name]);
          res.json(r.rows[0]);
        });

        /**
         * SYNC: push (outbox)
         * events[]: { entity, op, projectCode, payload }
         */
        app.post("/api/sync/push", requireAuth, async (req, res) => {
          const Event = z.object({
            entity: z.enum(["wps","welder","qualification","certificate"]),
            op: z.enum(["upsert","delete"]),
            projectCode: z.string(),
            payload: z.any()
          });

          const body = z.object({ events: z.array(Event) }).safeParse(req.body);
          if (!body.success) return res.status(400).json({ error: "Bad body" });

          let applied = 0;

          for (const ev of body.data.events) {
            const pr = await q("select id from projects where code=$1", [ev.projectCode]);
            if (pr.rowCount === 0) continue;
            const projectId = pr.rows[0].id;

            // WPS upsert
            if (ev.entity === "wps" && ev.op === "upsert") {
              const p = ev.payload;
              await q(
                `insert into wps(project_id,codigo,proceso,material,posicion,espesor_rango,diametro_rango,aporte,gas,observaciones,updated_at)
                 values ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,now())
                 on conflict(project_id,codigo) do update set
                   proceso=excluded.proceso,
                   material=excluded.material,
                   posicion=excluded.posicion,
                   espesor_rango=excluded.espesor_rango,
                   diametro_rango=excluded.diametro_rango,
                   aporte=excluded.aporte,
                   gas=excluded.gas,
                   observaciones=excluded.observaciones,
                   updated_at=now()`,
                [projectId, p.codigo, p.proceso, p.material, p.posicion, p.espesor_rango, p.diametro_rango, p.aporte, p.gas, p.observaciones]
              );
              applied++;
            }

            // Welder upsert
            if (ev.entity === "welder" && ev.op === "upsert") {
              const p = ev.payload;
              await q(
                `insert into welders(project_id,matricula,nombre,activo,updated_at)
                 values ($1,$2,$3,$4,now())
                 on conflict(project_id,matricula) do update set
                   nombre=excluded.nombre,
                   activo=excluded.activo,
                   updated_at=now()`,
                [projectId, p.matricula, p.nombre, p.activo ?? true]
              );
              applied++;
            }

            // Qualification insert (MVP)
            if (ev.entity === "qualification" && ev.op === "upsert") {
              const p = ev.payload;
              await q(
                `insert into qualifications(
                   project_id, fecha, welder_matricula, welder_nombre, wps_codigo,
                   material_capturado, posicion_capturada, raiz_resultado, vista_resultado,
                   observaciones, status, created_by, updated_at
                 ) values ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,now())`,
                [
                  projectId, p.fecha, p.welder_matricula, p.welder_nombre, p.wps_codigo,
                  p.material_capturado, p.posicion_capturada, p.raiz_resultado, p.vista_resultado,
                  p.observaciones, p.status, req.user.username
                ]
              );
              applied++;
            }

            // Certificate insert (MVP)
            if (ev.entity === "certificate" && ev.op === "upsert") {
              const p = ev.payload; // { qualification_id, folio, pdf_base64 }
              await q(
                `insert into certificates(project_id, qualification_id, folio, issued_by, pdf_base64)
                 values ($1,$2,$3,$4,$5)
                 on conflict(folio) do nothing`,
                [projectId, p.qualification_id || 0, p.folio, req.user.username, p.pdf_base64]
              );
              applied++;
            }
          }

          res.json({ ok: true, applied });
        });

        /**
         * SYNC: pull updates since timestamp
         */
        app.get("/api/sync/pull", requireAuth, async (req, res) => {
          const projectCode = String(req.query.projectCode || "");
          const since = String(req.query.since || "1970-01-01T00:00:00Z");

          const pr = await q("select id from projects where code=$1", [projectCode]);
          if (pr.rowCount === 0) {
            return res.json({ wps: [], welders: [], qualifications: [], certificates: [], serverTime: new Date().toISOString() });
          }

          const projectId = pr.rows[0].id;

          const wps = (await q("select * from wps where project_id=$1 and updated_at>$2", [projectId, since])).rows;
          const welders = (await q("select * from welders where project_id=$1 and updated_at>$2", [projectId, since])).rows;
          const qualifications = (await q("select * from qualifications where project_id=$1 and updated_at>$2", [projectId, since])).rows;
          const certificates = (await q("select * from certificates where project_id=$1 and issued_at>$2", [projectId, since])).rows;

          res.json({ wps, welders, qualifications, certificates, serverTime: new Date().toISOString() });
        });

        app.listen(process.env.PORT || 4000, () => {
          console.log(`API on :${process.env.PORT || 4000}`);
        });
        """
    )

    # ---------------------------
    # FRONTEND
    # ---------------------------
    files["frontend/index.html"] = dedent(
        """\
        <!doctype html>
        <html>
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>WPQ PWA</title>
          </head>
          <body>
            <div id="root"></div>
            <script type="module" src="/src/main.jsx"></script>
          </body>
        </html>
        """
    )

    files["frontend/package.json"] = dedent(
        """\
        {
          "name": "wpq-frontend",
          "private": true,
          "type": "module",
          "scripts": {
            "dev": "vite --host",
            "build": "vite build",
            "preview": "vite preview --host"
          },
          "dependencies": {
            "idb": "^8.0.0",
            "jspdf": "^2.5.1",
            "react": "^18.3.1",
            "react-dom": "^18.3.1",
            "react-router-dom": "^6.28.0",
            "xlsx": "^0.18.5"
          },
          "devDependencies": {
            "@vitejs/plugin-react": "^4.3.4",
            "vite": "^5.4.10",
            "vite-plugin-pwa": "^0.20.5"
          }
        }
        """
    )

    files["frontend/vite.config.js"] = dedent(
        """\
        import { defineConfig } from "vite";
        import react from "@vitejs/plugin-react";
        import { VitePWA } from "vite-plugin-pwa";

        export default defineConfig({
          plugins: [
            react(),
            VitePWA({
              registerType: "autoUpdate",
              manifest: {
                name: "WPQ Calificación Soldadores",
                short_name: "WPQ",
                start_url: "/",
                display: "standalone",
                background_color: "#0b1220",
                theme_color: "#0b1220",
                icons: [
                  { src: "/pwa-192.png", sizes: "192x192", type: "image/png" },
                  { src: "/pwa-512.png", sizes: "512x512", type: "image/png" }
                ]
              },
              workbox: { navigateFallback: "/index.html" }
            })
          ]
        });
        """
    )

    files["frontend/src/authStore.js"] = dedent(
        """\
        export function setAuth(auth) {
          localStorage.setItem("auth", JSON.stringify(auth));
        }
        export function getAuth() {
          const s = localStorage.getItem("auth");
          return s ? JSON.parse(s) : null;
        }
        export function clearAuth() {
          localStorage.removeItem("auth");
        }
        """
    )

    files["frontend/src/api.js"] = dedent(
        """\
        import { getAuth } from "./authStore";

        const API = import.meta.env.VITE_API_URL || "http://localhost:4000";

        export async function api(path, { method="GET", body } = {}) {
          const auth = getAuth();
          const headers = { "Content-Type": "application/json" };
          if (auth?.token) headers.Authorization = `Bearer ${auth.token}`;

          const res = await fetch(`${API}${path}`, {
            method,
            headers,
            body: body ? JSON.stringify(body) : undefined
          });

          if (!res.ok) throw new Error(await res.text());
          return res.json();
        }
        """
    )

    files["frontend/src/db.js"] = dedent(
        """\
        import { openDB } from "idb";

        export const dbPromise = openDB("wpq-db", 1, {
          upgrade(db) {
            db.createObjectStore("projects", { keyPath: "code" });
            db.createObjectStore("wps", { keyPath: "key" });          // key = `${projectCode}:${codigo}`
            db.createObjectStore("welders", { keyPath: "key" });      // key = `${projectCode}:${matricula}`
            db.createObjectStore("qualifications", { keyPath: "localId" });
            db.createObjectStore("certificates", { keyPath: "folio" });
            db.createObjectStore("outbox", { keyPath: "id" });
            db.createObjectStore("sync_state", { keyPath: "projectCode" });
          }
        });
        """
    )

    files["frontend/src/sync.js"] = dedent(
        """\
        import { api } from "./api";
        import { dbPromise } from "./db";

        function uid() {
          return crypto.randomUUID();
        }

        export async function enqueue(event) {
          const db = await dbPromise;
          await db.put("outbox", { id: uid(), createdAt: Date.now(), ...event });
        }

        // Regla flexible: OK en lo evaluado
        // - Si cualquier R -> REPROBADO
        // - Si hay al menos un OK y el otro es OK o N/A -> APROBADO
        // - Si ambos N/A -> PENDIENTE
        export function computeStatus(raiz, vista) {
          if (raiz === "R" || vista === "R") return "REPROBADO";
          if (raiz === "OK" && (vista === "OK" || vista === "N/A")) return "APROBADO";
          if (vista === "OK" && (raiz === "OK" || raiz === "N/A")) return "APROBADO";
          return "PENDIENTE";
        }

        export async function pull(projectCode) {
          const db = await dbPromise;
          const state = await db.get("sync_state", projectCode);
          const since = state?.lastPulledAt || "1970-01-01T00:00:00Z";

          const data = await api(`/api/sync/pull?projectCode=${encodeURIComponent(projectCode)}&since=${encodeURIComponent(since)}`);

          for (const w of data.wps) {
            await db.put("wps", { key: `${projectCode}:${w.codigo}`, projectCode, ...w });
          }
          for (const w of data.welders) {
            await db.put("welders", { key: `${projectCode}:${w.matricula}`, projectCode, ...w });
          }
          for (const q of data.qualifications || []) {
            await db.put("qualifications", { localId: `srv:${q.id}`, projectCode, ...q });
          }
          for (const c of data.certificates || []) {
            await db.put("certificates", { projectCode, ...c });
          }

          await db.put("sync_state", { projectCode, lastPulledAt: data.serverTime || new Date().toISOString() });
        }

        export async function flush(projectCode) {
          const db = await dbPromise;
          const all = await db.getAll("outbox");
          const pending = all.filter(e => e.projectCode === projectCode);

          if (pending.length === 0) return { pushed: 0 };

          await api("/api/sync/push", {
            method: "POST",
            body: {
              events: pending.map(p => ({
                entity: p.entity,
                op: p.op,
                projectCode: p.projectCode,
                payload: p.payload
              }))
            }
          });

          for (const p of pending) await db.delete("outbox", p.id);
          return { pushed: pending.length };
        }

        export function startAutoSync(projectCode, onStatus) {
          const tick = async () => {
            try {
              if (!navigator.onLine) return;
              onStatus?.("Sincronizando...");
              await flush(projectCode);
              await pull(projectCode);
              onStatus?.("Sincronizado");
            } catch {
              onStatus?.("Error sync (reintentará)");
            }
          };

          window.addEventListener("online", tick);
          const t = setInterval(tick, 15000);
          tick();

          return () => {
            window.removeEventListener("online", tick);
            clearInterval(t);
          };
        }
        """
    )

    files["frontend/src/excel.js"] = dedent(
        """\
        import * as XLSX from "xlsx";
        import { dbPromise } from "./db";
        import { enqueue } from "./sync";

        export function parseXlsx(file) {
          return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onerror = reject;
            reader.onload = () => {
              const data = new Uint8Array(reader.result);
              const wb = XLSX.read(data, { type: "array" });
              resolve(wb);
            };
            reader.readAsArrayBuffer(file);
          });
        }

        export function sheetToJson(wb, sheetName) {
          const ws = wb.Sheets[sheetName || wb.SheetNames[0]];
          return XLSX.utils.sheet_to_json(ws, { defval: "" });
        }

        export async function importWpsFromRows(projectCode, rows) {
          const db = await dbPromise;
          for (const r of rows) {
            const codigo = String(r.CodigoWPS || r.codigo || "").trim();
            if (!codigo) continue;

            const item = {
              key: `${projectCode}:${codigo}`,
              projectCode,
              codigo,
              proceso: String(r.Proceso || "").trim(),
              material: String(r.Material || "").trim(),
              posicion: String(r.Posicion || "").trim(),
              espesor_rango: String(r.EspesorRango || "").trim(),
              diametro_rango: String(r.DiametroRango || "").trim(),
              aporte: String(r.Aporte || "").trim(),
              gas: String(r.Gas || "").trim(),
              observaciones: String(r.Observaciones || "").trim()
            };

            await db.put("wps", item);
            await enqueue({ entity: "wps", op: "upsert", projectCode, payload: item });
          }
        }

        export async function importWeldersFromRows(projectCode, rows) {
          const db = await dbPromise;
          for (const r of rows) {
            const matricula = String(r.Matricula || "").trim();
            const nombre = String(r.Nombre || "").trim();
            if (!matricula || !nombre) continue;

            const item = {
              key: `${projectCode}:${matricula}`,
              projectCode,
              matricula,
              nombre,
              activo: String(r.Activo || "SI").toUpperCase() !== "NO"
            };

            await db.put("welders", item);
            await enqueue({ entity: "welder", op: "upsert", projectCode, payload: item });
          }
        }

        export function downloadXlsx(filename, sheets) {
          const wb = XLSX.utils.book_new();
          for (const [name, rows] of Object.entries(sheets)) {
            const ws = XLSX.utils.json_to_sheet(rows);
            XLSX.utils.book_append_sheet(wb, ws, name);
          }
          XLSX.writeFile(wb, filename);
        }
        """
    )

    files["frontend/src/pdf.js"] = dedent(
        """\
        import { jsPDF } from "jspdf";

        export async function makeCertificatePdfBytes({ folio, projectCode, q, inspector }) {
          const doc = new jsPDF();
          doc.setFontSize(14);
          doc.text("CERTIFICADO DE CALIFICACIÓN", 14, 18);

          doc.setFontSize(11);
          doc.text(`Folio: ${folio}`, 14, 28);
          doc.text(`Proyecto: ${projectCode}`, 14, 35);

          doc.text(`Soldador: ${q.welder_nombre}`, 14, 48);
          doc.text(`Matrícula: ${q.welder_matricula}`, 14, 55);

          doc.text(`WPS: ${q.wps_codigo}`, 14, 68);
          doc.text(`Material: ${q.material_capturado || ""}`, 14, 75);
          doc.text(`Posición: ${q.posicion_capturada || ""}`, 14, 82);

          doc.text(`RAÍZ: ${q.raiz_resultado}   VISTA: ${q.vista_resultado}`, 14, 95);
          doc.text(`Estatus: ${q.status}`, 14, 102);

          doc.text(`Inspector: ${inspector}`, 14, 116);

          const arrayBuf = doc.output("arraybuffer");
          return new Uint8Array(arrayBuf);
        }

        export function bytesToBase64(bytes) {
          let binary = "";
          bytes.forEach(b => (binary += String.fromCharCode(b)));
          return btoa(binary);
        }

        export function downloadPdf(bytes, filename) {
          const blob = new Blob([bytes], { type: "application/pdf" });
          const url = URL.createObjectURL(blob);
          const a = document.createElement("a");
          a.href = url;
          a.download = filename;
          a.click();
          URL.revokeObjectURL(url);
        }
        """
    )

    files["frontend/src/main.jsx"] = dedent(
        """\
        import React from "react";
        import ReactDOM from "react-dom/client";
        import { BrowserRouter } from "react-router-dom";
        import App from "./App.jsx";

        ReactDOM.createRoot(document.getElementById("root")).render(
          <BrowserRouter>
            <App />
          </BrowserRouter>
        );
        """
    )

    files["frontend/src/App.jsx"] = dedent(
        """\
        import React from "react";
        import { Routes, Route, Link, Navigate } from "react-router-dom";
        import Login from "./pages/Login.jsx";
        import Projects from "./pages/Projects.jsx";
        import Wps from "./pages/Wps.jsx";
        import Welders from "./pages/Welders.jsx";
        import Qualifications from "./pages/Qualifications.jsx";
        import Certificates from "./pages/Certificates.jsx";
        import { getAuth, clearAuth } from "./authStore.js";

        function Guard({ children }) {
          return getAuth()?.token ? children : <Navigate to="/login" replace />;
        }

        export default function App() {
          const auth = getAuth();

          return (
            <div style={{ padding: 12, fontFamily: "system-ui, Arial" }}>
              <div style={{ display: "flex", gap: 12, flexWrap: "wrap", alignItems: "center" }}>
                <strong>WPQ PWA</strong>
                {auth?.token && (
                  <>
                    <Link to="/projects">Proyectos</Link>
                    <Link to="/wps">WPS</Link>
                    <Link to="/welders">Soldadores</Link>
                    <Link to="/qualifications">Calificaciones</Link>
                    <Link to="/certificates">Certificados</Link>
                    <button onClick={() => { clearAuth(); location.href="/login"; }}>Salir</button>
                  </>
                )}
              </div>
              <hr />
              <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/projects" element={<Guard><Projects /></Guard>} />
                <Route path="/wps" element={<Guard><Wps /></Guard>} />
                <Route path="/welders" element={<Guard><Welders /></Guard>} />
                <Route path="/qualifications" element={<Guard><Qualifications /></Guard>} />
                <Route path="/certificates" element={<Guard><Certificates /></Guard>} />
                <Route path="*" element={<Navigate to={auth?.token ? "/projects" : "/login"} replace />} />
              </Routes>
            </div>
          );
        }
        """
    )

    files["frontend/src/pages/Login.jsx"] = dedent(
        """\
        import React, { useState } from "react";
        import { api } from "../api";
        import { setAuth } from "../authStore";

        export default function Login() {
          const [username, setUsername] = useState("admin");
          const [password, setPassword] = useState("admin123");
          const [err, setErr] = useState("");

          const onLogin = async () => {
            setErr("");
            try {
              const r = await api("/auth/login", { method: "POST", body: { username, password } });
              setAuth(r);
              location.href = "/projects";
            } catch (e) {
              setErr("No se pudo iniciar sesión.");
            }
          };

          return (
            <div style={{ maxWidth: 360 }}>
              <h3>Login</h3>
              <label>Usuario</label>
              <input value={username} onChange={e=>setUsername(e.target.value)} style={{ width:"100%" }} />
              <label>Contraseña</label>
              <input type="password" value={password} onChange={e=>setPassword(e.target.value)} style={{ width:"100%" }} />
              <button onClick={onLogin} style={{ marginTop: 12 }}>Entrar</button>
              {err && <div style={{ color:"crimson", marginTop: 8 }}>{err}</div>}
            </div>
          );
        }
        """
    )

    files["frontend/src/pages/Projects.jsx"] = dedent(
        """\
        import React, { useEffect, useState } from "react";
        import { api } from "../api";
        import { startAutoSync } from "../sync";

        export default function Projects() {
          const [projects, setProjects] = useState([]);
          const [selected, setSelected] = useState(localStorage.getItem("projectCode") || "");
          const [syncStatus, setSyncStatus] = useState("—");

          useEffect(() => {
            api("/api/projects").then(setProjects).catch(()=>{});
          }, []);

          useEffect(() => {
            if (!selected) return;
            localStorage.setItem("projectCode", selected);
            const stop = startAutoSync(selected, setSyncStatus);
            return stop;
          }, [selected]);

          return (
            <div>
              <h3>Proyectos</h3>
              <div>Estado sync: <strong>{syncStatus}</strong></div>
              <label>Proyecto activo</label>
              <select value={selected} onChange={e=>setSelected(e.target.value)}>
                <option value="">-- Selecciona --</option>
                {projects.map(p => <option key={p.id} value={p.code}>{p.code} - {p.name}</option>)}
              </select>
            </div>
          );
        }
        """
    )

    files["frontend/src/pages/Wps.jsx"] = dedent(
        """\
        import React, { useEffect, useState } from "react";
        import { dbPromise } from "../db";
        import { enqueue } from "../sync";
        import { parseXlsx, sheetToJson, importWpsFromRows, downloadXlsx } from "../excel";

        export default function Wps() {
          const projectCode = localStorage.getItem("projectCode") || "";
          const [items, setItems] = useState([]);

          async function refresh() {
            const db = await dbPromise;
            const all = await db.getAll("wps");
            setItems(all.filter(x => x.projectCode === projectCode));
          }

          useEffect(() => { refresh(); }, [projectCode]);

          const save = async (it) => {
            const db = await dbPromise;
            await db.put("wps", it);
            await enqueue({ entity: "wps", op: "upsert", projectCode, payload: it });
            refresh();
          };

          const onImport = async (file) => {
            const wb = await parseXlsx(file);
            const rows = sheetToJson(wb, "WPS");
            await importWpsFromRows(projectCode, rows);
            refresh();
          };

          const onExport = async () => {
            downloadXlsx("WPS.xlsx", {
              WPS: items.map(i => ({
                CodigoWPS: i.codigo,
                Proceso: i.proceso,
                Material: i.material,
                Posicion: i.posicion,
                EspesorRango: i.espesor_rango,
                DiametroRango: i.diametro_rango,
                Aporte: i.aporte,
                Gas: i.gas,
                Observaciones: i.observaciones
              }))
            });
          };

          if (!projectCode) return <div>Selecciona proyecto en “Proyectos”.</div>;

          return (
            <div>
              <h3>Catálogo WPS</h3>
              <input type="file" accept=".xlsx" onChange={e=>e.target.files?.[0] && onImport(e.target.files[0])} />
              <button onClick={onExport} style={{ marginLeft: 8 }}>Exportar Excel</button>

              <h4>Nuevo / Editar</h4>
              <WpsForm projectCode={projectCode} onSave={save} />

              <h4>Lista</h4>
              <table border="1" cellPadding="6">
                <thead><tr><th>Código</th><th>Proceso</th><th>Material</th><th>Posición</th></tr></thead>
                <tbody>
                  {items.map(i=>(
                    <tr key={i.key}>
                      <td>{i.codigo}</td><td>{i.proceso}</td><td>{i.material}</td><td>{i.posicion}</td>
                    </tr>
                  ))}
                </tbody>
              </table>

              <p style={{ opacity: 0.75 }}>
                Formato import WPS (hoja “WPS”): CodigoWPS, Proceso, Material, Posicion, EspesorRango, DiametroRango, Aporte, Gas, Observaciones.
              </p>
            </div>
          );
        }

        function WpsForm({ projectCode, onSave }) {
          const [codigo, setCodigo] = useState("");
          const [proceso, setProceso] = useState("");
          const [material, setMaterial] = useState("");
          const [posicion, setPosicion] = useState("");

          return (
            <div style={{ display:"grid", gap: 6, maxWidth: 520 }}>
              <input placeholder="Código WPS" value={codigo} onChange={e=>setCodigo(e.target.value)} />
              <input placeholder="Proceso" value={proceso} onChange={e=>setProceso(e.target.value)} />
              <input placeholder="Material" value={material} onChange={e=>setMaterial(e.target.value)} />
              <input placeholder="Posición" value={posicion} onChange={e=>setPosicion(e.target.value)} />
              <button onClick={()=>{
                const c = codigo.trim();
                if (!c) return;
                onSave({ key: `${projectCode}:${c}`, projectCode, codigo: c, proceso, material, posicion });
                setCodigo(""); setProceso(""); setMaterial(""); setPosicion("");
              }}>Guardar</button>
            </div>
          );
        }
        """
    )

    files["frontend/src/pages/Welders.jsx"] = dedent(
        """\
        import React, { useEffect, useState } from "react";
        import { dbPromise } from "../db";
        import { enqueue } from "../sync";
        import { parseXlsx, sheetToJson, importWeldersFromRows, downloadXlsx } from "../excel";

        export default function Welders() {
          const projectCode = localStorage.getItem("projectCode") || "";
          const [items, setItems] = useState([]);

          async function refresh() {
            const db = await dbPromise;
            const all = await db.getAll("welders");
            setItems(all.filter(x => x.projectCode === projectCode));
          }
          useEffect(() => { refresh(); }, [projectCode]);

          const save = async (it) => {
            const db = await dbPromise;
            await db.put("welders", it);
            await enqueue({ entity: "welder", op: "upsert", projectCode, payload: it });
            refresh();
          };

          const onImport = async (file) => {
            const wb = await parseXlsx(file);
            const rows = sheetToJson(wb, "Soldadores");
            await importWeldersFromRows(projectCode, rows);
            refresh();
          };

          const onExport = async () => {
            downloadXlsx("Soldadores.xlsx", {
              Soldadores: items.map(i => ({
                Matricula: i.matricula,
                Nombre: i.nombre,
                Activo: i.activo ? "SI" : "NO"
              }))
            });
          };

          if (!projectCode) return <div>Selecciona proyecto en “Proyectos”.</div>;

          return (
            <div>
              <h3>Catálogo Soldadores</h3>
              <input type="file" accept=".xlsx" onChange={e=>e.target.files?.[0] && onImport(e.target.files[0])} />
              <button onClick={onExport} style={{ marginLeft: 8 }}>Exportar Excel</button>

              <h4>Nuevo / Editar</h4>
              <WelderForm projectCode={projectCode} onSave={save} />

              <h4>Lista</h4>
              <table border="1" cellPadding="6">
                <thead><tr><th>Matrícula</th><th>Nombre</th><th>Activo</th></tr></thead>
                <tbody>
                  {items.map(i=>(
                    <tr key={i.key}>
                      <td>{i.matricula}</td><td>{i.nombre}</td><td>{i.activo ? "SI" : "NO"}</td>
                    </tr>
                  ))}
                </tbody>
              </table>

              <p style={{ opacity: 0.75 }}>
                Formato import Soldadores (hoja “Soldadores”): Matricula, Nombre, Activo (SI/NO).
              </p>
            </div>
          );
        }

        function WelderForm({ projectCode, onSave }) {
          const [matricula, setMatricula] = useState("");
          const [nombre, setNombre] = useState("");
          const [activo, setActivo] = useState(true);

          return (
            <div style={{ display:"grid", gap: 6, maxWidth: 520 }}>
              <input placeholder="Matrícula" value={matricula} onChange={e=>setMatricula(e.target.value)} />
              <input placeholder="Nombre" value={nombre} onChange={e=>setNombre(e.target.value)} />
              <label style={{ display:"flex", gap: 8, alignItems:"center" }}>
                <input type="checkbox" checked={activo} onChange={e=>setActivo(e.target.checked)} />
                Activo
              </label>
              <button onClick={()=>{
                const m = matricula.trim();
                const n = nombre.trim();
                if (!m || !n) return;
                onSave({ key: `${projectCode}:${m}`, projectCode, matricula: m, nombre: n, activo });
                setMatricula(""); setNombre(""); setActivo(true);
              }}>Guardar</button>
            </div>
          );
        }
        """
    )

    files["frontend/src/pages/Qualifications.jsx"] = dedent(
        """\
        import React, { useEffect, useMemo, useState } from "react";
        import { dbPromise } from "../db";
        import { enqueue, computeStatus } from "../sync";

        const OPTIONS = ["OK", "R", "N/A"];

        export default function Qualifications() {
          const projectCode = localStorage.getItem("projectCode") || "";
          const [welders, setWelders] = useState([]);
          const [wps, setWps] = useState([]);
          const [list, setList] = useState([]);

          const [fecha, setFecha] = useState(new Date().toISOString().slice(0,10));
          const [matricula, setMatricula] = useState("");
          const [nombre, setNombre] = useState("");
          const [wpsCodigo, setWpsCodigo] = useState("");
          const [material, setMaterial] = useState("");
          const [posicion, setPosicion] = useState("");
          const [raiz, setRaiz] = useState("OK");
          const [vista, setVista] = useState("OK");
          const [obs, setObs] = useState("");

          useEffect(() => {
            (async ()=>{
              const db = await dbPromise;
              setWelders((await db.getAll("welders")).filter(x=>x.projectCode===projectCode));
              setWps((await db.getAll("wps")).filter(x=>x.projectCode===projectCode));
              setList((await db.getAll("qualifications")).filter(x=>x.projectCode===projectCode).slice(-200).reverse());
            })();
          }, [projectCode]);

          useEffect(() => {
            const w = welders.find(x => x.matricula === matricula);
            if (w) setNombre(w.nombre);
          }, [matricula, welders]);

          useEffect(() => {
            const w = wps.find(x => x.codigo === wpsCodigo);
            if (w) {
              setMaterial(w.material || "");
              setPosicion(w.posicion || "");
            }
          }, [wpsCodigo, wps]);

          const status = useMemo(()=>computeStatus(raiz, vista), [raiz, vista]);

          const save = async () => {
            if (!projectCode) return alert("Selecciona proyecto.");
            if (!matricula || !nombre || !wpsCodigo) return alert("Matrícula, nombre y WPS requeridos.");

            const q = {
              localId: crypto.randomUUID(),
              projectCode,
              fecha,
              welder_matricula: matricula,
              welder_nombre: nombre,
              wps_codigo: wpsCodigo,
              material_capturado: material,
              posicion_capturada: posicion,
              raiz_resultado: raiz,
              vista_resultado: vista,
              observaciones: obs,
              status
            };

            const db = await dbPromise;
            await db.put("qualifications", q);
            await enqueue({ entity: "qualification", op: "upsert", projectCode, payload: q });

            setList([q, ...list]);
            setObs("");
            alert("Guardado local + en cola para sync.");
          };

          if (!projectCode) return <div>Selecciona proyecto en “Proyectos”.</div>;

          return (
            <div>
              <h3>Calificaciones</h3>

              <div style={{ display:"grid", gap: 6, maxWidth: 520 }}>
                <input type="date" value={fecha} onChange={e=>setFecha(e.target.value)} />

                <input list="welders" placeholder="Matrícula (buscador)" value={matricula} onChange={e=>setMatricula(e.target.value)} />
                <datalist id="welders">
                  {welders.map(w => <option key={w.key} value={w.matricula}>{w.nombre}</option>)}
                </datalist>

                <input placeholder="Nombre (autollenado; editable)" value={nombre} onChange={e=>setNombre(e.target.value)} />

                <input list="wpsList" placeholder="WPS (buscador)" value={wpsCodigo} onChange={e=>setWpsCodigo(e.target.value)} />
                <datalist id="wpsList">
                  {wps.map(w => <option key={w.key} value={w.codigo}></option>)}
                </datalist>

                <input placeholder="Material" value={material} onChange={e=>setMaterial(e.target.value)} />
                <input placeholder="Posición" value={posicion} onChange={e=>setPosicion(e.target.value)} />

                <label>RAÍZ</label>
                <select value={raiz} onChange={e=>setRaiz(e.target.value)}>{OPTIONS.map(o=><option key={o} value={o}>{o}</option>)}</select>

                <label>VISTA</label>
                <select value={vista} onChange={e=>setVista(e.target.value)}>{OPTIONS.map(o=><option key={o} value={o}>{o}</option>)}</select>

                <input placeholder="Observaciones" value={obs} onChange={e=>setObs(e.target.value)} />

                <div>Estatus: <strong>{status}</strong></div>
                <button onClick={save}>Guardar</button>
              </div>

              <h4>Últimos registros</h4>
              <table border="1" cellPadding="6">
                <thead><tr><th>Fecha</th><th>Matrícula</th><th>Nombre</th><th>WPS</th><th>Raíz</th><th>Vista</th><th>Status</th></tr></thead>
                <tbody>
                  {list.map(q=>(
                    <tr key={q.localId}>
                      <td>{q.fecha}</td><td>{q.welder_matricula}</td><td>{q.welder_nombre}</td><td>{q.wps_codigo}</td>
                      <td>{q.raiz_resultado}</td><td>{q.vista_resultado}</td><td>{q.status}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          );
        }
        """
    )

    files["frontend/src/pages/Certificates.jsx"] = dedent(
        """\
        import React, { useEffect, useState } from "react";
        import { dbPromise } from "../db";
        import { enqueue } from "../sync";
        import { makeCertificatePdfBytes, bytesToBase64, downloadPdf } from "../pdf";
        import { getAuth } from "../authStore";

        export default function Certificates() {
          const projectCode = localStorage.getItem("projectCode") || "";
          const auth = getAuth();
          const [quals, setQuals] = useState([]);

          useEffect(() => {
            (async ()=>{
              const db = await dbPromise;
              const all = await db.getAll("qualifications");
              setQuals(all.filter(x=>x.projectCode===projectCode && x.status==="APROBADO"));
            })();
          }, [projectCode]);

          const issue = async (q) => {
            const folio = `CERT-${projectCode}-${Date.now()}`;
            const bytes = await makeCertificatePdfBytes({
              folio,
              projectCode,
              q,
              inspector: auth?.user?.username || "inspector"
            });

            downloadPdf(bytes, `${folio}.pdf`);

            // MVP: qualification_id no está ligado a server id aún; en producción se debe mapear.
            const payload = {
              qualification_id: 0,
              folio,
              pdf_base64: bytesToBase64(bytes)
            };

            const db = await dbPromise;
            await db.put("certificates", { ...payload, projectCode });

            await enqueue({ entity: "certificate", op: "upsert", projectCode, payload });
            alert("Certificado generado y encolado para sincronizar.");
          };

          if (!projectCode) return <div>Selecciona proyecto en “Proyectos”.</div>;

          return (
            <div>
              <h3>Certificados (APROBADO)</h3>
              <ul>
                {quals.map(q => (
                  <li key={q.localId}>
                    {q.fecha} - {q.welder_matricula} - {q.welder_nombre} - WPS {q.wps_codigo}
                    <button onClick={()=>issue(q)} style={{ marginLeft: 8 }}>Generar PDF</button>
                  </li>
                ))}
              </ul>
            </div>
          );
        }
        """
    )

    # ---------------------------
    # Write everything
    # ---------------------------
    for path, content in files.items():
        write_file(path, content)

    print("OK: repositorio generado.")
    print("Siguiente:")
    print("1) backend: copia .env.example -> .env, configura DATABASE_URL, aplica schema.sql y corre npm i / npm run dev")
    print("2) frontend: npm i / npm run dev")


if __name__ == "__main__":
    main()
