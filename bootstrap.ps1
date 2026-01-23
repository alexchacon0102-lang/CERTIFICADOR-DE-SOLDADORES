# bootstrap.ps1
# Genera un monorepo: /backend (Node/Express + PostgreSQL) y /frontend (React/Vite PWA + IndexedDB + sync).
# Requisitos locales: Git, Node 18+, npm, PostgreSQL y PowerShell.
# Uso:
#   1) Crea carpeta vacía y copia este archivo dentro
#   2) Ejecuta: powershell -ExecutionPolicy Bypass -File .\bootstrap.ps1
#   3) Luego: git init; git add .; git commit -m "init"; git remote add origin ...; git push -u origin main

$ErrorActionPreference = "Stop"

function WriteFile($path, $content) {
  $dir = Split-Path $path -Parent
  if ($dir -and !(Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
  Set-Content -Path $path -Value $content -Encoding UTF8 -NoNewline
}

# -----------------------
# Root files
# -----------------------
WriteFile ".gitignore" @'
node_modules
dist
.env
*.log
.DS_Store
.vscode
wpq_app.db
'@

WriteFile "README.md" @'
# WPQ PWA (offline-first) + Sync (MVP)

## Requisitos
- Node 18+
- PostgreSQL
- Git

## Backend
1) Copia `backend/.env.example` a `backend/.env` y edita valores.
2) Crea DB y aplica schema:
   - En Windows: usa pgAdmin o `psql`:
     `cd backend`
     `psql "%DATABASE_URL%" -f schema.sql`
3) Ejecuta:
   `cd backend`
   `npm i`
   `npm run dev`

## Frontend
1) Ejecuta:
   `cd frontend`
   `npm i`
   `npm run dev`

## Notas MVP
- PWA cachea el "app shell"; datos se guardan en IndexedDB y se sincronizan con outbox cuando hay conexión.
- Estado APROBADO flexible: OK en lo evaluado (si hay al menos un OK y ningún R).
'@

# -----------------------
# Backend
# -----------------------
WriteFile "backend/.env.example" @'
PORT=4000
DATABASE_URL=postgres://usuario:password@localhost:5432/wpq
JWT_SECRET=CAMBIA_ESTA_LLAVE
'@

WriteFile "backend/package.json" @'
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
'@

WriteFile "backend/schema.sql" @'
create table if not exists users (
  id serial primary key,
  username text unique not null,
  password_hash text not null,
  role text not null default 'INSPECTOR',
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

-- Admin demo: usuario admin / password admin123
-- NOTA: el hash es de ejemplo. Para producción cambia y vuelve a hashear.
insert into users (username, password_hash, role)
values (
  'admin',
  '$2b$12$3x3m0W/0tH0Xo8oY4x0xPOfWqKx8hFQq6m5v2zjYtKf7GQe0K9pCe',
  'ADMIN'
)
on conflict do nothing;

insert into projects(code, name)
values ('OBRA-001', 'Proyecto demo')
on conflict do nothing;
'@

WriteFile "backend/src/db.js" @'
import pg from "pg";
import dotenv from "dotenv";
dotenv.config();

export const pool = new pg.Pool({
  connectionString: process.env.DATABASE_URL
});

export async function q(text, params) {
  return pool.query(text, params);
}
'@

WriteFile "backend/src/auth.js" @'
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
'@

WriteFile "backend/src/server.js" @'
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

app.get("/api/projects", requireAuth, async (req, res) => {
  const r = await q("select * from projects order by id desc", []);
  res.json(r.rows);
});

app.post("/api/projects", requireAuth, requireRole("ADMIN"), async (req, res) => {
  const body = z.object({ code: z.string(), name: z.string() }).safeParse(req.body);
  if (!body.success) return res.status(400).json({ error: "Bad body" });
  const r = await q(
    "insert into projects(code,name) values ($1,$2) returning *",
    [body.data.code, body.data.name]
  );
  res.json(r.rows[0]);
});

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

    if (ev.entity === "certificate" && ev.op === "upsert") {
      const p = ev.payload;
      await q(
        `insert into certificates(project_id, qualification_id, folio, issued_by, pdf_base64)
         values ($1,$2,$3,$4,$5)
         on conflict(folio) do nothing`,
        [projectId, p.qualification_id, p.folio, req.user.username, p.pdf_base64]
      );
      applied++;
    }
  }

  res.json({ ok: true, applied });
});

app.get("/api/sync/pull", requireAuth, async (req, res) => {
  const projectCode = String(req.query.projectCode || "");
  const since = String(req.query.since || "1970-01-01T00:00:00Z");

  const pr = await q("select id from projects where code=$1", [projectCode]);
  if (pr.rowCount === 0) return res.json({ wps: [], welders: [], qualifications: [], certificates: [], serverTime: new Date().toISOString() });
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
'@

# -----------------------
# Frontend
# -----------------------
WriteFile "frontend/index.html" @'
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
'@

WriteFile "frontend/package.json" @'
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
'@

WriteFile "frontend/vite.config.js" @'
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
'@

WriteFile "frontend/src/authStore.js" @'
export function setAuth(auth) { localStorage.setItem("auth", JSON.stringify(auth)); }
export function getAuth() { const s = localStorage.getItem("auth"); return s ? JSON.parse(s) : null; }
export function clearAuth() { localStorage.removeItem("auth"); }
'@

WriteFile "frontend/src/api.js" @'
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
'@

WriteFile "frontend/src/db.js" @'
import { openDB } from "idb";

export const dbPromise = openDB("wpq-db", 1, {
  upgrade(db) {
    db.createObjectStore("wps", { keyPath: "key" });
    db.createObjectStore("welders", { keyPath: "key" });
    db.createObjectStore("qualifications", { keyPath: "localId" });
    db.createObjectStore("certificates", { keyPath: "folio" });
    db.createObjectStore("outbox", { keyPath: "id" });
    db.createObjectStore("sync_state", { keyPath: "projectCode" });
  }
});
'@

WriteFile "frontend/src/sync.js" @'
import { api } from "./api";
import { dbPromise } from "./db";

function uid() { return crypto.randomUUID(); }

export async function enqueue(event) {
  const db = await dbPromise;
  await db.put("outbox", { id: uid(), createdAt: Date.now(), ...event });
}

export function computeStatus(raiz, vista) {
  // Flexible: OK en lo evaluado
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

  for (const w of data.wps) await db.put("wps", { key: `${projectCode}:${w.codigo}`, projectCode, ...w });
  for (const w of data.welders) await db.put("welders", { key: `${projectCode}:${w.matricula}`, projectCode, ...w });

  await db.put("sync_state", { projectCode, lastPulledAt: data.serverTime || new Date().toISOString() });
}

export async function flush(projectCode) {
  const db = await dbPromise;
  const all = await db.getAll("outbox");
  const pending = all.filter(e => e.projectCode === projectCode);
  if (pending.length === 0) return { pushed: 0 };

  await api("/api/sync/push", { method: "POST", body: { events: pending.map(p => ({
    entity: p.entity, op: p.op, projectCode: p.projectCode, payload: p.payload
  })) }});

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
'@

WriteFile "frontend/src/pdf.js" @'
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
'@

WriteFile "frontend/src/main.jsx" @'
import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
'@

WriteFile "frontend/src/App.jsx" @'
import React, { useEffect, useState } from "react";
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
      <div style={{ display:"flex", gap:12, flexWrap:"wrap", alignItems:"center" }}>
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
'@

WriteFile "frontend/src/pages/Login.jsx" @'
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
    } catch {
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
'@

WriteFile "frontend/src/pages/Projects.jsx" @'
import React, { useEffect, useState } from "react";
import { api } from "../api";
import { startAutoSync } from "../sync";

export default function Projects() {
  const [projects, setProjects] = useState([]);
  const [selected, setSelected] = useState(localStorage.getItem("projectCode") || "");
  const [syncStatus, setSyncStatus] = useState("—");

  useEffect(() => { api("/api/projects").then(setProjects).catch(()=>{}); }, []);
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
      <div style={{ marginTop: 10, opacity: 0.85 }}>
        Consejo: abre la app en tu móvil con la URL del VPS (HTTPS) y agrega a pantalla de inicio.
      </div>
    </div>
  );
}
'@

WriteFile "frontend/src/pages/Wps.jsx" @'
import React, { useEffect, useState } from "react";
import { dbPromise } from "../db";
import { enqueue } from "../sync";

export default function Wps() {
  const projectCode = localStorage.getItem("projectCode") || "";
  const [items, setItems] = useState([]);
  const [codigo, setCodigo] = useState("");

  const refresh = async () => {
    const db = await dbPromise;
    const all = await db.getAll("wps");
    setItems(all.filter(x=>x.projectCode===projectCode));
  };

  useEffect(() => { refresh(); }, [projectCode]);

  const save = async () => {
    const c = codigo.trim();
    if (!c) return;
    const db = await dbPromise;
    const it = { key: `${projectCode}:${c}`, projectCode, codigo: c };
    await db.put("wps", it);
    await enqueue({ entity:"wps", op:"upsert", projectCode, payload: it });
    setCodigo("");
    refresh();
  };

  if (!projectCode) return <div>Selecciona proyecto en “Proyectos”.</div>;

  return (
    <div>
      <h3>WPS (MVP)</h3>
      <input placeholder="Código WPS" value={codigo} onChange={e=>setCodigo(e.target.value)} />
      <button onClick={save}>Guardar</button>

      <h4>Lista</h4>
      <ul>
        {items.map(i => <li key={i.key}>{i.codigo}</li>)}
      </ul>
    </div>
  );
}
'@

WriteFile "frontend/src/pages/Welders.jsx" @'
import React, { useEffect, useState } from "react";
import { dbPromise } from "../db";
import { enqueue } from "../sync";

export default function Welders() {
  const projectCode = localStorage.getItem("projectCode") || "";
  const [items, setItems] = useState([]);
  const [matricula, setMatricula] = useState("");
  const [nombre, setNombre] = useState("");

  const refresh = async () => {
    const db = await dbPromise;
    const all = await db.getAll("welders");
    setItems(all.filter(x=>x.projectCode===projectCode));
  };

  useEffect(() => { refresh(); }, [projectCode]);

  const save = async () => {
    const m = matricula.trim();
    const n = nombre.trim();
    if (!m || !n) return;
    const db = await dbPromise;
    const it = { key: `${projectCode}:${m}`, projectCode, matricula: m, nombre: n, activo: true };
    await db.put("welders", it);
    await enqueue({ entity:"welder", op:"upsert", projectCode, payload: it });
    setMatricula(""); setNombre("");
    refresh();
  };

  if (!projectCode) return <div>Selecciona proyecto en “Proyectos”.</div>;

  return (
    <div>
      <h3>Soldadores (MVP)</h3>
      <input placeholder="Matrícula" value={matricula} onChange={e=>setMatricula(e.target.value)} />
      <input placeholder="Nombre" value={nombre} onChange={e=>setNombre(e.target.value)} />
      <button onClick={save}>Guardar</button>

      <h4>Lista</h4>
      <ul>
        {items.map(i => <li key={i.key}>{i.matricula} - {i.nombre}</li>)}
      </ul>
    </div>
  );
}
'@

WriteFile "frontend/src/pages/Qualifications.jsx" @'
import React, { useEffect, useMemo, useState } from "react";
import { dbPromise } from "../db";
import { enqueue, computeStatus } from "../sync";

const OPTIONS = ["OK", "R", "N/A"];

export default function Qualifications() {
  const projectCode = localStorage.getItem("projectCode") || "";
  const [welders, setWelders] = useState([]);
  const [wps, setWps] = useState([]);

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
    })();
  }, [projectCode]);

  useEffect(() => {
    const w = welders.find(x => x.matricula === matricula);
    if (w) setNombre(w.nombre);
  }, [matricula, welders]);

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
    await enqueue({ entity:"qualification", op:"upsert", projectCode, payload: q });

    setObs("");
    alert("Guardado (local) y encolado para sync.");
  };

  if (!projectCode) return <div>Selecciona proyecto en “Proyectos”.</div>;

  return (
    <div>
      <h3>Calificaciones (MVP)</h3>

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
    </div>
  );
}
'@

WriteFile "frontend/src/pages/Certificates.jsx" @'
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

    const payload = {
      qualification_id: 0,
      folio,
      pdf_base64: bytesToBase64(bytes)
    };

    const db = await dbPromise;
    await db.put("certificates", { ...payload, projectCode });

    await enqueue({ entity:"certificate", op:"upsert", projectCode, payload });
    alert("Certificado generado y encolado para sync.");
  };

  if (!projectCode) return <div>Selecciona proyecto en “Proyectos”.</div>;

  return (
    <div>
      <h3>Certificados (solo APROBADO)</h3>
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
'@

Write-Host "Listo. Se generaron /backend y /frontend. Ahora instala dependencias y ejecuta."
