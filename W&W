<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <title>W&W - Welding and Welders | Hutchison Ports TNG</title>
  <style>
    :root {
      --bg: #f0f4f8;
      --surface: #ffffff;
      --surface-2: #f8fafc;
      --text: #1B365D;
      --muted: #64748b;
      --line: #cbd5e1;
      --primary: #1B365D;
      --primary-2: #0d2445;
      --accent: #00A9E0;
      --accent-soft: #e0f4fc;
      --accent-dark: #0085b3;
      --ok: #059669;
      --bad: #dc2626;
      --warn: #d97706;
      --shadow: 0 10px 30px rgba(27, 54, 93, 0.08);
      --shadow-lg: 0 20px 40px rgba(27, 54, 93, 0.12);
    }
    * { box-sizing: border-box; }
    body { margin: 0; font-family: 'Inter', 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, #f0f4f8 0%, #e8eef5 50%, #f5f8fb 100%); color: var(--text); }
    .app { display: grid; grid-template-columns: 260px 1fr; min-height: 100vh; }
    .app.home-mode { grid-template-columns: 1fr; }
    .sidebar { background: linear-gradient(180deg, #1B365D 0%, #0d2445 100%); color: #fff; padding: 24px 18px; display: flex; flex-direction: column; }
    .app.home-mode .sidebar { display: none; }
    .brand { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 28px; font-weight: 800; margin-bottom: 4px; }
    .brand-sub { color: #00A9E0; font-size: 13px; font-weight: 600; margin-bottom: 24px; letter-spacing: 1px; }
    .nav-btn { width: 100%; display: block; border: 0; border-radius: 12px; background: rgba(255,255,255,.06); color: #fff; padding: 14px 16px; text-align: left; font-size: 14px; font-weight: 600; margin-bottom: 8px; cursor: pointer; transition: all .2s; }
    .nav-btn.active, .nav-btn:hover { background: linear-gradient(90deg, #00A9E0 0%, #0085b3 100%); box-shadow: 0 4px 15px rgba(0, 169, 224, 0.3); }
    .nav-btn.disabled-nav { opacity: 0.35; pointer-events: none; }
    .main { padding: 24px; overflow-y: auto; max-height: 100vh; }
    .page { display: none; animation: fadeIn 0.3s ease; }
    .page.active { display: block; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
    .topbar { margin-bottom: 20px; }
    .title { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 28px; font-weight: 800; color: var(--primary); }
    .subtitle { color: var(--muted); font-size: 14px; }
    .card { background: #fff; border: 1px solid var(--line); border-radius: 16px; box-shadow: var(--shadow); padding: 20px; margin-bottom: 20px; }
    .card h3 { margin: 0 0 14px; color: var(--primary); font-size: 16px; font-weight: 700; }

    /* ===== HOME PAGE ===== */
    .home-hero { min-height: calc(100vh - 48px); display: flex; flex-direction: column; justify-content: center; max-width: 1200px; margin: 0 auto; }
    .home-header { text-align: center; margin-bottom: 40px; }
    .home-logo { max-width: 280px; margin-bottom: 20px; filter: drop-shadow(0 4px 12px rgba(27,54,93,0.15)); }
    .home-title { font-family: 'Plus Jakarta Sans', sans-serif; font-size: clamp(32px, 5vw, 56px); font-weight: 800; margin: 0; color: var(--primary); text-transform: uppercase; }
    .home-subtitle { margin-top: 10px; font-size: clamp(14px, 2vw, 22px); font-weight: 700; color: var(--accent); letter-spacing: 4px; }
    .hero-menu { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; max-width: 1000px; margin: 0 auto; }
    .menu-tile { position: relative; border: 2px solid #e2e8f0; background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); border-radius: 24px; padding: 36px 28px; cursor: pointer; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.08); transition: all .3s cubic-bezier(0.4, 0, 0.2, 1); text-align: center; overflow: hidden; }
    .menu-tile::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #00A9E0 0%, #1B365D 100%); transform: scaleX(0); transform-origin: left; transition: transform .3s ease; }
    .menu-tile:hover::before { transform: scaleX(1); }
    .menu-tile:hover { transform: translateY(-8px); border-color: var(--accent); box-shadow: 0 12px 28px rgba(0, 169, 224, 0.25), 0 0 0 1px rgba(0, 169, 224, 0.1); background: linear-gradient(135deg, #ffffff 0%, #e0f4fc 100%); }
    .menu-tile svg { filter: drop-shadow(0 2px 4px rgba(27, 54, 93, 0.15)); transition: transform .3s ease; }
    .menu-tile:hover svg { transform: scale(1.1); }
    .menu-tile h3 { font-family: 'Plus Jakarta Sans', sans-serif; margin: 0 0 12px; font-size: 20px; font-weight: 800; color: var(--primary); }
    .menu-tile p { margin: 0; color: var(--muted); font-size: 13px; line-height: 1.5; }
    .menu-tile.disabled-tile { opacity: 0.35; pointer-events: none; filter: grayscale(0.6); }

    /* ===== FORM ELEMENTS ===== */
    input, select, textarea { width: 100%; padding: 10px 12px; border-radius: 8px; border: 1px solid var(--line); background: #fff; font-size: 13px; font-family: inherit; transition: border-color .2s; }
    input:focus, select:focus, textarea:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px rgba(0,169,224,0.12); }
    input[readonly], input[disabled] { background: #f8fafc; color: var(--muted); cursor: default; }
    label.field-label { display: block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: var(--muted); margin-bottom: 4px; }
    .form-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
    .form-grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }
    .form-grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
    .form-grid-5 { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; }
    .btn-row { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 14px; }
    .btn { border: 0; border-radius: 8px; padding: 10px 16px; cursor: pointer; font-weight: 700; font-size: 13px; font-family: inherit; transition: all .2s; }
    .btn-sm { padding: 5px 10px; font-size: 11px; border-radius: 6px; }
    .btn-primary { background: linear-gradient(90deg, #00A9E0 0%, #0085b3 100%); color: #fff; }
    .btn-primary:hover { box-shadow: 0 4px 15px rgba(0,169,224,0.4); transform: translateY(-1px); }
    .btn-secondary { background: #f1f5f9; color: var(--primary); border: 1px solid var(--line); }
    .btn-secondary:hover { background: #e2e8f0; }
    .btn-danger { background: #fee2e2; color: #dc2626; border: 1px solid #fecaca; }
    .btn-danger:hover { background: #fecaca; }
    .btn-success { background: linear-gradient(90deg, #059669 0%, #047857 100%); color: #fff; }
    .btn-warn { background: #fef3c7; color: #92400e; border: 1px solid #fcd34d; }
    .btn-warn:hover { background: #fde68a; }

    /* ===== TABLES ===== */
    .table-shell { border: 1px solid var(--line); border-radius: 12px; overflow: hidden; background: #fff; }
    .table-shell table { width: 100%; border-collapse: collapse; font-size: 13px; }
    .table-shell th, .table-shell td { border: 1px solid var(--line); padding: 8px 10px; vertical-align: middle; }
    .table-shell th { background: linear-gradient(180deg, #1B365D 0%, #0d2445 100%); color: #fff; font-weight: 700; font-size: 11px; letter-spacing: 0.3px; }
    .table-shell tbody tr:nth-child(even) { background: #f8fafc; }
    .table-shell tbody tr:hover { background: var(--accent-soft); }

    /* ===== PROJECT LAYOUT ===== */
    .project-layout { display: grid; grid-template-columns: 280px 1fr; gap: 18px; }
    .project-list .proj-item { width: 100%; margin-bottom: 8px; text-align: left; border: 1px solid var(--line); background: #fff; border-radius: 10px; padding: 10px 12px; cursor: pointer; font-family: inherit; transition: all .2s; display: flex; align-items: center; gap: 8px; }
    .project-list .proj-item:hover, .project-list .proj-item.active { border-color: var(--accent); background: var(--accent-soft); }
    .proj-item .proj-info { flex: 1; min-width: 0; }
    .proj-item .proj-info strong { display: block; font-size: 13px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .proj-item .proj-delete-btn { width: 30px; height: 30px; border: none; background: #fee2e2; color: #dc2626; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; flex-shrink: 0; transition: all .2s; font-size: 14px; }
    .proj-item .proj-delete-btn:hover { background: #fecaca; transform: scale(1.1); }
    .section-title { margin: 4px 0 10px; font-size: 16px; font-weight: 800; color: var(--primary); font-family: 'Plus Jakarta Sans', sans-serif; }
    .small { color: var(--muted); font-size: 12px; }

    /* ===== SECTION BADGES ===== */
    .section-badge { display: flex; align-items: center; gap: 8px; font-size: 10px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; color: var(--primary); margin: 14px 0 8px; padding: 6px 14px; background: linear-gradient(90deg, var(--accent-soft), #fff); border-radius: 8px; border-left: 4px solid var(--accent); }
    .section-badge::before { content: ''; display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: var(--accent); flex-shrink: 0; }

    /* ===== STATUS BADGES ===== */
    .status-micro { font-size: 9px; font-weight: 800; text-transform: uppercase; padding: 2px 7px; border-radius: 999px; white-space: nowrap; letter-spacing: 0.5px; }
    .status-micro.pending { background: #f1f5f9; color: #94a3b8; border: 1px solid #e2e8f0; }
    .status-micro.ok { background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }
    .status-micro.bad { background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }
    .action-cell { display: flex; gap: 5px; align-items: center; }

    /* ===== MASTER WELDERS ===== */
    .certificados-layout { display: grid; grid-template-columns: 1fr 300px; gap: 20px; }
    .mass-actions-bar { background: linear-gradient(180deg, #1B365D 0%, #0d2445 100%); border-radius: 12px; padding: 12px 16px; margin-bottom: 16px; display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }
    .mass-actions-bar label { color: #fff; font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 8px; }
    .mass-actions-bar select { width: auto; padding: 8px 12px; font-size: 13px; }
    .selection-count { color: var(--accent); font-weight: 700; font-size: 14px; }
    .welder-cards-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; }
    .welder-card { border: 1px solid var(--line); border-radius: 14px; background: #fff; padding: 16px; display: flex; gap: 12px; align-items: center; cursor: pointer; transition: all .2s; }
    .welder-card:hover { border-color: var(--accent); box-shadow: 0 8px 20px rgba(0,169,224,0.12); }
    .welder-card.selected { border-color: var(--accent); background: var(--accent-soft); }
    .welder-avatar { width: 50px; height: 50px; border-radius: 12px; background: linear-gradient(135deg, #1B365D 0%, #00A9E0 100%); color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px; flex-shrink: 0; overflow: hidden; }
    .welder-avatar img { width: 100%; height: 100%; object-fit: cover; }
    .welder-main { flex: 1; min-width: 0; }
    .welder-name { font-size: 14px; font-weight: 800; color: var(--text); margin-bottom: 4px; text-transform: uppercase; }
    .welder-id-line { color: var(--muted); font-size: 12px; margin-bottom: 6px; }
    .welder-meta { display: flex; gap: 6px; flex-wrap: wrap; }
    .status-badge { padding: 3px 10px; border-radius: 999px; font-size: 10px; font-weight: 800; text-transform: uppercase; }
    .status-badge.activo { background: #dcfce7; color: #166534; }
    .status-badge.inactivo { background: #fee2e2; color: #991b1b; }
    .cert-count-badge { padding: 3px 8px; border-radius: 999px; font-size: 10px; font-weight: 700; background: var(--accent-soft); color: var(--accent-dark); }

    /* ===== WPS CARDS ===== */
    .wps-cards-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; }
    .wps-card { border: 1px solid var(--line); border-radius: 16px; background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); padding: 16px; display: flex; gap: 14px; align-items: center; cursor: pointer; transition: all .25s; position: relative; }
    .wps-card:hover { border-color: var(--accent); box-shadow: 0 8px 24px rgba(0,169,224,0.18); transform: translateY(-2px); }
    .wps-process-box { min-width: 74px; max-width: 94px; height: 64px; border-radius: 12px; background: linear-gradient(135deg, #1B365D 0%, #00A9E0 100%); color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 13px; flex-shrink: 0; text-align: center; padding: 6px; line-height: 1.2; letter-spacing: 0.5px; box-shadow: 0 4px 12px rgba(0,169,224,0.25); }
    .wps-card-body { flex: 1; min-width: 0; }
    .wps-card-name { font-size: 13px; font-weight: 800; color: var(--text); margin-bottom: 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .wps-card-societies { display: flex; gap: 4px; flex-wrap: wrap; }
    .soc-badge { padding: 2px 8px; border-radius: 999px; font-size: 9px; font-weight: 800; text-transform: uppercase; color: #fff; letter-spacing: 0.3px; }
    .soc-badge.soc-abs { background: #dc2626; }
    .soc-badge.soc-lr { background: #1e3a5f; }
    .soc-badge.soc-dnv { background: #38bdf8; color: #0c4a6e; }
    .soc-badge.soc-bv { background: #78350f; }
    .soc-badge.soc-cwi { background: #f97316; }
    .soc-badge.soc-rina { background: #1f2937; }
    .soc-badge.soc-other { background: #9ca3af; }
    .wps-card-delete { position: absolute; top: 8px; right: 8px; width: 24px; height: 24px; border: none; background: #fee2e2; color: #dc2626; border-radius: 6px; cursor: pointer; font-size: 12px; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity .2s; }
    .wps-card:hover .wps-card-delete { opacity: 1; }
    .wps-card-delete:hover { background: #fecaca; }

    /* ===== WPS TABS ===== */
    .wps-tabs { display: flex; gap: 0; border-bottom: 2px solid var(--line); margin-bottom: 12px; align-items: stretch; flex-wrap: wrap; }
    .wps-tab-btn { padding: 8px 16px; border: none; background: none; font-weight: 700; font-size: 13px; cursor: pointer; color: var(--muted); border-bottom: 2px solid transparent; margin-bottom: -2px; transition: all .2s; font-family: inherit; display: flex; align-items: center; gap: 6px; }
    .wps-tab-btn.active { color: var(--accent); border-bottom-color: var(--accent); }
    .wps-tab-btn:hover { color: var(--primary); }
    .wps-tab-content { display: none; }
    .wps-tab-content.active { display: block; }
    .wps-tab-name-input { border: none; background: transparent; font-weight: 700; font-size: 13px; color: inherit; font-family: inherit; width: 60px; min-width: 30px; text-align: center; padding: 0; outline: none; }
    .wps-tab-name-input:focus { border-bottom: 1px dashed var(--accent); }
    .wps-tab-delete { width: 16px; height: 16px; border: none; background: rgba(220,38,38,0.1); color: #dc2626; border-radius: 50%; cursor: pointer; font-size: 10px; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity .2s; padding: 0; }
    .wps-tab-btn:hover .wps-tab-delete { opacity: 1; }
    .wps-add-tab-btn { padding: 6px 14px; border: 1px dashed var(--accent); background: transparent; color: var(--accent); border-radius: 8px; cursor: pointer; font-weight: 800; font-size: 16px; margin-left: 8px; margin-bottom: -2px; transition: all .2s; line-height: 1; font-family: inherit; }
    .wps-add-tab-btn:hover { background: var(--accent-soft); }

    /* ===== WPS SOCIETY CHECKBOXES ===== */
    .soc-check-grid { display: flex; flex-wrap: wrap; gap: 12px; padding: 8px 0; }
    .soc-check-item { display: flex; align-items: center; gap: 6px; }
    .soc-check-item input[type="checkbox"] { width: 18px; height: 18px; accent-color: var(--accent); cursor: pointer; }
    .soc-check-item label { font-size: 12px; font-weight: 700; cursor: pointer; padding: 3px 10px; border-radius: 6px; }
    .soc-check-item.soc-abs label { background: #fee2e2; color: #dc2626; }
    .soc-check-item.soc-lr label { background: #dbeafe; color: #1e3a5f; }
    .soc-check-item.soc-dnv label { background: #e0f2fe; color: #0369a1; }
    .soc-check-item.soc-bv label { background: #fef3c7; color: #78350f; }
    .soc-check-item.soc-cwi label { background: #ffedd5; color: #c2410c; }
    .soc-check-item.soc-rina label { background: #f3f4f6; color: #1f2937; }

    /* ===== MODALS ===== */
    .modal { position: fixed; inset: 0; background: rgba(27,54,93,0.65); display: none; align-items: center; justify-content: center; padding: 16px; z-index: 9999; backdrop-filter: blur(6px); }
    .modal.show { display: flex; }
    .modal-card { width: min(960px, 95%); max-height: 92vh; overflow: auto; background: #fff; border-radius: 20px; box-shadow: 0 30px 70px rgba(27,54,93,0.3); }
    .modal-card::-webkit-scrollbar { width: 6px; }
    .modal-card::-webkit-scrollbar-track { background: #f1f5f9; }
    .modal-card::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 3px; }
    .modal-header { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; border-bottom: 2px solid var(--line); background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 100%); border-radius: 20px 20px 0 0; position: sticky; top: 0; z-index: 10; }
    .modal-header .title { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 20px; font-weight: 800; color: var(--primary); }
    .modal-body { padding: 24px; }
    .photo-box { width: 120px; height: 140px; border: 2px dashed var(--accent); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: var(--muted); background: #f8fafc; overflow: hidden; font-size: 12px; text-align: center; }
    .photo-box img { width: 100%; height: 100%; object-fit: cover; }
    .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    .tag-ok { color: var(--ok); font-weight: 800; }
    .tag-bad { color: var(--bad); font-weight: 800; }
    .search-dropdown { position: relative; }
    .search-results { position: absolute; top: 100%; left: 0; right: 0; background: #fff; border: 1px solid var(--line); border-radius: 8px; max-height: 200px; overflow: auto; z-index: 100; box-shadow: var(--shadow); display: none; }
    .search-results.show { display: block; }
    .search-result-item { padding: 10px 12px; cursor: pointer; border-bottom: 1px solid #eee; font-size: 13px; }
    .search-result-item:hover { background: var(--accent-soft); }
    .search-result-item:last-child { border-bottom: 0; }
    .insp-table input[type="radio"] { width: auto; margin: 0 4px; }
    .result-approved { background: #dcfce7 !important; }
    .result-rejected { background: #fee2e2 !important; color: #991b1b; font-weight: 800; }

    /* ===== STOCK SECTION ===== */
    .stock-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; align-items: start; }
    .stock-panel { background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%); }
    .soft-caption { color: var(--muted); font-size: 13px; margin-top: 6px; }
    .stock-search-results { max-height: 220px; overflow: auto; border: 1px solid var(--line); border-radius: 14px; background: #fff; margin-top: 10px; }
    .stock-result-item { padding: 14px 16px; border-bottom: 1px solid #edf1f4; display: flex; justify-content: space-between; gap: 10px; align-items: center; }
    .stock-result-item:last-child { border-bottom: 0; }
    .stock-result-item button { background: var(--accent-soft); color: var(--primary); border: 1px solid var(--accent); border-radius: 10px; padding: 8px 14px; font-weight: 700; cursor: pointer; transition: all .2s; font-size: 13px; }
    .stock-result-item button:hover { background: var(--accent); color: #fff; }
    .stock-result-item strong { color: var(--primary); font-size: 15px; }
    .selected-chip-wrap { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; }
    .selected-chip { display: inline-flex; align-items: center; gap: 8px; padding: 9px 14px; border-radius: 999px; background: var(--accent-soft); border: 1px solid var(--accent); font-size: 13px; color: var(--primary); font-weight: 700; }
    .selected-chip button { border: 0; background: transparent; color: var(--bad); cursor: pointer; font-weight: 800; font-size: 16px; padding: 0; }
    .stock-top-actions { display: flex; justify-content: space-between; gap: 12px; align-items: center; flex-wrap: wrap; margin-bottom: 14px; }
    .check-col { width: 42px; text-align: center; }
    .qty-input { width: 80px; text-align: center; padding: 6px 8px; }

    /* ===== FORM FIELD GROUPS ===== */
    .field-group { margin-bottom: 10px; }
    .field-group > label.field-label { display: block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: var(--muted); margin-bottom: 4px; }
    .process-check-group { display: flex; gap: 20px; padding: 10px 0; }
    .process-check-group label { display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600; cursor: pointer; }
    .process-check-group input[type="checkbox"] { width: 16px; height: 16px; cursor: pointer; accent-color: var(--accent); }

    /* ===== RESULT DISPLAY ===== */
    .result-display { text-align: center; padding: 14px; border-radius: 12px; font-size: 20px; font-weight: 800; border: 3px solid; letter-spacing: 2px; }
    .result-display.approved { background: #dcfce7; color: #166534; border-color: #86efac; }
    .result-display.rejected { background: #fee2e2; color: #991b1b; border-color: #fca5a5; }
    .result-display.pending { background: #f1f5f9; color: #94a3b8; border-color: #e2e8f0; }

    /* ===== CERT TABLE ===== */
    .cert-table-input { min-width: 120px; }

    /* ===== LOGIN OVERLAY ===== */
    .login-overlay { position: fixed; inset: 0; background: linear-gradient(135deg, #1B365D 0%, #0d2445 60%, #0a1e3d 100%); z-index: 100000; display: flex; align-items: center; justify-content: center; flex-direction: column; padding: 20px; }
    .login-overlay.hidden { display: none; }
    .login-box { background: #fff; border-radius: 24px; padding: 40px 36px; max-width: 460px; width: 100%; box-shadow: 0 30px 80px rgba(0,0,0,0.4); text-align: center; }
    .login-box .login-logo { max-width: 180px; margin-bottom: 20px; }
    .login-box h2 { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 24px; font-weight: 800; color: var(--primary); margin: 0 0 8px; }
    .login-box .login-sub { color: var(--muted); font-size: 13px; margin-bottom: 28px; }
    .role-cards { display: grid; gap: 12px; margin-bottom: 20px; }
    .role-card { border: 2px solid var(--line); border-radius: 14px; padding: 16px; cursor: pointer; transition: all .2s; text-align: left; display: flex; align-items: center; gap: 14px; }
    .role-card:hover { border-color: var(--accent); background: var(--accent-soft); }
    .role-card.active-role { border-color: var(--accent); background: var(--accent-soft); }
    .role-icon { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; }
    .role-icon.creator { background: linear-gradient(135deg, #fbbf24, #f59e0b); }
    .role-icon.trust { background: linear-gradient(135deg, #00A9E0, #0085b3); }
    .role-icon.guest { background: linear-gradient(135deg, #94a3b8, #64748b); }
    .role-card h4 { margin: 0; font-size: 15px; font-weight: 700; color: var(--primary); }
    .role-card p { margin: 2px 0 0; font-size: 11px; color: var(--muted); }
    .login-password-area { display: none; margin-top: 16px; }
    .login-password-area.show { display: block; }
    .login-confianza-select { display: none; margin-bottom: 10px; }
    .login-confianza-select.show { display: block; }
    .login-btn { width: 100%; padding: 14px; border: none; border-radius: 12px; font-size: 15px; font-weight: 800; cursor: pointer; transition: all .2s; font-family: inherit; }
    .login-btn-enter { background: linear-gradient(90deg, #00A9E0, #0085b3); color: #fff; }
    .login-btn-enter:hover { box-shadow: 0 6px 20px rgba(0,169,224,0.4); }
    .login-error { color: #dc2626; font-size: 12px; font-weight: 700; margin-top: 8px; display: none; }
    .login-error.show { display: block; }

    /* ===== ADMIN PANEL ===== */
    .admin-section-title { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 15px; font-weight: 800; color: var(--primary); margin: 0 0 16px; display: flex; align-items: center; gap: 10px; }
    .admin-section-title::before { content: ''; width: 4px; height: 20px; background: linear-gradient(180deg, #00A9E0, #1B365D); border-radius: 2px; }
    .admin-user-card { border: 1px solid var(--line); border-radius: 14px; background: linear-gradient(135deg, #fff 0%, #f8fafc 100%); padding: 16px 20px; margin-bottom: 12px; transition: all .2s; }
    .admin-user-card:hover { border-color: var(--accent); box-shadow: 0 4px 16px rgba(0,169,224,0.1); }
    .admin-user-header { display: flex; align-items: center; gap: 14px; margin-bottom: 10px; }
    .admin-user-avatar { width: 44px; height: 44px; border-radius: 12px; background: linear-gradient(135deg, #1B365D, #00A9E0); color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 15px; flex-shrink: 0; }
    .admin-user-header .admin-user-info { flex: 1; }
    .admin-user-header .admin-user-info strong { display: block; font-size: 15px; font-weight: 800; color: var(--primary); text-transform: uppercase; }
    .admin-user-header .admin-user-info small { color: var(--muted); font-size: 11px; }
    .admin-user-actions { display: flex; gap: 6px; flex-shrink: 0; }
    .admin-modules-badges { display: flex; gap: 6px; flex-wrap: wrap; }
    .admin-mod-badge { padding: 4px 10px; border-radius: 8px; font-size: 10px; font-weight: 700; background: var(--accent-soft); color: var(--accent-dark); }
    .admin-pass-row { display: flex; align-items: center; gap: 8px; margin-top: 8px; padding-top: 8px; border-top: 1px solid #f1f5f9; }
    .admin-pass-row input { flex: 1; font-size: 12px; padding: 6px 10px; }
    .eye-toggle { width: 34px; height: 34px; border: 1px solid var(--line); background: #fff; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 16px; color: var(--muted); transition: all .2s; flex-shrink: 0; }
    .eye-toggle:hover { border-color: var(--accent); color: var(--accent); }
    .admin-change-pass-card { background: linear-gradient(135deg, #1B365D 0%, #0d2445 100%); color: #fff; border-radius: 16px; padding: 20px; margin-top: 20px; }
    .admin-change-pass-card h3 { color: #00A9E0; margin: 0 0 14px; font-size: 15px; }
    .admin-change-pass-card input { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; }
    .admin-change-pass-card input::placeholder { color: rgba(255,255,255,0.5); }
    .admin-change-pass-card input:focus { border-color: #00A9E0; }
    .pass-field-wrap { position: relative; }
    .pass-field-wrap input { padding-right: 40px; }
    .pass-field-wrap .eye-toggle { position: absolute; right: 4px; top: 50%; transform: translateY(-50%); border: none; background: transparent; }

    /* ===== PRINT TOAST ===== */
    .save-toast { position: fixed; top: 24px; left: 50%; transform: translateX(-50%); background: #059669; color: #fff; padding: 12px 28px; border-radius: 10px; font-weight: 800; z-index: 99999; box-shadow: 0 8px 24px rgba(5,150,105,0.35); font-size: 14px; animation: toastIn .25s ease; }
    .save-toast.error-toast { background: #dc2626; }
    @keyframes toastIn { from { opacity: 0; transform: translateX(-50%) translateY(-10px); } to { opacity: 1; transform: translateX(-50%) translateY(0); } }

    /* role label */
    .role-indicator { color: #00A9E0; font-size: 10px; margin-top: auto; padding-top: 12px; text-align: center; opacity: 0.85; line-height: 1.4; }
    .role-indicator strong { display: block; font-size: 12px; color: #fff; }
    .logout-btn { width: 100%; margin-top: 8px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #94a3b8; border-radius: 8px; padding: 8px; cursor: pointer; font-size: 11px; font-weight: 600; font-family: inherit; transition: all .2s; }
    .logout-btn:hover { background: rgba(255,255,255,0.15); color: #fff; }

    /* ===== RESPONSIVE ===== */
    .menu-toggle {
      display: none; position: fixed; top: 12px; left: 12px; z-index: 10000;
      width: 46px; height: 46px; border: none; border-radius: 12px; cursor: pointer;
      background: linear-gradient(135deg, #1B365D 0%, #0d2445 100%);
      box-shadow: 0 4px 14px rgba(27,54,93,0.35);
      align-items: center; justify-content: center; flex-direction: column; gap: 5px;
      transition: all .2s;
    }
    .menu-toggle:hover { box-shadow: 0 6px 20px rgba(0,169,224,0.4); }
    .menu-toggle span { display: block; width: 22px; height: 2px; background: #fff; border-radius: 2px; transition: all .3s; }
    .menu-toggle.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
    .menu-toggle.open span:nth-child(2) { opacity: 0; }
    .menu-toggle.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }
    .sidebar-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.45); z-index: 9996; backdrop-filter: blur(2px); }
    .sidebar-overlay.show { display: block; }

    @media (max-width: 1024px) {
      .app { grid-template-columns: 220px 1fr; }
      .form-grid { grid-template-columns: repeat(2, 1fr); }
      .form-grid-5 { grid-template-columns: repeat(3, 1fr); }
      .hero-menu { grid-template-columns: repeat(2, 1fr); gap: 16px; }
      .welder-cards-grid, .wps-cards-grid { grid-template-columns: repeat(auto-fill, minmax(240px,1fr)); }
    }

    @media (max-width: 900px) {
      .app { grid-template-columns: 1fr; }
      .app.home-mode { grid-template-columns: 1fr; }
      .sidebar {
        position: fixed; left: -280px; top: 0; width: 270px;
        height: 100vh; z-index: 9997; overflow-y: auto;
        transition: left .3s cubic-bezier(.4,0,.2,1);
        box-shadow: none;
      }
      .sidebar.open { left: 0; box-shadow: 8px 0 32px rgba(27,54,93,0.25); }
      .app.home-mode .sidebar { display: flex; flex-direction: column; }
      .menu-toggle { display: flex; }
      .main { padding: 70px 16px 100px; }
      .project-layout { grid-template-columns: 1fr; }
      .certificados-layout { grid-template-columns: 1fr; }
      .grid-2 { grid-template-columns: 1fr; }
      .stock-layout { grid-template-columns: 1fr; }
      .form-grid-3 { grid-template-columns: repeat(2, 1fr); }
      .form-grid-5 { grid-template-columns: repeat(2, 1fr); }
      .modal { align-items: flex-end; padding: 0; }
      .modal-card { width: 100% !important; max-height: 94vh; border-radius: 20px 20px 0 0; }
      .modal-body { padding: 16px; }
      .modal-header { padding: 14px 16px; border-radius: 20px 20px 0 0; }
      .bottom-nav {
        display: flex; position: fixed; bottom: 0; left: 0; right: 0; z-index: 9995;
        background: #fff; border-top: 1px solid var(--line);
        box-shadow: 0 -4px 20px rgba(27,54,93,0.1);
      }
      .bottom-nav button {
        flex: 1; border: none; background: none; padding: 10px 4px; cursor: pointer;
        display: flex; flex-direction: column; align-items: center; gap: 3px;
        font-size: 9px; font-weight: 700; color: var(--muted); text-transform: uppercase;
        letter-spacing: 0.3px; transition: all .2s; font-family: inherit;
      }
      .bottom-nav button.active { color: var(--accent); }
      .bottom-nav button svg, .bottom-nav button .bnav-icon { font-size: 20px; line-height: 1; }
      .bottom-nav button.disabled-nav { opacity: 0.3; pointer-events: none; }
    }

    @media (max-width: 600px) {
      .form-grid { grid-template-columns: 1fr; }
      .form-grid-2 { grid-template-columns: 1fr; }
      .form-grid-3 { grid-template-columns: 1fr; }
      .form-grid-5 { grid-template-columns: 1fr 1fr; }
      .hero-menu { grid-template-columns: 1fr 1fr; gap: 10px; }
      .menu-tile { padding: 20px 14px; border-radius: 16px; }
      .menu-tile h3 { font-size: 15px; }
      .menu-tile p { font-size: 12px; }
      .menu-tile svg { width: 36px; height: 36px; }
      .title { font-size: 22px; }
      .home-title { font-size: 26px; }
      .home-logo { max-width: 180px; }
      .card { padding: 14px; }
      .btn { padding: 11px 14px; font-size: 13px; min-height: 44px; }
      .btn-sm { padding: 8px 10px; font-size: 12px; min-height: 36px; }
      .table-shell { overflow-x: auto; }
      .table-shell table { min-width: 480px; }
      .cert-table-input { min-width: 80px; }
      .section-badge { flex-wrap: wrap; font-size: 9px; }
      .wps-cards-grid { grid-template-columns: 1fr; }
      .login-box { padding: 28px 20px; }
    }

    @media (max-width: 380px) {
      .hero-menu { grid-template-columns: 1fr; }
      .form-grid-5 { grid-template-columns: 1fr; }
      .main { padding: 70px 12px 90px; }
    }

    @media (min-width: 901px) {
      .bottom-nav { display: none !important; }
    }
  </style>
</head>
<body>

  <!-- ===== LOGIN OVERLAY ===== -->
  <div class="login-overlay" id="loginOverlay">
    <div class="login-box">
      <img src="https://customer-assets.emergentagent.com/job_954bd461-6438-4194-8adb-960c1ce79792/artifacts/hyg0xidk_Logo%20para%20doctos.png" class="login-logo" alt="TNG">
      <h2>WELDING AND WELDERS</h2>
      <div class="login-sub">Selecciona tu tipo de usuario para continuar</div>
      <div class="role-cards" id="roleCards">
        <div class="role-card" onclick="selectLoginRole('creador')" data-role="creador">
          <div class="role-icon creator">&#9733;</div>
          <div><h4>Creador</h4><p>Control total del sistema y administraci&oacute;n de usuarios</p></div>
        </div>
        <div class="role-card" onclick="selectLoginRole('confianza')" data-role="confianza">
          <div class="role-icon trust">&#9830;</div>
          <div><h4>Confianza</h4><p>Acceso a m&oacute;dulos asignados por el creador</p></div>
        </div>
        <div class="role-card" onclick="selectLoginRole('invitado')" data-role="invitado">
          <div class="role-icon guest">&#9675;</div>
          <div><h4>Invitado</h4><p>Visualizaci&oacute;n y control b&aacute;sico de stock</p></div>
        </div>
      </div>
      <div class="login-confianza-select" id="loginConfianzaSelect">
        <select id="loginConfianzaUser" style="margin-bottom:10px;">
          <option value="">Seleccionar usuario...</option>
        </select>
      </div>
      <div class="login-password-area" id="loginPasswordArea">
        <input type="password" id="loginPassword" placeholder="Contrase&ntilde;a" style="margin-bottom:12px;" onkeydown="if(event.key==='Enter')doLogin()" />
      </div>
      <button class="login-btn login-btn-enter" onclick="doLogin()">Ingresar</button>
      <div class="login-error" id="loginError">Contrase&ntilde;a incorrecta</div>
    </div>
  </div>

  <!-- Hamburger toggle (mobile/tablet) -->
  <button class="menu-toggle" id="menuToggle" onclick="toggleSidebar()" aria-label="Men&uacute;">
    <span></span><span></span><span></span>
  </button>
  <div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

  <!-- Bottom navigation bar (mobile/tablet only) -->
  <nav class="bottom-nav" id="bottomNav">
    <button data-page="inicio" onclick="goToPage('inicio');setBottomNav('inicio')">
      <span class="bnav-icon">&#127968;</span><span>Inicio</span>
    </button>
    <button data-page="stock" onclick="goToPage('stock');setBottomNav('stock')">
      <span class="bnav-icon">&#128230;</span><span>Stock</span>
    </button>
    <button data-page="calificacion" onclick="goToPage('calificacion');setBottomNav('calificacion')">
      <span class="bnav-icon">&#128203;</span><span>Calif.</span>
    </button>
    <button data-page="certificados" onclick="goToPage('certificados');setBottomNav('certificados')">
      <span class="bnav-icon">&#128119;</span><span>Soldadores</span>
    </button>
    <button data-page="wps" onclick="goToPage('wps');setBottomNav('wps')">
      <span class="bnav-icon">&#128196;</span><span>WPS</span>
    </button>
  </nav>

  <div class="app home-mode">
    <aside class="sidebar" id="mainSidebar">
      <div class="brand">W&W</div>
      <div class="brand-sub">HUTCHISON PORTS TNG</div>
      <button class="nav-btn active" data-page="inicio">&#127968; Inicio</button>
      <button class="nav-btn" data-page="stock">&#128230; Stock de soldadura</button>
      <button class="nav-btn" data-page="calificacion">&#128203; Calificaci&oacute;n de soldadores</button>
      <button class="nav-btn" data-page="certificados">&#128119; Soldadores certificados</button>
      <button class="nav-btn" data-page="wps">&#128196; WPS</button>
      <button class="nav-btn" data-page="admin" id="adminNavBtn" style="display:none;">&#9881; Administraci&oacute;n</button>
      <div class="role-indicator" id="roleIndicator">
        <strong id="roleIndicatorName">---</strong>
        <span id="roleIndicatorRole"></span>
      </div>
      <button class="logout-btn" onclick="doLogout()">Cerrar sesi&oacute;n</button>
    </aside>
    <main class="main">

      <!-- INICIO -->
      <section class="page active" id="inicio">
        <div class="home-hero">
          <div class="home-header">
            <img src="https://customer-assets.emergentagent.com/job_954bd461-6438-4194-8adb-960c1ce79792/artifacts/hyg0xidk_Logo%20para%20doctos.png" class="home-logo" alt="Hutchison Ports TNG">
            <h1 class="home-title">WELDING AND WELDERS</h1>
            <div class="home-subtitle">W&W</div>
            <div style="margin-top:16px;color:var(--muted);font-size:14px;">Plataforma de control para soldadura, calificaci&oacute;n y trazabilidad documental</div>
          </div>
          <div class="hero-menu" id="heroMenu">
            <div class="menu-tile" data-module="stock" onclick="goToPage('stock')">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" style="margin-bottom:12px;"><rect x="3" y="3" width="7" height="7" rx="1" fill="#00A9E0"/><rect x="3" y="14" width="7" height="7" rx="1" fill="#1B365D"/><rect x="14" y="3" width="7" height="7" rx="1" fill="#1B365D"/><rect x="14" y="14" width="7" height="7" rx="1" fill="#00A9E0"/></svg>
              <h3>Stock de soldadura</h3>
              <p>Control de aporte y consumibles del taller.</p>
            </div>
            <div class="menu-tile" data-module="calificacion" onclick="goToPage('calificacion')">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" style="margin-bottom:12px;"><path d="M9 11H7v2h2v-2zm4 0h-2v2h2v-2zm4 0h-2v2h2v-2zm2-7h-1V2h-2v2H8V2H6v2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V9h14v11z" fill="url(#grad1)"/><defs><linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#00A9E0"/><stop offset="100%" style="stop-color:#1B365D"/></linearGradient></defs></svg>
              <h3>Calificaci&oacute;n de soldadores</h3>
              <p>Gesti&oacute;n de proyectos con formatos de Inspecci&oacute;n, Doblez y Certificado.</p>
            </div>
            <div class="menu-tile" data-module="certificados" onclick="goToPage('certificados')">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" style="margin-bottom:12px;"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" fill="url(#grad2)"/><defs><linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#1B365D"/><stop offset="100%" style="stop-color:#00A9E0"/></linearGradient></defs></svg>
              <h3>Soldadores certificados</h3>
              <p>Consulta de soldadores activos e inactivos.</p>
            </div>
            <div class="menu-tile" data-module="wps" onclick="goToPage('wps')">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" style="margin-bottom:12px;"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V8l-6-6zM6 20V4h7v5h5v11H6z" fill="#00A9E0"/><path d="M8 12h8v2H8v-2zm0 4h5v2H8v-2z" fill="#1B365D"/></svg>
              <h3>WPS</h3>
              <p>Procedimientos de soldadura certificados.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- STOCK DE SOLDADURA -->
      <section class="page" id="stock">
        <div class="topbar">
          <div class="title">Stock de soldadura</div>
          <div class="subtitle">Control editable de aporte, gas, flux y consumibles con selecci&oacute;n para surtido e impresi&oacute;n.</div>
        </div>
        <div class="card" id="stockAddCard">
          <h3>Agregar nuevo &iacute;tem</h3>
          <div class="form-grid">
            <input id="stockItem" placeholder="&Iacute;tem" />
            <input id="stockDesc" placeholder="Descripci&oacute;n" />
            <select id="stockUnit"><option value="KG">KG</option><option value="CL">CL</option><option value="PZAS">PZAS</option><option value="PAR">PAR</option></select>
            <input id="stockQty" type="number" placeholder="Cantidad" />
          </div>
          <div class="btn-row"><button class="btn btn-primary" onclick="addStockItem()">Agregar l&iacute;nea</button></div>
        </div>
        <div class="stock-layout">
          <div class="card stock-panel">
            <h3>Buscador y selecci&oacute;n para surtido</h3>
            <div class="soft-caption">Localiza materiales por nombre o descripci&oacute;n.</div>
            <input id="stockSearch" placeholder="Buscar por &iacute;tem o descripci&oacute;n" oninput="renderStockSearchResults()" style="margin-top:14px;" />
            <div class="stock-search-results" id="stockSearchResults"></div>
          </div>
          <div class="card stock-panel">
            <h3>Selecci&oacute;n activa para requisici&oacute;n</h3>
            <div class="soft-caption">Mantiene visibles los materiales elegidos para surtido.</div>
            <div class="selected-chip-wrap" id="selectedStockChips"></div>
            <div class="btn-row">
              <button class="btn btn-secondary" onclick="clearSelectedStock()">Limpiar selecci&oacute;n</button>
              <button class="btn btn-primary" onclick="printSelectedStock()">Imprimir seleccionados</button>
            </div>
          </div>
        </div>
        <div class="card">
          <div class="stock-top-actions">
            <div><h3 style="margin-bottom:4px;">Tabla de stock</h3><div class="soft-caption">Vista editable del inventario para control diario del taller.</div></div>
            <div class="btn-row" style="margin-top:0;">
              <button class="btn btn-secondary" onclick="selectAllVisibleStock()">Seleccionar visibles</button>
              <button class="btn btn-secondary" onclick="clearSelectedStock()">Quitar selecci&oacute;n</button>
            </div>
          </div>
          <div class="table-shell"><table><thead><tr><th class="check-col">Sel.</th><th>&Iacute;tem</th><th>Descripci&oacute;n</th><th>Unidad</th><th>Cantidad</th><th>Acciones</th></tr></thead><tbody id="stockTableBody"></tbody></table></div>
        </div>
      </section>

      <!-- CALIFICACI&Oacute;N DE SOLDADORES -->
      <section class="page" id="calificacion">
        <div class="topbar"><div class="title">Calificaci&oacute;n de soldadores</div><div class="subtitle">Gesti&oacute;n por proyecto con formatos de Inspecci&oacute;n, Prueba de Doblez y Certificado.</div></div>
        <div class="project-layout">
          <div>
            <div class="card" id="newProjectCard">
              <h3>Nuevo Proyecto</h3>
              <div style="display:grid;gap:10px;">
                <input id="projectName" placeholder="Nombre del proyecto" />
                <input id="projectClient" placeholder="Cliente / astillero" />
              </div>
              <div class="btn-row"><button class="btn btn-primary" onclick="addProject()">Crear proyecto</button></div>
            </div>
            <div class="card project-list"><h3>Proyectos</h3><div id="projectList"></div></div>
          </div>
          <div>
            <div class="card" id="projectFormCard" style="display:none;">
              <h3 id="activeProjectTitle">Proyecto activo</h3>
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div>
                  <label class="field-label">WPS del proyecto</label>
                  <select id="projectWpsSelect" onchange="updateProjectWps()"></select>
                </div>
                <div>
                  <label class="field-label">Fecha</label>
                  <input id="procDate" type="date" onchange="saveProjectMeta()" />
                </div>
              </div>
              <div class="btn-row" style="margin-top:0;">
                <button class="btn btn-secondary" onclick="saveProjectMeta()">&#128190; Guardar informaci&oacute;n</button>
                <button class="btn btn-primary" onclick="openInspeccionListModal()">&#128424; Imprimir Lista de Inspecci&oacute;n</button>
              </div>
            </div>
            <div class="card" id="addWelderCard" style="display:none;">
              <div class="section-title">Agregar soldador al proyecto</div>
              <div class="form-grid-3">
                <div class="search-dropdown">
                  <input id="welderSearchInput" placeholder="Buscar matr&iacute;cula..." oninput="searchWelders()" onfocus="showWelderResults()" />
                  <div class="search-results" id="welderSearchResults"></div>
                </div>
                <input id="welderNameDisplay" placeholder="Nombre" />
                <input id="welderPos" placeholder="Posiciones (3G/4G)" />
              </div>
              <div class="form-grid-5" style="margin-top:10px;">
                <input id="welderPlateThickness" placeholder="Espesor placa" />
                <input id="welderPipeDiameter" placeholder="&Oslash; tuber&iacute;a" />
                <input id="classInspector" placeholder="Inspector clase" />
                <input id="qcInspector" placeholder="Inspector calidad" />
                <input id="wpqNo" placeholder="WPQ" />
              </div>
              <div class="btn-row"><button class="btn btn-primary" onclick="addProjectWelder()">&#10133; Agregar a lista</button></div>
            </div>
            <div class="card" id="projectTableCard" style="display:none;">
              <div class="section-title">Listado del proyecto</div>
              <div class="table-shell" style="overflow-x:auto;">
                <table>
                  <thead>
                    <tr>
                      <th>Matr&iacute;cula</th><th>Nombre</th><th>WPS</th><th>Posici&oacute;n</th>
                      <th>Inspecci&oacute;n</th><th>Doblez</th><th>Certificado</th><th>Acciones</th>
                    </tr>
                  </thead>
                  <tbody id="projectWeldersTable"></tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SOLDADORES CERTIFICADOS -->
      <section class="page" id="certificados">
        <div class="topbar"><div class="title">Soldadores Certificados</div><div class="subtitle">Gesti&oacute;n de personal calificado y cambio masivo de estatus.</div></div>
        <div class="certificados-layout">
          <div>
            <div class="mass-actions-bar" id="massActionsBar">
              <label><input type="checkbox" id="selectAllWelders" onchange="toggleSelectAllWelders()"> Seleccionar todos</label>
              <span class="selection-count" id="selectionCount">0 seleccionados</span>
              <select id="massStatusChange"><option value="">Cambiar estatus a...</option><option value="activo">Activo</option><option value="inactivo">Inactivo</option></select>
              <button class="btn btn-success" onclick="applyMassStatusChange()">Aplicar</button>
              <button class="btn btn-secondary" onclick="clearSelectedWelders()">Limpiar</button>
            </div>
            <div class="card">
              <div style="display:flex;gap:12px;margin-bottom:16px;">
                <input id="weldersSearch" placeholder="Buscar por nombre o matr&iacute;cula..." oninput="renderMasterWelders()" style="flex:1;" />
                <select id="weldersStatusFilter" onchange="renderMasterWelders()" style="width:140px;"><option value="">Todos</option><option value="activo">Activos</option><option value="inactivo">Inactivos</option></select>
              </div>
              <div id="masterWeldersCards" class="welder-cards-grid"></div>
            </div>
          </div>
          <div class="card" id="newWelderCard" style="position:sticky;top:24px;">
            <h3>Nuevo Registro</h3>
            <div style="display:grid;gap:10px;">
              <input id="masterWelderId" placeholder="Matr&iacute;cula / ID" />
              <input id="masterWelderName" placeholder="Nombre completo" />
              <select id="masterWelderStatus"><option value="activo">Activo</option><option value="inactivo">Inactivo</option></select>
            </div>
            <div class="btn-row"><button class="btn btn-primary" style="width:100%;" onclick="addMasterWelder()">Registrar Soldador</button></div>
            <div class="small" style="margin-top:12px;">Doble clic en tarjeta para abrir ficha completa.</div>
          </div>
        </div>
      </section>

      <!-- WPS (REDESIGNED) -->
      <section class="page" id="wps">
        <div class="topbar"><div class="title">WPS</div><div class="subtitle">Procedimientos de soldadura certificados.</div></div>
        <div class="card">
          <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;">
            <input type="text" id="wpsSearchInput" placeholder="Buscar por WPS, Proceso, Material..." oninput="renderWpsCards()" style="flex:1;min-width:200px;" />
            <button class="btn btn-primary" id="wpsAddBtn" onclick="openWpsModalAdd()" style="white-space:nowrap;">&#10133; Agregar nuevo WPS</button>
          </div>
        </div>
        <div id="wpsCardsContainer" class="wps-cards-grid"></div>
      </section>

      <!-- ADMIN -->
      <section class="page" id="admin">
        <div class="topbar"><div class="title">Administraci&oacute;n</div><div class="subtitle">Panel de control de usuarios y seguridad del sistema.</div></div>
        <div class="grid-2">
          <div>
            <div class="card">
              <div class="admin-section-title">Crear usuario de Confianza</div>
              <div style="display:grid;gap:12px;">
                <div class="field-group"><label class="field-label">Nombre completo</label><input id="adminNewUserName" placeholder="Nombre del usuario" /></div>
                <div class="field-group"><label class="field-label">Contrase&ntilde;a de acceso</label>
                  <div class="pass-field-wrap"><input id="adminNewUserPass" type="password" placeholder="Contrase&ntilde;a" /><button class="eye-toggle" type="button" onclick="togglePassVisibility('adminNewUserPass', this)">&#128065;</button></div>
                </div>
              </div>
              <div class="section-badge" style="margin-top:14px;">M&oacute;dulos permitidos</div>
              <div class="soc-check-grid">
                <div class="soc-check-item"><input type="checkbox" id="adminPermStock" checked /><label for="adminPermStock">Stock</label></div>
                <div class="soc-check-item"><input type="checkbox" id="adminPermCalif" /><label for="adminPermCalif">Calificaci&oacute;n</label></div>
                <div class="soc-check-item"><input type="checkbox" id="adminPermCert" /><label for="adminPermCert">Certificados</label></div>
                <div class="soc-check-item"><input type="checkbox" id="adminPermWps" /><label for="adminPermWps">WPS</label></div>
              </div>
              <div class="btn-row"><button class="btn btn-primary" style="width:100%;" onclick="addConfianzaUser()">Crear Usuario</button></div>
            </div>
            <div class="admin-change-pass-card">
              <h3>&#128274; Cambiar contrase&ntilde;a de Creador</h3>
              <div style="display:grid;gap:10px;">
                <div class="pass-field-wrap"><input id="creadorOldPass" type="password" placeholder="Contrase&ntilde;a actual" /><button class="eye-toggle" type="button" onclick="togglePassVisibility('creadorOldPass', this)" style="color:rgba(255,255,255,0.6);">&#128065;</button></div>
                <div class="pass-field-wrap"><input id="creadorNewPass" type="password" placeholder="Nueva contrase&ntilde;a" /><button class="eye-toggle" type="button" onclick="togglePassVisibility('creadorNewPass', this)" style="color:rgba(255,255,255,0.6);">&#128065;</button></div>
                <div class="pass-field-wrap"><input id="creadorNewPass2" type="password" placeholder="Confirmar nueva contrase&ntilde;a" /><button class="eye-toggle" type="button" onclick="togglePassVisibility('creadorNewPass2', this)" style="color:rgba(255,255,255,0.6);">&#128065;</button></div>
              </div>
              <div class="btn-row"><button class="btn btn-success" style="width:100%;" onclick="changeCreadorPassword()">Actualizar Contrase&ntilde;a</button></div>
            </div>
          </div>
          <div class="card">
            <div class="admin-section-title">Usuarios de Confianza</div>
            <div id="adminUsersList"></div>
          </div>
        </div>
      </section>

    </main>
  </div>

  <!-- ===== MODAL SOLDADOR ===== -->
  <div class="modal" id="welderModal">
    <div class="modal-card">
      <div class="modal-header">
        <div><div class="title" id="modalWelderName">Soldador</div><div class="subtitle" id="modalWelderId">Matr&iacute;cula</div></div>
        <button class="btn btn-secondary" onclick="closeModal('welderModal')">&#10005; Cerrar</button>
      </div>
      <div class="modal-body">
        <div class="grid-2" style="margin-bottom:16px;">
          <div style="display:flex;gap:16px;">
            <div>
              <div class="photo-box" id="modalPhotoBox">Sin foto</div>
              <input type="file" accept="image/*" onchange="loadWelderPhoto(event)" style="font-size:11px;margin-top:8px;" id="welderPhotoInput" />
            </div>
            <div class="card" style="margin:0;box-shadow:none;flex:1;">
              <div class="section-title">Datos</div>
              <div id="modalBasicData"></div>
            </div>
          </div>
          <div class="card" style="margin:0;box-shadow:none;">
            <div class="section-title">Estatus</div>
            <div class="form-grid-2">
              <select id="modalStatusChange" onchange="updateCurrentWelderStatus(this.value)"><option value="activo">Activo</option><option value="inactivo">Inactivo</option></select>
              <button class="btn btn-danger" id="deleteWelderBtn" onclick="deleteCurrentWelder()">Eliminar</button>
            </div>
          </div>
        </div>
        <div class="card" style="box-shadow:none;">
          <div class="section-title">Certificaciones</div>
          <div class="form-grid" id="certAddForm">
            <input id="newCertWps" placeholder="WPS" />
            <input id="newCertPosition" placeholder="Posici&oacute;n" />
            <input id="newCertProcess" placeholder="Proceso" />
            <input id="newCertThickness" placeholder="Espesor" />
          </div>
          <div class="form-grid" style="margin-top:10px;" id="certAddForm2">
            <input id="newCertDiameter" placeholder="Di&aacute;metro" />
            <input id="newCertQualDate" type="date" title="Fecha calificaci&oacute;n" />
            <input id="newCertExpiryDate" type="date" title="Vencimiento" />
            <select id="newCertSociety"><option value="">Sociedad</option><option>ABS</option><option>LR</option><option>DNV</option><option>BV</option><option>CWI</option><option>RINA</option></select>
          </div>
          <div class="btn-row" id="certAddBtnRow"><button class="btn btn-primary" onclick="addCertToCurrentWelder()">Agregar certificaci&oacute;n</button></div>
          <div class="table-shell" style="margin-top:16px;"><table><thead><tr><th>WPS</th><th>Posici&oacute;n</th><th>Proceso</th><th>Espesor</th><th>Di&aacute;metro</th><th>Calif.</th><th>Venc.</th><th>Sociedad</th><th>Acc.</th></tr></thead><tbody id="modalCertTableBody"></tbody></table></div>
        </div>
      </div>
    </div>
  </div>

  <!-- ===== MODAL EDITAR SOLDADOR DEL PROYECTO ===== -->
  <div class="modal" id="editProjectWelderModal">
    <div class="modal-card" style="width:min(700px,95%);">
      <div class="modal-header">
        <div><div class="title" style="font-size:18px;">Modificar Soldador</div><div class="subtitle" id="editWelderInfo">Edici&oacute;n de datos del soldador en el proyecto</div></div>
        <button class="btn btn-secondary" onclick="closeModal('editProjectWelderModal')">&#10005; Cerrar</button>
      </div>
      <div class="modal-body">
        <div class="section-badge">Datos del soldador</div>
        <div class="form-grid-2" style="margin-bottom:14px;">
          <div><label class="field-label">Matr&iacute;cula</label><input id="editWelderId" readonly style="background:#f8fafc;" /></div>
          <div><label class="field-label">Nombre</label><input id="editWelderName" readonly style="background:#f8fafc;" /></div>
        </div>
        <div class="section-badge">Datos del proyecto</div>
        <div class="form-grid-2" style="margin-bottom:14px;">
          <div><label class="field-label">WPS</label><select id="editWelderWps"></select></div>
          <div><label class="field-label">Posiciones</label><input id="editWelderPos" placeholder="Posiciones (3G/4G)" /></div>
        </div>
        <div class="form-grid-2" style="margin-bottom:14px;">
          <div><label class="field-label">Espesor placa</label><input id="editWelderPlateThickness" placeholder="Espesor placa" /></div>
          <div><label class="field-label">&Oslash; tuber&iacute;a</label><input id="editWelderPipeDiameter" placeholder="&Oslash; tuber&iacute;a" /></div>
        </div>
        <div class="form-grid-2" style="margin-bottom:14px;">
          <div><label class="field-label">Inspector clase</label><input id="editClassInspector" placeholder="Inspector clase" /></div>
          <div><label class="field-label">Inspector calidad</label><input id="editQcInspector" placeholder="Inspector calidad" /></div>
        </div>
        <div style="margin-bottom:14px;"><label class="field-label">WPQ</label><input id="editWpqNo" placeholder="WPQ" /></div>
        <div class="btn-row">
          <button class="btn btn-primary" onclick="saveEditedProjectWelder()">&#128190; Guardar Cambios</button>
          <button class="btn btn-secondary" onclick="closeModal('editProjectWelderModal')">Cancelar</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ===== MODAL INSPECCION ===== -->
  <div class="modal" id="inspeccionModal">
    <div class="modal-card" style="width:min(700px,95%);">
      <div class="modal-header">
        <div><div class="title" style="font-size:18px;">Inspecci&oacute;n Visual</div><div class="subtitle" id="inspeccionWelderInfo">Soldador</div></div>
        <button class="btn btn-secondary" onclick="closeModal('inspeccionModal')">&#10005; Cerrar</button>
      </div>
      <div class="modal-body">
        <div class="section-badge">Resultados por Posici&oacute;n</div>
        <div class="table-shell insp-table">
          <table>
            <thead><tr><th>Posici&oacute;n</th><th>Ra&iacute;z</th><th>Vista</th></tr></thead>
            <tbody id="inspeccionTableBody"></tbody>
          </table>
        </div>
        <div class="btn-row">
          <button class="btn btn-secondary" onclick="addInspeccionRow()">+ Agregar posici&oacute;n</button>
          <button class="btn btn-primary" onclick="saveInspeccion()">&#128190; Guardar</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ===== MODAL DOBLEZ ===== -->
  <div class="modal" id="doblezModal">
    <div class="modal-card" style="width:min(920px,95%);">
      <div class="modal-header">
        <div><div class="title" style="font-size:18px;">Prueba de Doblez Guiado</div><div class="subtitle" id="doblezWelderInfo">Soldador</div></div>
        <button class="btn btn-secondary" onclick="closeModal('doblezModal')">&#10005; Cerrar</button>
      </div>
      <div class="modal-body">
        <div class="section-badge">Encabezado del Reporte</div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Fecha del reporte</label><input id="doblezReportDate" type="date" /></div>
          <div class="field-group"><label class="field-label">Reporte N&ordm;</label><input id="doblezReportNo" placeholder="N&uacute;mero de reporte" /></div>
        </div>
        <div class="section-badge">Informaci&oacute;n del Soldador / Operador</div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Nombre del soldador</label><input id="doblezWelderName" readonly style="background:#f8fafc;" /></div>
          <div class="field-group"><label class="field-label">Matr&iacute;cula</label><input id="doblezWelderId" readonly style="background:#f8fafc;" /></div>
        </div>
        <div class="field-group" style="margin-bottom:10px;"><label class="field-label">Proceso de soldadura</label>
          <div class="process-check-group"><label><input type="checkbox" id="doblezProcManual"> Manual</label><label><input type="checkbox" id="doblezProcSemi"> Semiautom&aacute;tico</label><label><input type="checkbox" id="doblezProcMech"> Mecanizado</label></div>
        </div>
        <div class="form-grid-3" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">WPS</label><input id="doblezWps" readonly style="background:#f8fafc;" /></div>
          <div class="field-group"><label class="field-label">WPQ</label><input id="doblezWpq" readonly style="background:#f8fafc;" /></div>
          <div class="field-group"><label class="field-label">Posici&oacute;n(es)</label><input id="doblezPositions" readonly style="background:#f8fafc;" /></div>
        </div>
        <div class="section-badge">Descripci&oacute;n de la Prueba</div>
        <div class="form-grid-3" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Especificaci&oacute;n del material</label><input id="doblezMaterialSpec" placeholder="Ej: ASTM A36" /></div>
          <div class="field-group"><label class="field-label">Espesor</label><input id="doblezThickness" placeholder='Ej: 1/2" PLATE' /></div>
          <div class="field-group"><label class="field-label">Di&aacute;metro (tuber&iacute;a)</label><input id="doblezDiameter" placeholder='Ej: 2" SCH 40' /></div>
        </div>
        <div class="form-grid-3" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Descripci&oacute;n</label><input id="doblezDescription" placeholder="Descripci&oacute;n de la prueba" /></div>
          <div class="field-group"><label class="field-label">M&eacute;todo de Doblez</label><select id="doblezBendMethod"><option value="guided">Doblez Guiado</option><option value="free">Doblez Libre</option></select></div>
          <div class="field-group"><label class="field-label">Norma / Est&aacute;ndar</label><input id="doblezStandard" placeholder="Ej: AWS D1.1:2020" /></div>
        </div>
        <div class="section-badge">Resultados / Results</div>
        <div class="table-shell"><table><thead><tr><th>Tipo / Type</th><th>Posici&oacute;n</th><th>Resultado</th><th>Acc.</th></tr></thead><tbody id="doblezTableBody"></tbody></table></div>
        <div class="btn-row"><button class="btn btn-secondary btn-sm" onclick="addDoblezRow()">+ Agregar fila</button></div>
        <div class="field-group" style="margin-top:16px;"><label class="field-label">Observaciones</label><textarea id="doblezRemarks" rows="3" placeholder="Observaciones..."></textarea></div>
        <div class="section-badge" style="margin-top:4px;">Evidencia y Resultado Final</div>
        <div class="grid-2" style="margin-bottom:16px;">
          <div class="card" style="box-shadow:none;margin:0;">
            <div class="soft-caption" style="margin-bottom:8px;">Evidencia fotogr&aacute;fica</div>
            <div class="photo-box" id="doblezPhotoBox" style="width:100%;height:180px;">Sin foto</div>
            <input type="file" accept="image/*" onchange="loadDoblezPhoto(event)" style="font-size:11px;margin-top:8px;" />
          </div>
          <div class="card" style="box-shadow:none;margin:0;">
            <div class="soft-caption" style="margin-bottom:8px;">Resultado Final</div>
            <select id="doblezResultadoFinal" style="font-size:16px;padding:14px;margin-bottom:12px;" onchange="updateDoblezResultColor()">
              <option value="">Seleccionar resultado...</option>
              <option value="aprobado">APROBADO</option>
              <option value="reprobado">REPROBADO</option>
            </select>
            <div class="field-group"><label class="field-label">Fecha de inspecci&oacute;n</label><input id="doblezTestDate" type="date" /></div>
            <div class="field-group" style="margin-top:8px;"><label class="field-label">Realizado por</label><input id="doblezPerformedBy" placeholder="Inspector de Clase" /></div>
            <div class="field-group" style="margin-top:8px;"><label class="field-label">Aprobado por</label><input id="doblezApprovedBy" placeholder="Dpto. Control de Calidad" /></div>
          </div>
        </div>
        <div class="btn-row" style="justify-content:flex-end;border-top:1px solid var(--line);padding-top:16px;">
          <button class="btn btn-primary" onclick="saveDoblez()">&#128190; Guardar Doblez</button>
          <button class="btn btn-warn" onclick="printDoblezFormat()">&#128424; Imprimir Formato</button>
          <button class="btn btn-secondary" onclick="closeModal('doblezModal')">Cerrar</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ===== MODAL CERTIFICADO ===== -->
  <div class="modal" id="certificadoModal">
    <div class="modal-card" style="width:min(980px,95%);">
      <div class="modal-header">
        <div><div class="title" style="font-size:18px;">Certificado de Calificaci&oacute;n</div><div class="subtitle" id="certificadoWelderInfo">Process Instruction Check Sheet</div></div>
        <button class="btn btn-secondary" onclick="closeModal('certificadoModal')">&#10005; Cerrar</button>
      </div>
      <div class="modal-body">
        <div class="section-badge">Informaci&oacute;n General</div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Buque / Vessel</label><input id="certVessel" placeholder="Nombre del buque" /></div>
          <div class="field-group"><label class="field-label">Astillero / Client</label><input id="certShipyard" readonly style="background:#f8fafc;" /></div>
          <div class="field-group"><label class="field-label">No. Casco TNG</label><input id="certHullNo" placeholder="N&ordm; de casco" /></div>
          <div class="field-group"><label class="field-label">No. Reporte (WPQ)</label><input id="certReportNo" readonly style="background:#f8fafc;" /></div>
          <div class="field-group"><label class="field-label">ABS ID / PID / CIP</label><input id="certAbsId" placeholder="ABS ID" /></div>
          <div class="field-group"><label class="field-label">Fecha</label><input id="certDate" type="date" /></div>
          <div class="field-group" style="grid-column:span 2;"><label class="field-label">Puerto</label><input id="certPort" value="Veracruz, Ver., M&eacute;xico" /></div>
        </div>
        <div class="section-badge">Registro del Soldador</div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Nombre</label><input id="certWelderName" readonly style="background:#f8fafc;" /></div>
          <div class="field-group"><label class="field-label">Matr&iacute;cula</label><input id="certWelderId" readonly style="background:#f8fafc;" /></div>
        </div>
        <div class="field-group" style="margin-bottom:10px;"><label class="field-label">Proceso de soldadura</label>
          <div class="process-check-group"><label><input type="checkbox" id="certProcManual"> Manual</label><label><input type="checkbox" id="certProcSemi"> Semiautom&aacute;tico</label><label><input type="checkbox" id="certProcMachine"> M&aacute;quina</label></div>
        </div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Posici&oacute;n</label><input id="certPosition" readonly style="background:#f8fafc;" /></div>
          <div class="field-group"><label class="field-label">WPS No.</label><input id="certWps" readonly style="background:#f8fafc;" /></div>
          <div class="field-group"><label class="field-label">Material</label><input id="certMaterialSpec" placeholder="Ej: ASTM A36" /></div>
          <div class="field-group"><label class="field-label">Espesor / Di&aacute;metro</label><input id="certThicknessOrDia" placeholder='Ej: 1" PLATE' /></div>
          <div class="field-group" style="grid-column:span 2;"><label class="field-label">Rango que califica</label><input id="certThicknessRange" placeholder='Ej: 1/8" to 1 1/4"' /></div>
        </div>
        <div class="section-badge">Metal de Aporte</div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Especificaci&oacute;n No.</label><input id="certFillerSpec" placeholder="Ej: AWS SFA. 5.20" /></div>
          <div class="field-group"><label class="field-label">Clasificaci&oacute;n</label><input id="certFillerClass" /></div>
          <div class="field-group"><label class="field-label">No.</label><input id="certFillerNo" /></div>
          <div class="field-group"><label class="field-label">Descripci&oacute;n</label><input id="certFillerDesc" value="N/A" /></div>
          <div class="field-group"><label class="field-label">Respaldo?</label><select id="certBackingStrip"><option value="SI">S&Iacute;</option><option value="NO">NO</option></select></div>
          <div class="field-group"><label class="field-label">Di&aacute;metro y nombre</label><input id="certFillerDia" /></div>
          <div class="field-group" style="grid-column:span 2;"><label class="field-label">Flux / Gas</label><input id="certFlux" /></div>
        </div>
        <div class="section-badge">Inspecci&oacute;n Visual</div>
        <div class="form-grid-3" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Apariencia</label><select id="certVisualAppearance"><option value="">Seleccionar...</option><option value="BUENA">BUENA</option><option value="ACEPTABLE">ACEPTABLE</option><option value="NO ACEPTABLE">NO ACEPTABLE</option></select></div>
          <div class="field-group"><label class="field-label">Socavado</label><select id="certUndercut"><option value="">Seleccionar...</option><option value="ACEPTABLE">ACEPTABLE</option><option value="NO ACEPTABLE">NO ACEPTABLE</option></select></div>
          <div class="field-group"><label class="field-label">Porosidad</label><input id="certPipingPorosity" /></div>
        </div>
        <div class="section-badge">Doblez Guiado</div>
        <div class="table-shell" style="margin-bottom:8px;"><table><thead><tr><th>Especificaci&oacute;n</th><th>Figura</th><th>Lado</th><th>Muestra</th><th>Resultado</th></tr></thead><tbody id="certBendTableBody"></tbody></table></div>
        <div class="btn-row" style="margin-top:6px;"><button class="btn btn-sm btn-secondary" onclick="addCertBendRow()">+ Agregar fila de doblez</button></div>
        <div class="section-badge">Prueba Radiogr&aacute;fica</div>
        <div class="table-shell" style="margin-bottom:8px;"><table><thead><tr><th>Identificaci&oacute;n</th><th>Resultados</th><th>Observaciones</th><th>Acc.</th></tr></thead><tbody id="certRadioTableBody"></tbody></table></div>
        <div class="btn-row" style="margin-top:6px;"><button class="btn btn-sm btn-secondary" onclick="addCertRadioRow()">+ Agregar fila radiogr&aacute;fica</button></div>
        <div class="section-badge">Firmas y Aprobaciones</div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Presenciada por</label><input id="certWitnessedBy" /></div>
          <div class="field-group"><label class="field-label">Contratista</label><input id="certContractor" value="TALLERES NAVALES DEL GOLFO S.A. DE C.V." /></div>
          <div class="field-group"><label class="field-label">Inspector</label><input id="certSurveyorName" /></div>
          <div class="field-group"><label class="field-label">Fecha firma</label><input id="certSignDate" type="date" /></div>
        </div>
        <div class="btn-row" style="justify-content:flex-end;border-top:1px solid var(--line);padding-top:16px;">
          <button class="btn btn-primary" onclick="saveCertificado()">&#128190; Guardar Certificado</button>
          <button class="btn btn-warn" onclick="printCertificadoFormat()">&#128424; Imprimir Certificado</button>
          <button class="btn btn-secondary" onclick="closeModal('certificadoModal')">Cerrar</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ===== MODAL LISTA INSPECCION ===== -->
  <div class="modal" id="inspeccionListModal">
    <div class="modal-card" style="width:min(1100px,95%);">
      <div class="modal-header">
        <div><div class="title" style="font-size:18px;">Lista de Inspecci&oacute;n del Proyecto</div><div class="subtitle" id="inspeccionListProjectInfo">Proyecto</div></div>
        <button class="btn btn-secondary" onclick="closeModal('inspeccionListModal')">&#10005; Cerrar</button>
      </div>
      <div class="modal-body">
        <div id="inspeccionListContent"></div>
        <div class="btn-row" style="margin-top:16px;justify-content:flex-end;">
          <button class="btn btn-primary" onclick="printInspeccionList()">&#128424; Imprimir Lista</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ===== MODAL WPS (ADD/VIEW/EDIT) ===== -->
  <div class="modal" id="wpsModal">
    <div class="modal-card" style="width:min(1020px,95%);">
      <div class="modal-header">
        <div><div class="title" style="font-size:18px;" id="wpsModalTitle">Agregar WPS</div><div class="subtitle" id="wpsModalSubtitle">Nuevo procedimiento de soldadura</div></div>
        <button class="btn btn-secondary" onclick="closeModal('wpsModal')">&#10005; Cerrar</button>
      </div>
      <div class="modal-body">
        <!-- WPS Number -->
        <div class="form-grid-2" style="margin-bottom:14px;">
          <div class="field-group"><label class="field-label">N&uacute;mero / Nombre del WPS</label><input id="wf_no" placeholder="Ej: 222-AI240 REV.0" /></div>
          <div class="field-group"><label class="field-label">Proceso Principal</label><input id="wf_proceso" placeholder="Ej: FCAW, SMAW/FCAW, GMAW" /></div>
        </div>

        <!-- MATERIAL BASE -->
        <div class="section-badge">Material Base</div>
        <div class="form-grid-3" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Especificaci&oacute;n</label><input id="wf_mb_espec" /></div>
          <div class="field-group"><label class="field-label">Grado de Mat.</label><input id="wf_mb_grado" /></div>
          <div class="field-group"><label class="field-label">P.No. / Grupo No.</label><input id="wf_mb_pno" /></div>
        </div>
        <div class="form-grid-3" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Di&aacute;metro Calif.</label><input id="wf_mb_diametro" /></div>
          <div class="field-group"><label class="field-label">Espesor Calif.</label><input id="wf_mb_espesor" /></div>
          <div class="field-group"><label class="field-label">Filete Calif.</label><input id="wf_mb_filete" /></div>
        </div>

        <!-- POSICIONES -->
        <div class="section-badge">Posiciones</div>
        <div class="form-grid-3" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Posiciones</label><input id="wf_pos" /></div>
          <div class="field-group"><label class="field-label">Posici&oacute;n de Filete</label><input id="wf_pos_filete" /></div>
          <div class="field-group"><label class="field-label">Progresi&oacute;n</label><input id="wf_pos_progresion" /></div>
        </div>

        <!-- PRECALENTAMIENTO -->
        <div class="section-badge">Precalentamiento</div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Temp. de Precal.</label><input id="wf_pre_temp" /></div>
          <div class="field-group"><label class="field-label">Temp. de Interpass</label><input id="wf_pre_interpass" /></div>
        </div>

        <!-- METAL DE APORTE -->
        <div class="section-badge">Metal de Aporte</div>
        <div class="form-grid-3" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Proceso</label><input id="wf_ma_proceso" /></div>
          <div class="field-group"><label class="field-label">F. No.</label><input id="wf_ma_fno" /></div>
          <div class="field-group"><label class="field-label">A. No.</label><input id="wf_ma_ano" /></div>
        </div>
        <div class="form-grid-3" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">S.F.</label><input id="wf_ma_sf" /></div>
          <div class="field-group"><label class="field-label">AWS No (Clasif.)</label><input id="wf_ma_aws" /></div>
          <div class="field-group"><label class="field-label">Di&aacute;metro de Apor.</label><input id="wf_ma_diametro" /></div>
        </div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Flux</label><input id="wf_ma_flux" /></div>
          <div class="field-group"><label class="field-label">Nombre Comer.</label><input id="wf_ma_nombre" /></div>
        </div>

        <!-- GAS -->
        <div class="section-badge">Gas</div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Gas de Protec.</label><input id="wf_gas_protec" /></div>
          <div class="field-group"><label class="field-label">Flujo (CFH)</label><input id="wf_gas_flujo" /></div>
        </div>

        <!-- TECNICA -->
        <div class="section-badge">T&eacute;cnica</div>
        <div class="form-grid-3" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Tipo de Pasadas</label><input id="wf_tec_pasadas" /></div>
          <div class="field-group"><label class="field-label">&Aacute;ngulo de Elect.</label><input id="wf_tec_angulo" /></div>
          <div class="field-group"><label class="field-label">Distancia de Cont.</label><input id="wf_tec_distancia" /></div>
        </div>

        <!-- CARACTERISTICAS ELECTRICAS -->
        <div class="section-badge">Caracter&iacute;sticas El&eacute;ctricas</div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Corriente</label><input id="wf_ce_corriente" /></div>
          <div class="field-group"><label class="field-label">Polaridad</label><input id="wf_ce_polaridad" /></div>
          <div class="field-group"><label class="field-label">Electrodo</label><input id="wf_ce_electrodo" /></div>
          <div class="field-group"><label class="field-label">Transferencia</label><input id="wf_ce_transferencia" /></div>
        </div>

        <!-- CARACTERISTICAS ELECTRICAS POR POSICION (TABBED) -->
        <div class="section-badge">Caracter&iacute;sticas El&eacute;ctricas para el Metal de Aporte</div>
        <div class="wps-tabs" id="wpsCeTabs">
          <!-- Rendered dynamically by JS -->
        </div>
        <div id="wpsCeTabContent">
          <!-- Tab content rendered by JS -->
        </div>

        <!-- NORMA Y CLASE CERTIFICADORA -->
        <div class="section-badge">Norma y Clase Certificadora</div>
        <div class="form-grid-2" style="margin-bottom:10px;">
          <div class="field-group"><label class="field-label">Normas</label><input id="wf_normas" placeholder="Ej: AWS D1.1:2020" /></div>
          <div></div>
        </div>
        <div style="margin-bottom:10px;">
          <label class="field-label">Certificadora</label>
          <div class="soc-check-grid">
            <div class="soc-check-item soc-abs"><input type="checkbox" id="wf_soc_abs" /><label for="wf_soc_abs">ABS</label></div>
            <div class="soc-check-item soc-lr"><input type="checkbox" id="wf_soc_lr" /><label for="wf_soc_lr">LR</label></div>
            <div class="soc-check-item soc-dnv"><input type="checkbox" id="wf_soc_dnv" /><label for="wf_soc_dnv">DNV</label></div>
            <div class="soc-check-item soc-bv"><input type="checkbox" id="wf_soc_bv" /><label for="wf_soc_bv">BV</label></div>
            <div class="soc-check-item soc-cwi"><input type="checkbox" id="wf_soc_cwi" /><label for="wf_soc_cwi">CWI</label></div>
            <div class="soc-check-item soc-rina"><input type="checkbox" id="wf_soc_rina" /><label for="wf_soc_rina">RINA</label></div>
          </div>
          <div style="margin-top:8px;display:flex;gap:8px;align-items:center;">
            <input id="wf_soc_custom" placeholder="Agregar otra sociedad..." style="max-width:200px;" />
            <button class="btn btn-sm btn-secondary" onclick="addCustomSociety()">+ Agregar</button>
          </div>
          <div id="wf_custom_societies" style="display:flex;gap:6px;flex-wrap:wrap;margin-top:8px;"></div>
        </div>

        <!-- ACTION BUTTONS -->
        <div class="btn-row" id="wpsModalActions" style="justify-content:flex-end;border-top:1px solid var(--line);padding-top:16px;">
          <button class="btn btn-primary" id="wpsModalSaveBtn" onclick="saveWpsFromModal()">&#128190; Guardar WPS</button>
          <button class="btn btn-warn" id="wpsModalModifyBtn" onclick="setWpsModalEditable()" style="display:none;">&#9998; Modificar</button>
          <button class="btn btn-danger btn-sm" id="wpsModalDeleteBtn" onclick="deleteWpsFromModal()" style="display:none;">Eliminar</button>
          <button class="btn btn-secondary" onclick="closeModal('wpsModal')">Cerrar</button>
        </div>
      </div>
    </div>
  </div>

  <script>
    // ===================== CONSTANTS =====================
    const LOGO_URL = 'https://customer-assets.emergentagent.com/job_954bd461-6438-4194-8adb-960c1ce79792/artifacts/hyg0xidk_Logo%20para%20doctos.png';
    const CREATOR_PASSWORD = '1234';
    const KNOWN_SOCIETIES = ['ABS', 'LR', 'DNV', 'BV', 'CWI', 'RINA'];
    const SOC_COLORS = { ABS: 'soc-abs', LR: 'soc-lr', DNV: 'soc-dnv', BV: 'soc-bv', CWI: 'soc-cwi', RINA: 'soc-rina' };

    // ===================== GLOBAL STATE =====================
    const state = {
      stock: [],
      selectedStock: [],
      wps: [],
      projects: [],
      activeProject: null,
      masterWelders: [],
      currentWelderIndex: null,
      editingWelderIndex: null,
      auth: { role: 'invitado', userId: null, userName: '' },
      users: [],
      creadorPassword: null,
      wpsModal: { mode: 'add', index: null, activeTab: null, customSocieties: [] }
    };

    // ===================== PERMISSIONS =====================
    function canView(mod) {
      if (state.auth.role === 'creador') return true;
      if (state.auth.role === 'invitado') return ['stock','certificados','wps'].includes(mod);
      if (state.auth.role === 'confianza') {
        const u = state.users.find(x => x.id === state.auth.userId);
        return u && u.modules && u.modules[mod];
      }
      return false;
    }
    function canEdit(mod) {
      if (state.auth.role === 'creador') return true;
      if (state.auth.role === 'invitado') return mod === 'stock_qty';
      if (state.auth.role === 'confianza') {
        if (mod === 'wps') return false; // Confianza can only VIEW WPS
        const u = state.users.find(x => x.id === state.auth.userId);
        return u && u.modules && u.modules[mod];
      }
      return false;
    }
    function canDelete(mod) {
      if (state.auth.role === 'creador') return true;
      if (state.auth.role === 'confianza') {
        if (mod === 'wps') return false; // Confianza cannot delete WPS
        const u = state.users.find(x => x.id === state.auth.userId);
        return u && u.modules && u.modules[mod];
      }
      return false;
    }

    // ===================== AUTH / LOGIN =====================
    let selectedLoginRole = null;
    function selectLoginRole(role) {
      selectedLoginRole = role;
      document.querySelectorAll('.role-card').forEach(c => c.classList.remove('active-role'));
      document.querySelector(`.role-card[data-role="${role}"]`).classList.add('active-role');
      const passArea = document.getElementById('loginPasswordArea');
      const confSelect = document.getElementById('loginConfianzaSelect');
      document.getElementById('loginError').classList.remove('show');
      if (role === 'invitado') {
        passArea.classList.remove('show');
        confSelect.classList.remove('show');
      } else if (role === 'creador') {
        passArea.classList.add('show');
        confSelect.classList.remove('show');
        document.getElementById('loginPassword').value = '';
        document.getElementById('loginPassword').focus();
      } else {
        passArea.classList.add('show');
        confSelect.classList.add('show');
        document.getElementById('loginPassword').value = '';
        populateConfianzaSelect();
      }
    }
    function populateConfianzaSelect() {
      const sel = document.getElementById('loginConfianzaUser');
      sel.innerHTML = '<option value="">Seleccionar usuario...</option>';
      state.users.forEach(u => {
        sel.innerHTML += `<option value="${u.id}">${u.name}</option>`;
      });
    }
    function doLogin() {
      if (!selectedLoginRole) { showToast('Selecciona un tipo de usuario', true); return; }
      const errEl = document.getElementById('loginError');
      errEl.classList.remove('show');
      if (selectedLoginRole === 'invitado') {
        state.auth = { role: 'invitado', userId: null, userName: 'Invitado' };
        finishLogin();
      } else if (selectedLoginRole === 'creador') {
        const pass = document.getElementById('loginPassword').value;
        const currentCreadorPass = state.creadorPassword || CREATOR_PASSWORD;
        if (pass !== currentCreadorPass) { errEl.textContent = 'Contrase\u00f1a incorrecta'; errEl.classList.add('show'); return; }
        state.auth = { role: 'creador', userId: null, userName: 'Creador' };
        finishLogin();
      } else {
        const userId = document.getElementById('loginConfianzaUser').value;
        const pass = document.getElementById('loginPassword').value;
        if (!userId) { errEl.textContent = 'Selecciona un usuario'; errEl.classList.add('show'); return; }
        const user = state.users.find(u => u.id === userId);
        if (!user || user.password !== pass) { errEl.textContent = 'Contrase\u00f1a incorrecta'; errEl.classList.add('show'); return; }
        state.auth = { role: 'confianza', userId: user.id, userName: user.name };
        finishLogin();
      }
    }
    function finishLogin() {
      document.getElementById('loginOverlay').classList.add('hidden');
      applyPermissions();
      updateRoleIndicator();
      saveToStorage();
    }
    function doLogout() {
      state.auth = { role: 'invitado', userId: null, userName: '' };
      selectedLoginRole = null;
      document.querySelectorAll('.role-card').forEach(c => c.classList.remove('active-role'));
      document.getElementById('loginPasswordArea').classList.remove('show');
      document.getElementById('loginConfianzaSelect').classList.remove('show');
      document.getElementById('loginError').classList.remove('show');
      document.getElementById('loginOverlay').classList.remove('hidden');
      goToPage('inicio');
      saveToStorage();
    }
    function updateRoleIndicator() {
      const nameEl = document.getElementById('roleIndicatorName');
      const roleEl = document.getElementById('roleIndicatorRole');
      nameEl.textContent = state.auth.userName || '---';
      const labels = { creador: 'Creador - Control Total', confianza: 'Confianza', invitado: 'Invitado - Solo lectura' };
      roleEl.textContent = labels[state.auth.role] || '';
    }
    function applyPermissions() {
      const role = state.auth.role;
      // Sidebar nav
      document.querySelectorAll('.nav-btn[data-page]').forEach(btn => {
        const page = btn.dataset.page;
        if (page === 'inicio') return;
        if (page === 'admin') {
          btn.style.display = role === 'creador' ? 'block' : 'none';
          return;
        }
        btn.classList.toggle('disabled-nav', !canView(page));
      });
      document.getElementById('adminNavBtn').style.display = role === 'creador' ? 'block' : 'none';
      // Bottom nav
      document.querySelectorAll('#bottomNav button[data-page]').forEach(btn => {
        const page = btn.dataset.page;
        if (page === 'inicio') return;
        btn.classList.toggle('disabled-nav', !canView(page));
      });
      // Home tiles
      document.querySelectorAll('.menu-tile[data-module]').forEach(tile => {
        tile.classList.toggle('disabled-tile', !canView(tile.dataset.module));
      });
      // Stock: hide add form for invitado
      const stockAddCard = document.getElementById('stockAddCard');
      if (stockAddCard) stockAddCard.style.display = (role === 'invitado') ? 'none' : '';
      // Calificacion: hide new project for invitado
      const newProjCard = document.getElementById('newProjectCard');
      if (newProjCard) newProjCard.style.display = canEdit('calificacion') ? '' : 'none';
      // Certificados: hide new welder card for invitado
      const newWelderCard = document.getElementById('newWelderCard');
      if (newWelderCard) newWelderCard.style.display = canEdit('certificados') ? '' : 'none';
      const massBar = document.getElementById('massActionsBar');
      if (massBar) massBar.style.display = canEdit('certificados') ? '' : 'none';
      // WPS: hide add button for invitado
      const wpsAddBtn = document.getElementById('wpsAddBtn');
      if (wpsAddBtn) wpsAddBtn.style.display = canEdit('wps') ? '' : 'none';
      // Admin users list
      if (role === 'creador') renderAdminUsers();
    }

    // ===================== NAVIGATION =====================
    function goToPage(pageId) {
      if (pageId !== 'inicio' && pageId !== 'admin' && !canView(pageId)) {
        showToast('No tienes acceso a este m\u00f3dulo', true);
        return;
      }
      document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      document.getElementById(pageId)?.classList.add('active');
      document.querySelector(`.nav-btn[data-page="${pageId}"]`)?.classList.add('active');
      const app = document.querySelector('.app');
      if (pageId === 'inicio') { app.classList.add('home-mode'); } else { app.classList.remove('home-mode'); }
    }
    document.querySelectorAll('.nav-btn').forEach(btn => {
      btn.addEventListener('click', () => goToPage(btn.dataset.page));
    });
    function closeModal(modalId) { document.getElementById(modalId).classList.remove('show'); }

    // ===================== TOAST =====================
    function showSaveSuccess(message) { showToast(message, false); }
    function showToast(message, isError) {
      const toast = document.createElement('div');
      toast.className = 'save-toast' + (isError ? ' error-toast' : '');
      toast.textContent = (isError ? '! ' : '\u2713 ') + message;
      document.body.appendChild(toast);
      setTimeout(() => { if (toast.parentNode) document.body.removeChild(toast); }, 2500);
    }

    // ===================== STATUS HELPERS =====================
    function getInspStatus(w) {
      if (!w.inspeccion || !w.inspeccion.rows || !w.inspeccion.rows.length) return { cls:'pending', label:'\u2014', text:'Pendiente' };
      const filled = w.inspeccion.rows.filter(r => r.raiz || r.vista);
      if (!filled.length) return { cls:'pending', label:'\u2014', text:'Pendiente' };
      const anyReject = w.inspeccion.rows.some(r => r.raiz === 'r' || r.vista === 'r');
      return anyReject ? { cls:'bad', label:'R', text:'Requiere revisi\u00f3n' } : { cls:'ok', label:'OK', text:'Aprobado' };
    }
    function getDoblezStatus(w) {
      if (!w.doblez || !w.doblez.result) return { cls:'pending', label:'\u2014', text:'Pendiente' };
      return w.doblez.result === 'aprobado' ? { cls:'ok', label:'APR', text:'Aprobado' } : { cls:'bad', label:'REP', text:'Reprobado' };
    }
    function getCertStatus(w) {
      if (!w.certificado || !w.certificado.saved) return { cls:'pending', label:'\u2014', text:'Pendiente' };
      return { cls:'ok', label:'OK', text:'Guardado' };
    }

    // ===================== INIT HELPERS =====================
    function initDoblezData(w, p, wpsData) {
      if (!w.doblez) w.doblez = {};
      if (!Array.isArray(w.doblez.rows)) w.doblez.rows = [];
      if (!w.doblez.result) w.doblez.result = '';
      if (!w.doblez.photo) w.doblez.photo = '';
      if (w.doblez.procManual === undefined) w.doblez.procManual = false;
      if (w.doblez.procSemi === undefined) w.doblez.procSemi = true;
      if (w.doblez.procMech === undefined) w.doblez.procMech = false;
      if (w.doblez.reportDate === undefined) w.doblez.reportDate = p.date || '';
      if (w.doblez.reportNo === undefined) w.doblez.reportNo = '';
      if (w.doblez.materialSpec === undefined) w.doblez.materialSpec = wpsData.baseMaterial || wpsData.mb_espec || '';
      if (w.doblez.thickness === undefined) w.doblez.thickness = w.plateThickness || wpsData.thickness || wpsData.mb_espesor || '';
      if (w.doblez.diameter === undefined) w.doblez.diameter = w.pipeDiameter || wpsData.diameter || wpsData.mb_diametro || '';
      if (w.doblez.description === undefined) w.doblez.description = '';
      if (w.doblez.bendMethod === undefined) w.doblez.bendMethod = 'guided';
      if (w.doblez.standard === undefined) w.doblez.standard = 'AWS D1.1:2020';
      if (w.doblez.remarks === undefined) w.doblez.remarks = '';
      if (w.doblez.testDate === undefined) w.doblez.testDate = '';
      if (w.doblez.performedBy === undefined) w.doblez.performedBy = w.classInspector || '';
      if (w.doblez.approvedBy === undefined) w.doblez.approvedBy = w.qcInspector || '';
    }
    function initCertData(w, p, wpsData) {
      if (!w.certificado) w.certificado = {};
      const c = w.certificado;
      if (c.vessel === undefined) c.vessel = '';
      if (c.shipyard === undefined) c.shipyard = p.client || '';
      if (c.hullNo === undefined) c.hullNo = '';
      if (c.reportNo === undefined) c.reportNo = w.wpq ? 'WPQ - ' + w.wpq : '';
      if (c.absId === undefined) c.absId = '';
      if (c.date === undefined) c.date = p.date || '';
      if (c.port === undefined) c.port = 'Veracruz, Ver., M\u00e9xico';
      if (c.procManual === undefined) c.procManual = false;
      if (c.procSemi === undefined) c.procSemi = true;
      if (c.procMachine === undefined) c.procMachine = false;
      if (c.materialSpec === undefined) c.materialSpec = wpsData.baseMaterial || wpsData.mb_espec || '';
      if (c.thicknessOrDia === undefined) c.thicknessOrDia = w.plateThickness || wpsData.thickness || wpsData.mb_espesor || '';
      if (c.thicknessRange === undefined) c.thicknessRange = '';
      if (c.fillerSpec === undefined) c.fillerSpec = '';
      if (c.fillerClass === undefined) c.fillerClass = wpsData.filler || wpsData.ma_aws || '';
      if (c.fillerNo === undefined) c.fillerNo = '';
      if (c.fillerDesc === undefined) c.fillerDesc = 'N/A';
      if (c.backingStrip === undefined) c.backingStrip = 'SI';
      if (c.fillerDia === undefined) c.fillerDia = wpsData.fillerDiameter || wpsData.ma_diametro || '';
      if (c.flux === undefined) c.flux = wpsData.gas || wpsData.gas_protec || '';
      if (c.visualAppearance === undefined) c.visualAppearance = '';
      if (c.undercut === undefined) c.undercut = '';
      if (c.pipingPorosity === undefined) c.pipingPorosity = '';
      if (!Array.isArray(c.bendRows)) {
        const positions = (w.pos || '3G').split('/').map(s => s.trim()).filter(Boolean);
        c.bendRows = [];
        positions.forEach(pos => {
          c.bendRows.push({ spec: 'A.W.S. D1.1:2020', figure: 'Fig. 6.11', side: pos, sample: '1', result: '' });
          c.bendRows.push({ spec: 'A.W.S. D1.1:2020', figure: 'Fig. 6.11', side: pos, sample: '2', result: '' });
        });
        if (!c.bendRows.length) {
          c.bendRows = [
            { spec: 'A.W.S. D1.1:2020', figure: 'Fig. 6.11', side: '3G', sample: '1', result: '' },
            { spec: 'A.W.S. D1.1:2020', figure: 'Fig. 6.11', side: '4G', sample: '1', result: '' },
          ];
        }
      }
      if (!Array.isArray(c.radioRows)) c.radioRows = [{ filmId: '', results: '', remarks: '' }];
      if (c.witnessedBy === undefined) c.witnessedBy = '';
      if (c.contractor === undefined) c.contractor = 'TALLERES NAVALES DEL GOLFO S.A. DE C.V.';
      if (c.surveyorName === undefined) c.surveyorName = '';
      if (c.signDate === undefined) c.signDate = '';
      if (c.saved === undefined) c.saved = false;
    }

    // ===================== NORMALIZE WPS DATA =====================
    function normalizeWps(w) {
      if (!Array.isArray(w.societies)) {
        w.societies = w.society ? [w.society] : [];
      }
      if (!w.proceso) w.proceso = w.process || w.ma_proceso || '';
      if (!w.ce_tabs) w.ce_tabs = { _tabs: [{ id: 'tab_1', name: 'P\u00e1gina 1' }, { id: 'tab_2', name: 'P\u00e1gina 2' }], tab_1: [], tab_2: [] };
      return w;
    }

    // ===================== STOCK FUNCTIONS =====================
    function renderStock() {
      const tbody = document.getElementById('stockTableBody');
      tbody.innerHTML = '';
      if (!state.stock.length) {
        tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;padding:30px;color:#64748b;">No hay \u00edtems en el stock</td></tr>';
        renderStockSearchResults(); renderSelectedStockChips(); return;
      }
      const isInvitado = state.auth.role === 'invitado';
      state.stock.forEach((row, index) => {
        const isSelected = state.selectedStock.includes(index);
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="check-col"><input type="checkbox" ${isSelected ? 'checked' : ''} onchange="toggleStockSelection(${index}, this.checked)"></td>
          <td>${row.item}</td><td>${row.desc}</td><td>${row.unit}</td>
          <td><input type="number" class="qty-input" value="${row.qty}" onchange="editStockQty(${index}, this.value)" /></td>
          <td>${isInvitado ? '' : `
            <button class="btn btn-sm btn-warn" onclick="editStockItem(${index})" style="margin-right:4px;">Modificar</button>
            <button class="btn btn-sm btn-danger" onclick="deleteStock(${index})">Eliminar</button>
          `}</td>`;
        tbody.appendChild(tr);
      });
      renderStockSearchResults(); renderSelectedStockChips();
    }
    function addStockItem() {
      if (state.auth.role === 'invitado') { showToast('No tienes permiso', true); return; }
      const item = document.getElementById('stockItem').value.trim();
      const desc = document.getElementById('stockDesc').value.trim();
      const unit = document.getElementById('stockUnit').value;
      const qty = parseFloat(document.getElementById('stockQty').value) || 0;
      if (!item && !desc) return;
      state.stock.push({ item, desc, unit, qty });
      ['stockItem','stockDesc','stockQty'].forEach(id => document.getElementById(id).value = '');
      renderStock(); saveToStorage();
    }
    function editStockQty(index, value) { state.stock[index].qty = parseFloat(value) || 0; renderStockSearchResults(); renderSelectedStockChips(); saveToStorage(); }
    function editStockItem(index) {
      if (!canEdit('stock')) { showToast('No tienes permiso', true); return; }
      const row = state.stock[index];
      const newItem = prompt('\u00cdtem:', row.item); if (newItem === null) return;
      const newDesc = prompt('Descripci\u00f3n:', row.desc); if (newDesc === null) return;
      row.item = newItem; row.desc = newDesc; renderStock(); saveToStorage();
    }
    function deleteStock(i) {
      if (!canDelete('stock')) { showToast('No tienes permiso', true); return; }
      if (!confirm('\u00bfEliminar este \u00edtem del stock?')) return;
      state.stock.splice(i, 1);
      state.selectedStock = state.selectedStock.filter(idx => idx !== i).map(idx => idx > i ? idx - 1 : idx);
      renderStock(); saveToStorage();
    }
    function toggleStockSelection(index, checked) {
      if (checked) { if (!state.selectedStock.includes(index)) state.selectedStock.push(index); }
      else { state.selectedStock = state.selectedStock.filter(i => i !== index); }
      renderSelectedStockChips(); renderStockSearchResults(); renderStock();
    }
    function renderStockSearchResults() {
      const term = (document.getElementById('stockSearch')?.value || '').toLowerCase().trim();
      const box = document.getElementById('stockSearchResults'); if (!box) return;
      const filtered = state.stock.map((item, index) => ({ ...item, index })).filter(item => !term || item.item.toLowerCase().includes(term) || item.desc.toLowerCase().includes(term));
      box.innerHTML = '';
      if (!filtered.length) { box.innerHTML = '<div class="stock-result-item"><span class="small">No hay coincidencias.</span></div>'; return; }
      filtered.forEach(row => {
        const selected = state.selectedStock.includes(row.index);
        const div = document.createElement('div'); div.className = 'stock-result-item';
        div.innerHTML = `<div><strong>${row.item}</strong><br><span class="small">${row.desc} \u00b7 ${row.qty} ${row.unit}</span></div><button onclick="toggleStockSelection(${row.index}, ${!selected})">${selected ? 'Quitar' : 'Seleccionar'}</button>`;
        box.appendChild(div);
      });
    }
    function renderSelectedStockChips() {
      const wrap = document.getElementById('selectedStockChips'); if (!wrap) return;
      wrap.innerHTML = '';
      if (!state.selectedStock.length) { wrap.innerHTML = '<span class="small">No hay \u00edtems seleccionados.</span>'; return; }
      state.selectedStock.forEach(index => {
        const row = state.stock[index]; if (!row) return;
        const chip = document.createElement('div'); chip.className = 'selected-chip';
        chip.innerHTML = `<span>${row.item} \u00b7 ${row.qty} ${row.unit}</span><button onclick="toggleStockSelection(${index}, false)">\u00d7</button>`;
        wrap.appendChild(chip);
      });
    }
    function clearSelectedStock() { state.selectedStock = []; renderStock(); }
    function selectAllVisibleStock() {
      const term = (document.getElementById('stockSearch')?.value || '').toLowerCase().trim();
      state.stock.forEach((item, index) => { const visible = !term || item.item.toLowerCase().includes(term) || item.desc.toLowerCase().includes(term); if (visible && !state.selectedStock.includes(index)) state.selectedStock.push(index); });
      renderStock();
    }
    function printSelectedStock() {
      const rows = state.selectedStock.map(i => state.stock[i]).filter(Boolean);
      if (!rows.length) { alert('Selecciona al menos un \u00edtem para imprimir.'); return; }
      const htmlRows = rows.map(r => `<tr><td>${r.item}</td><td>${r.desc}</td><td>${r.unit}</td><td>${r.qty}</td></tr>`).join('');
      const pw = window.open('', '_blank');
      pw.document.write(`<html><head><title>Lista de surtido</title><style>body{font-family:Arial,sans-serif;padding:24px;color:#1B365D}.logo{max-width:180px;margin-bottom:16px}table{width:100%;border-collapse:collapse;margin-top:16px}th,td{border:1px solid #cbd5e1;padding:10px;text-align:left}th{background:#1B365D;color:#fff}</style></head><body><img src="${LOGO_URL}" class="logo"><h2>W&W - Lista de surtido</h2><table><thead><tr><th>\u00cdtem</th><th>Descripci\u00f3n</th><th>Unidad</th><th>Cantidad</th></tr></thead><tbody>${htmlRows}</tbody></table></body></html>`);
      pw.document.close(); pw.focus(); pw.print();
    }

    // ===================== WPS FUNCTIONS (CARD-BASED) =====================
    function getWpsProcess(w) { return w.proceso || w.process || w.ma_proceso || ''; }
    function getWpsSocieties(w) {
      if (Array.isArray(w.societies) && w.societies.length) return w.societies;
      if (w.society) return [w.society];
      return [];
    }
    function getSocBadgeClass(soc) {
      const upper = (soc || '').toUpperCase();
      return SOC_COLORS[upper] || 'soc-other';
    }

    function renderWpsCards() {
      const container = document.getElementById('wpsCardsContainer');
      const searchTerm = (document.getElementById('wpsSearchInput')?.value || '').toLowerCase();
      container.innerHTML = '';
      const filtered = state.wps.filter(w => {
        if (!searchTerm) return true;
        const proc = getWpsProcess(w).toLowerCase();
        const no = (w.no || '').toLowerCase();
        const mat = (w.baseMaterial || w.mb_espec || '').toLowerCase();
        const socs = getWpsSocieties(w).join(' ').toLowerCase();
        return no.includes(searchTerm) || proc.includes(searchTerm) || mat.includes(searchTerm) || socs.includes(searchTerm);
      });
      if (!filtered.length) {
        container.innerHTML = '<div class="card" style="text-align:center;padding:40px;color:var(--muted);">No hay WPS registrados</div>';
        return;
      }
      filtered.forEach(w => {
        const origIdx = state.wps.indexOf(w);
        const process = getWpsProcess(w) || '---';
        const societies = getWpsSocieties(w);
        const div = document.createElement('div');
        div.className = 'wps-card';
        div.ondblclick = () => openWpsModalView(origIdx);
        div.onclick = () => openWpsModalView(origIdx);
        let socBadgesHtml = societies.map(s => `<span class="soc-badge ${getSocBadgeClass(s)}">${s}</span>`).join('');
        if (!socBadgesHtml) socBadgesHtml = '<span class="soc-badge soc-other">---</span>';
        const canDel = canDelete('wps');
        div.innerHTML = `
          <div class="wps-process-box">${process}</div>
          <div class="wps-card-body">
            <div class="wps-card-name">${w.no || 'Sin nombre'}</div>
            <div class="wps-card-societies">${socBadgesHtml}</div>
          </div>
          ${canDel ? `<button class="wps-card-delete" onclick="event.stopPropagation();deleteWpsDirect(${origIdx})" title="Eliminar">\u2716</button>` : ''}`;
        container.appendChild(div);
      });
      updateWpsSelects();
    }

    function deleteWpsDirect(i) {
      if (!canDelete('wps')) { showToast('No tienes permiso', true); return; }
      if (!confirm('\u00bfEliminar este WPS?')) return;
      state.wps.splice(i, 1); renderWpsCards(); saveToStorage();
    }
    function updateWpsSelects() {
      const selects = [document.getElementById('projectWpsSelect'), document.getElementById('editWelderWps')];
      selects.forEach(select => {
        if (!select) return;
        const currentVal = select.value;
        select.innerHTML = '<option value="">Seleccionar WPS...</option>';
        state.wps.forEach(w => { const opt = document.createElement('option'); opt.value = w.no; opt.textContent = `${w.no} - ${getWpsProcess(w)}`; select.appendChild(opt); });
        select.value = currentVal;
      });
    }

    // ===================== WPS MODAL =====================
    const WPS_FIELDS = ['wf_no','wf_proceso','wf_mb_espec','wf_mb_grado','wf_mb_pno','wf_mb_diametro','wf_mb_espesor','wf_mb_filete','wf_pos','wf_pos_filete','wf_pos_progresion','wf_pre_temp','wf_pre_interpass','wf_ma_proceso','wf_ma_fno','wf_ma_ano','wf_ma_sf','wf_ma_aws','wf_ma_diametro','wf_ma_flux','wf_ma_nombre','wf_gas_protec','wf_gas_flujo','wf_tec_pasadas','wf_tec_angulo','wf_tec_distancia','wf_ce_corriente','wf_ce_polaridad','wf_ce_electrodo','wf_ce_transferencia','wf_normas'];
    const WPS_FIELD_MAP = {
      wf_no:'no', wf_proceso:'proceso', wf_mb_espec:'mb_espec', wf_mb_grado:'mb_grado', wf_mb_pno:'mb_pno', wf_mb_diametro:'mb_diametro', wf_mb_espesor:'mb_espesor', wf_mb_filete:'mb_filete', wf_pos:'pos', wf_pos_filete:'pos_filete', wf_pos_progresion:'pos_progresion', wf_pre_temp:'pre_temp', wf_pre_interpass:'pre_interpass', wf_ma_proceso:'ma_proceso', wf_ma_fno:'ma_fno', wf_ma_ano:'ma_ano', wf_ma_sf:'ma_sf', wf_ma_aws:'ma_aws', wf_ma_diametro:'ma_diametro', wf_ma_flux:'ma_flux', wf_ma_nombre:'ma_nombre', wf_gas_protec:'gas_protec', wf_gas_flujo:'gas_flujo', wf_tec_pasadas:'tec_pasadas', wf_tec_angulo:'tec_angulo', wf_tec_distancia:'tec_distancia', wf_ce_corriente:'ce_corriente', wf_ce_polaridad:'ce_polaridad', wf_ce_electrodo:'ce_electrodo', wf_ce_transferencia:'ce_transferencia', wf_normas:'normas'
    };

    function clearWpsForm() {
      WPS_FIELDS.forEach(id => { const el = document.getElementById(id); if (el) el.value = ''; });
      KNOWN_SOCIETIES.forEach(s => { const cb = document.getElementById('wf_soc_' + s.toLowerCase()); if (cb) cb.checked = false; });
      state.wpsModal.customSocieties = [];
      document.getElementById('wf_custom_societies').innerHTML = '';
      document.getElementById('wf_soc_custom').value = '';
    }

    function fillWpsForm(w) {
      WPS_FIELDS.forEach(id => {
        const key = WPS_FIELD_MAP[id];
        const el = document.getElementById(id);
        if (el) el.value = w[key] || '';
      });
      // Legacy compat
      if (!document.getElementById('wf_proceso').value && w.process) document.getElementById('wf_proceso').value = w.process;
      if (!document.getElementById('wf_pos').value && w.positions) document.getElementById('wf_pos').value = w.positions;
      if (!document.getElementById('wf_mb_espec').value && w.baseMaterial) document.getElementById('wf_mb_espec').value = w.baseMaterial;
      if (!document.getElementById('wf_mb_espesor').value && w.thickness) document.getElementById('wf_mb_espesor').value = w.thickness;
      if (!document.getElementById('wf_mb_diametro').value && w.diameter) document.getElementById('wf_mb_diametro').value = w.diameter;
      if (!document.getElementById('wf_ma_diametro').value && w.fillerDiameter) document.getElementById('wf_ma_diametro').value = w.fillerDiameter;
      if (!document.getElementById('wf_ma_aws').value && w.filler) document.getElementById('wf_ma_aws').value = w.filler;
      if (!document.getElementById('wf_gas_protec').value && w.gas) document.getElementById('wf_gas_protec').value = w.gas;
      if (!document.getElementById('wf_ce_polaridad').value && w.connection) document.getElementById('wf_ce_polaridad').value = w.connection;
      if (!document.getElementById('wf_ce_corriente').value && w.voltage) document.getElementById('wf_ce_corriente').value = (w.voltage||'') + (w.amperage ? '/' + w.amperage : '');

      // Societies
      KNOWN_SOCIETIES.forEach(s => { const cb = document.getElementById('wf_soc_' + s.toLowerCase()); if (cb) cb.checked = false; });
      const socs = getWpsSocieties(w);
      const customSocs = [];
      socs.forEach(s => {
        const cb = document.getElementById('wf_soc_' + s.toLowerCase());
        if (cb) cb.checked = true;
        else customSocs.push(s);
      });
      state.wpsModal.customSocieties = customSocs;
      renderCustomSocieties();

      // CE Tabs
      if (w.ce_tabs) {
        state.wpsModal.ceTabData = JSON.parse(JSON.stringify(w.ce_tabs));
      } else {
        state.wpsModal.ceTabData = { _tabs: [{ id: 'tab_1', name: 'P\u00e1gina 1' }, { id: 'tab_2', name: 'P\u00e1gina 2' }], tab_1: [], tab_2: [] };
      }
      ensureCeTabData();
      state.wpsModal.activeTab = state.wpsModal.ceTabData._tabs[0]?.id || null;
      renderCeTabsBar();
      switchWpsCeTab(state.wpsModal.activeTab);
    }

    function collectWpsForm() {
      const data = {};
      WPS_FIELDS.forEach(id => { data[WPS_FIELD_MAP[id]] = (document.getElementById(id)?.value || '').trim(); });
      data.proceso = data.proceso || data.ma_proceso || '';
      // Legacy fields for compat
      data.process = data.proceso;
      data.positions = data.pos;
      data.baseMaterial = data.mb_espec;
      data.thickness = data.mb_espesor;
      data.diameter = data.mb_diametro;
      data.filler = data.ma_aws;
      data.fillerDiameter = data.ma_diametro;
      data.gas = data.gas_protec;
      data.connection = data.ce_polaridad;
      data.voltage = ''; data.amperage = '';

      // Societies
      const socs = [];
      KNOWN_SOCIETIES.forEach(s => {
        if (document.getElementById('wf_soc_' + s.toLowerCase())?.checked) socs.push(s);
      });
      state.wpsModal.customSocieties.forEach(s => socs.push(s));
      data.societies = socs;
      data.society = socs[0] || '';

      // CE Tab data
      data.ce_tabs = state.wpsModal.ceTabData || { _tabs: [{ id: 'tab_1', name: 'P\u00e1gina 1' }, { id: 'tab_2', name: 'P\u00e1gina 2' }], tab_1: [], tab_2: [] };

      return data;
    }

    function setWpsFormReadonly(readonly) {
      WPS_FIELDS.forEach(id => {
        const el = document.getElementById(id);
        if (el) { el.readOnly = readonly; if (readonly) el.style.background = '#f8fafc'; else el.style.background = ''; }
      });
      KNOWN_SOCIETIES.forEach(s => {
        const cb = document.getElementById('wf_soc_' + s.toLowerCase());
        if (cb) cb.disabled = readonly;
      });
      document.getElementById('wf_soc_custom').disabled = readonly;
      document.querySelectorAll('#wpsCeTabContent input, #wpsCeTabContent select').forEach(el => {
        el.readOnly = readonly;
        if (readonly) el.style.background = '#f8fafc'; else el.style.background = '';
      });
    }

    function openWpsModalAdd() {
      if (!canEdit('wps')) { showToast('No tienes permiso', true); return; }
      state.wpsModal = { mode: 'add', index: null, activeTab: null, customSocieties: [],
        ceTabData: { _tabs: [{ id: 'tab_1', name: 'P\u00e1gina 1' }, { id: 'tab_2', name: 'P\u00e1gina 2' }], tab_1: [], tab_2: [] }
      };
      state.wpsModal.activeTab = 'tab_1';
      clearWpsForm();
      setWpsFormReadonly(false);
      document.getElementById('wpsModalTitle').textContent = 'Agregar WPS';
      document.getElementById('wpsModalSubtitle').textContent = 'Nuevo procedimiento de soldadura';
      document.getElementById('wpsModalSaveBtn').style.display = '';
      document.getElementById('wpsModalModifyBtn').style.display = 'none';
      document.getElementById('wpsModalDeleteBtn').style.display = 'none';
      renderCeTabsBar();
      renderWpsCeTab();
      document.getElementById('wpsModal').classList.add('show');
    }

    function openWpsModalView(index) {
      const w = state.wps[index];
      if (!w) return;
      state.wpsModal = { mode: 'view', index: index, activeTab: null, customSocieties: [], ceTabData: null };
      clearWpsForm();
      fillWpsForm(w);
      setWpsFormReadonly(true);
      document.getElementById('wpsModalTitle').textContent = w.no || 'WPS';
      document.getElementById('wpsModalSubtitle').textContent = 'Detalle del procedimiento de soldadura';
      document.getElementById('wpsModalSaveBtn').style.display = 'none';
      document.getElementById('wpsModalModifyBtn').style.display = canEdit('wps') ? '' : 'none';
      document.getElementById('wpsModalDeleteBtn').style.display = canDelete('wps') ? '' : 'none';
      renderCeTabsBar();
      renderWpsCeTab();
      document.getElementById('wpsModal').classList.add('show');
    }

    function setWpsModalEditable() {
      state.wpsModal.mode = 'edit';
      setWpsFormReadonly(false);
      document.getElementById('wpsModalTitle').textContent = 'Modificar WPS';
      document.getElementById('wpsModalSaveBtn').style.display = '';
      document.getElementById('wpsModalModifyBtn').style.display = 'none';
      renderCeTabsBar();
      renderWpsCeTab();
    }

    function saveWpsFromModal() {
      const data = collectWpsForm();
      if (!data.no) { showToast('El n\u00famero de WPS es requerido', true); return; }
      if (state.wpsModal.mode === 'add') {
        state.wps.push(data);
      } else if (state.wpsModal.mode === 'edit' && state.wpsModal.index !== null) {
        state.wps[state.wpsModal.index] = data;
      }
      closeModal('wpsModal');
      renderWpsCards();
      showSaveSuccess('WPS guardado correctamente');
      saveToStorage();
    }

    function deleteWpsFromModal() {
      if (!canDelete('wps')) return;
      if (state.wpsModal.index === null) return;
      if (!confirm('\u00bfEliminar este WPS?')) return;
      state.wps.splice(state.wpsModal.index, 1);
      closeModal('wpsModal');
      renderWpsCards();
      showSaveSuccess('WPS eliminado');
      saveToStorage();
    }

    // WPS CE Tabs (Dynamic)
    function ensureCeTabData() {
      if (!state.wpsModal.ceTabData) {
        state.wpsModal.ceTabData = { _tabs: [{ id: 'tab_1', name: 'P\u00e1gina 1' }, { id: 'tab_2', name: 'P\u00e1gina 2' }], tab_1: [], tab_2: [] };
      }
      // Migration: convert old format to new
      if (!state.wpsModal.ceTabData._tabs) {
        const oldData = state.wpsModal.ceTabData;
        const newData = { _tabs: [] };
        Object.keys(oldData).forEach((key, idx) => {
          if (key === '_tabs') return;
          const tabId = 'tab_' + (idx + 1);
          newData._tabs.push({ id: tabId, name: key });
          newData[tabId] = oldData[key] || [];
        });
        if (!newData._tabs.length) {
          newData._tabs = [{ id: 'tab_1', name: 'P\u00e1gina 1' }, { id: 'tab_2', name: 'P\u00e1gina 2' }];
          newData.tab_1 = []; newData.tab_2 = [];
        }
        state.wpsModal.ceTabData = newData;
      }
      if (!state.wpsModal.activeTab && state.wpsModal.ceTabData._tabs.length) {
        state.wpsModal.activeTab = state.wpsModal.ceTabData._tabs[0].id;
      }
    }

    function renderCeTabsBar() {
      ensureCeTabData();
      const container = document.getElementById('wpsCeTabs');
      const readonly = state.wpsModal.mode === 'view';
      const tabs = state.wpsModal.ceTabData._tabs || [];
      let html = '';
      tabs.forEach(t => {
        const isActive = state.wpsModal.activeTab === t.id;
        if (readonly) {
          html += `<button class="wps-tab-btn ${isActive ? 'active' : ''}" onclick="switchWpsCeTab('${t.id}')">${t.name}</button>`;
        } else {
          html += `<div class="wps-tab-btn ${isActive ? 'active' : ''}" onclick="switchWpsCeTab('${t.id}')">
            <input class="wps-tab-name-input" value="${t.name}" onclick="event.stopPropagation()" onchange="renameCeTab('${t.id}', this.value)" style="width:${Math.max(30, t.name.length * 8)}px;color:inherit;" />
            ${tabs.length > 1 ? `<button class="wps-tab-delete" onclick="event.stopPropagation();deleteCeTab('${t.id}')" title="Eliminar p\u00e1gina">\u2716</button>` : ''}
          </div>`;
        }
      });
      if (!readonly) {
        html += `<button class="wps-add-tab-btn" onclick="addNewCeTab()" title="Agregar nueva p\u00e1gina">+</button>`;
      }
      container.innerHTML = html;
    }

    function switchWpsCeTab(tabId) {
      state.wpsModal.activeTab = tabId;
      renderCeTabsBar();
      renderWpsCeTab();
    }

    function addNewCeTab() {
      ensureCeTabData();
      const num = state.wpsModal.ceTabData._tabs.length + 1;
      const id = 'tab_' + Date.now();
      state.wpsModal.ceTabData._tabs.push({ id, name: 'P\u00e1gina ' + num });
      state.wpsModal.ceTabData[id] = [];
      state.wpsModal.activeTab = id;
      renderCeTabsBar();
      renderWpsCeTab();
    }

    function deleteCeTab(tabId) {
      ensureCeTabData();
      if (state.wpsModal.ceTabData._tabs.length <= 1) return;
      state.wpsModal.ceTabData._tabs = state.wpsModal.ceTabData._tabs.filter(t => t.id !== tabId);
      delete state.wpsModal.ceTabData[tabId];
      if (state.wpsModal.activeTab === tabId) {
        state.wpsModal.activeTab = state.wpsModal.ceTabData._tabs[0]?.id || null;
      }
      renderCeTabsBar();
      renderWpsCeTab();
    }

    function renameCeTab(tabId, newName) {
      ensureCeTabData();
      const tab = state.wpsModal.ceTabData._tabs.find(t => t.id === tabId);
      if (tab) tab.name = newName.trim() || tab.name;
    }

    function renderWpsCeTab() {
      ensureCeTabData();
      const tabId = state.wpsModal.activeTab;
      const container = document.getElementById('wpsCeTabContent');
      if (!tabId) { container.innerHTML = '<div class="small" style="padding:20px;text-align:center;">Seleccione una p\u00e1gina</div>'; return; }
      const rows = state.wpsModal.ceTabData[tabId] || [];
      const readonly = state.wpsModal.mode === 'view';
      const tabInfo = state.wpsModal.ceTabData._tabs.find(t => t.id === tabId);
      const tabName = tabInfo ? tabInfo.name : tabId;
      let html = '<div class="table-shell" style="overflow-x:auto;margin-bottom:8px;"><table><thead><tr><th style="text-align:center;min-width:120px;">Paso</th><th style="text-align:center;min-width:100px;">Proceso</th><th style="text-align:center;min-width:100px;">Di\u00e1metro</th><th style="text-align:center;min-width:110px;">Amper.</th><th style="text-align:center;min-width:100px;">Voltaje</th><th style="text-align:center;min-width:120px;">Veloc. de Ava.</th>';
      if (!readonly) html += '<th style="text-align:center;width:50px;">Acc.</th>';
      html += '</tr></thead><tbody>';
      if (!rows.length) {
        html += `<tr><td colspan="${readonly ? 6 : 7}" style="text-align:center;color:var(--muted);padding:20px;">Sin datos para <strong>${tabName}</strong></td></tr>`;
      }
      rows.forEach((row, i) => {
        const ro = readonly ? 'readonly style="background:#f8fafc;text-align:center;font-size:13px;padding:10px 8px;"' : 'style="text-align:center;font-size:13px;padding:10px 8px;"';
        html += `<tr>
          <td><input value="${row.paso||''}" onchange="updateCeRow('${tabId}',${i},'paso',this.value)" ${ro} /></td>
          <td><input value="${row.proceso||''}" onchange="updateCeRow('${tabId}',${i},'proceso',this.value)" ${ro} /></td>
          <td><input value="${row.diametro||''}" onchange="updateCeRow('${tabId}',${i},'diametro',this.value)" ${ro} /></td>
          <td><input value="${row.amper||''}" onchange="updateCeRow('${tabId}',${i},'amper',this.value)" ${ro} /></td>
          <td><input value="${row.voltaje||''}" onchange="updateCeRow('${tabId}',${i},'voltaje',this.value)" ${ro} /></td>
          <td><input value="${row.velocidad||''}" onchange="updateCeRow('${tabId}',${i},'velocidad',this.value)" ${ro} /></td>
          ${!readonly ? `<td style="text-align:center;"><button class="btn btn-sm btn-danger" onclick="deleteCeRow('${tabId}',${i})">\u2716</button></td>` : ''}
        </tr>`;
      });
      html += '</tbody></table></div>';
      if (!readonly) html += `<button class="btn btn-sm btn-secondary" onclick="addCeRow('${tabId}')" style="margin-top:4px;">+ Agregar fila</button>`;
      container.innerHTML = html;
    }

    function addCeRow(tab) {
      if (!state.wpsModal.ceTabData[tab]) state.wpsModal.ceTabData[tab] = [];
      state.wpsModal.ceTabData[tab].push({ paso: '', proceso: '', diametro: '', amper: '', voltaje: '', velocidad: '' });
      renderWpsCeTab();
    }
    function deleteCeRow(tab, i) {
      state.wpsModal.ceTabData[tab].splice(i, 1);
      renderWpsCeTab();
    }
    function updateCeRow(tab, i, field, val) {
      if (state.wpsModal.ceTabData[tab] && state.wpsModal.ceTabData[tab][i]) {
        state.wpsModal.ceTabData[tab][i][field] = val;
      }
    }

    // Custom societies
    function addCustomSociety() {
      const val = document.getElementById('wf_soc_custom').value.trim().toUpperCase();
      if (!val) return;
      if (KNOWN_SOCIETIES.includes(val)) {
        const cb = document.getElementById('wf_soc_' + val.toLowerCase());
        if (cb) cb.checked = true;
      } else if (!state.wpsModal.customSocieties.includes(val)) {
        state.wpsModal.customSocieties.push(val);
      }
      document.getElementById('wf_soc_custom').value = '';
      renderCustomSocieties();
    }
    function removeCustomSociety(soc) {
      state.wpsModal.customSocieties = state.wpsModal.customSocieties.filter(s => s !== soc);
      renderCustomSocieties();
    }
    function renderCustomSocieties() {
      const container = document.getElementById('wf_custom_societies');
      container.innerHTML = state.wpsModal.customSocieties.map(s => `<span class="soc-badge soc-other" style="cursor:pointer;" onclick="removeCustomSociety('${s}')">${s} \u00d7</span>`).join('');
    }

    // ===================== PROJECT FUNCTIONS =====================
    function renderProjects() {
      const list = document.getElementById('projectList'); list.innerHTML = '';
      if (!state.projects.length) { list.innerHTML = '<div class="small" style="padding:10px;">No hay proyectos</div>'; return; }
      state.projects.forEach((p, i) => {
        const div = document.createElement('div');
        div.className = `proj-item ${state.activeProject === i ? 'active' : ''}`;
        div.innerHTML = `
          <div class="proj-info" onclick="selectProject(${i})">
            <strong>${p.name}</strong>
            <span class="small">${p.client || 'Sin cliente'} \u00b7 ${p.welders.length} soldadores</span>
          </div>
          ${canDelete('calificacion') ? `<button class="proj-delete-btn" onclick="event.stopPropagation();deleteProject(${i})" title="Eliminar proyecto">\u2716</button>` : ''}`;
        list.appendChild(div);
      });
    }
    function selectProject(index) { state.activeProject = index; renderProjects(); renderActiveProject(); }
    function deleteProject(index) {
      if (!canDelete('calificacion')) { showToast('No tienes permiso', true); return; }
      const p = state.projects[index];
      if (!confirm(`\u00bfEliminar el proyecto "${p.name}"? Se perder\u00e1n todos los soldadores y datos asociados.`)) return;
      state.projects.splice(index, 1);
      if (state.activeProject === index) state.activeProject = null;
      else if (state.activeProject !== null && state.activeProject > index) state.activeProject--;
      renderProjects(); renderActiveProject(); saveToStorage();
      showSaveSuccess('Proyecto eliminado');
    }
    function renderActiveProject() {
      const formCard = document.getElementById('projectFormCard');
      const addCard = document.getElementById('addWelderCard');
      const tableCard = document.getElementById('projectTableCard');
      if (state.activeProject === null) { formCard.style.display = 'none'; addCard.style.display = 'none'; tableCard.style.display = 'none'; return; }
      formCard.style.display = 'block'; addCard.style.display = canEdit('calificacion') ? 'block' : 'none'; tableCard.style.display = 'block';
      const p = state.projects[state.activeProject];
      document.getElementById('activeProjectTitle').textContent = `Proyecto: ${p.name}`;
      document.getElementById('projectWpsSelect').value = p.wps || '';
      document.getElementById('procDate').value = p.date || '';
      renderProjectWeldersTable();
    }
    function renderProjectWeldersTable() {
      const tbody = document.getElementById('projectWeldersTable');
      tbody.innerHTML = '';
      if (state.activeProject === null) return;
      const p = state.projects[state.activeProject];
      if (!p.welders.length) { tbody.innerHTML = '<tr><td colspan="8" style="text-align:center;padding:20px;color:#64748b;">Sin soldadores asignados</td></tr>'; return; }
      const editable = canEdit('calificacion');
      p.welders.forEach((w, i) => {
        const inspSt = getInspStatus(w);
        const doblezSt = getDoblezStatus(w);
        const certSt = getCertStatus(w);
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:700;">${w.id}</td>
          <td>${w.name}</td>
          <td><span style="font-weight:600;color:var(--accent-dark);">${w.wps || p.wps || '\u2014'}</span></td>
          <td><strong>${w.pos}</strong></td>
          <td><div class="action-cell"><button class="btn btn-sm btn-secondary" onclick="openInspeccionModal(${i})">Ver</button><span class="status-micro ${inspSt.cls}">${inspSt.label}</span></div></td>
          <td><div class="action-cell"><button class="btn btn-sm btn-secondary" onclick="openDoblezModal(${i})">Ver</button><span class="status-micro ${doblezSt.cls}">${doblezSt.label}</span></div></td>
          <td><div class="action-cell"><button class="btn btn-sm btn-secondary" onclick="openCertificadoModal(${i})">Ver</button><span class="status-micro ${certSt.cls}">${certSt.label}</span></div></td>
          <td>${editable ? `<div style="display:flex;gap:4px;"><button class="btn btn-sm btn-warn" onclick="openEditProjectWelderModal(${i})">Modificar</button><button class="btn btn-sm btn-danger" onclick="deleteProjectWelder(${i})">Eliminar</button></div>` : ''}</td>`;
        tbody.appendChild(tr);
      });
    }
    function addProject() {
      if (!canEdit('calificacion')) { showToast('No tienes permiso', true); return; }
      const name = document.getElementById('projectName').value.trim();
      const client = document.getElementById('projectClient').value.trim();
      if (!name) return;
      state.projects.push({ name, client, wps: '', date: '', welders: [] });
      state.activeProject = state.projects.length - 1;
      document.getElementById('projectName').value = ''; document.getElementById('projectClient').value = '';
      renderProjects(); renderActiveProject(); saveToStorage();
    }
    function updateProjectWps() { if (state.activeProject === null) return; state.projects[state.activeProject].wps = document.getElementById('projectWpsSelect').value; }
    function saveProjectMeta() {
      if (state.activeProject === null) return;
      const p = state.projects[state.activeProject];
      p.wps = document.getElementById('projectWpsSelect').value;
      p.date = document.getElementById('procDate').value;
      showSaveSuccess('Informaci\u00f3n del proyecto guardada');
      saveToStorage();
    }

    // ===================== WELDER SEARCH =====================
    function searchWelders() {
      const term = document.getElementById('welderSearchInput').value.toLowerCase();
      const resultsDiv = document.getElementById('welderSearchResults');
      if (!term) { resultsDiv.classList.remove('show'); return; }
      const filtered = state.masterWelders.filter(w => w.id.toLowerCase().includes(term) || w.name.toLowerCase().includes(term));
      resultsDiv.innerHTML = '';
      if (!filtered.length) { resultsDiv.innerHTML = '<div class="search-result-item small">No se encontraron soldadores</div>'; }
      else { filtered.forEach(w => { const div = document.createElement('div'); div.className = 'search-result-item'; div.innerHTML = `<strong>${w.id}</strong> - ${w.name}`; div.onclick = () => selectWelderForProject(w); resultsDiv.appendChild(div); }); }
      resultsDiv.classList.add('show');
    }
    function showWelderResults() { const term = document.getElementById('welderSearchInput').value; if (term) searchWelders(); }
    function selectWelderForProject(welder) {
      document.getElementById('welderSearchInput').value = welder.id;
      document.getElementById('welderNameDisplay').value = welder.name;
      document.getElementById('welderSearchResults').classList.remove('show');
    }
    function addProjectWelder() {
      if (state.activeProject === null) { alert('Seleccione un proyecto primero'); return; }
      const id = document.getElementById('welderSearchInput').value.trim();
      const name = document.getElementById('welderNameDisplay').value.trim();
      const pos = document.getElementById('welderPos').value.trim();
      const plateThickness = document.getElementById('welderPlateThickness').value.trim();
      const pipeDiameter = document.getElementById('welderPipeDiameter').value.trim();
      const classInspector = document.getElementById('classInspector').value.trim();
      const qcInspector = document.getElementById('qcInspector').value.trim();
      const wpq = document.getElementById('wpqNo').value.trim();
      if (!id || !name) { alert('Matr\u00edcula y nombre son requeridos'); return; }
      const p = state.projects[state.activeProject];
      p.welders.push({ id, name, pos, plateThickness, pipeDiameter, classInspector, qcInspector, wpq, wps: p.wps, inspeccion: { rows: [], result: '' }, doblez: { rows: [], result: '', photo: '' }, certificado: {} });
      ['welderSearchInput','welderNameDisplay','welderPos','welderPlateThickness','welderPipeDiameter','classInspector','qcInspector','wpqNo'].forEach(id => document.getElementById(id).value = '');
      if (!state.masterWelders.find(w => w.id === id)) { state.masterWelders.push({ id, name, status: 'activo', certs: [], photo: '', selected: false }); renderMasterWelders(); }
      renderProjectWeldersTable(); saveToStorage();
    }
    function deleteProjectWelder(index) {
      if (!confirm('\u00bfEliminar este soldador del proyecto?')) return;
      state.projects[state.activeProject].welders.splice(index, 1);
      renderProjectWeldersTable(); saveToStorage();
    }

    // ===================== EDIT PROJECT WELDER MODAL =====================
    function openEditProjectWelderModal(index) {
      if (state.activeProject === null) return;
      state.editingWelderIndex = index;
      const w = state.projects[state.activeProject].welders[index];
      document.getElementById('editWelderId').value = w.id;
      document.getElementById('editWelderName').value = w.name;
      document.getElementById('editWelderWps').value = w.wps || state.projects[state.activeProject].wps || '';
      document.getElementById('editWelderPos').value = w.pos || '';
      document.getElementById('editWelderPlateThickness').value = w.plateThickness || '';
      document.getElementById('editWelderPipeDiameter').value = w.pipeDiameter || '';
      document.getElementById('editClassInspector').value = w.classInspector || '';
      document.getElementById('editQcInspector').value = w.qcInspector || '';
      document.getElementById('editWpqNo').value = w.wpq || '';
      document.getElementById('editWelderInfo').textContent = `${w.id} - ${w.name}`;
      document.getElementById('editProjectWelderModal').classList.add('show');
    }
    function saveEditedProjectWelder() {
      if (state.activeProject === null || state.editingWelderIndex === null) return;
      const w = state.projects[state.activeProject].welders[state.editingWelderIndex];
      w.wps = document.getElementById('editWelderWps').value;
      w.pos = document.getElementById('editWelderPos').value;
      w.plateThickness = document.getElementById('editWelderPlateThickness').value;
      w.pipeDiameter = document.getElementById('editWelderPipeDiameter').value;
      w.classInspector = document.getElementById('editClassInspector').value;
      w.qcInspector = document.getElementById('editQcInspector').value;
      w.wpq = document.getElementById('editWpqNo').value;
      closeModal('editProjectWelderModal');
      state.editingWelderIndex = null;
      renderProjectWeldersTable();
      showSaveSuccess('Datos del soldador actualizados');
      saveToStorage();
    }

    // ===================== INSPECTION MODAL =====================
    let currentInspeccionWelderIndex = null;
    function openInspeccionModal(index) {
      currentInspeccionWelderIndex = index;
      const w = state.projects[state.activeProject].welders[index];
      document.getElementById('inspeccionWelderInfo').textContent = `${w.id} - ${w.name}`;
      renderInspeccionTable();
      document.getElementById('inspeccionModal').classList.add('show');
    }
    function renderInspeccionTable() {
      const tbody = document.getElementById('inspeccionTableBody'); tbody.innerHTML = '';
      const w = state.projects[state.activeProject].welders[currentInspeccionWelderIndex];
      if (!w.inspeccion) w.inspeccion = { rows: [], result: '' };
      if (!w.inspeccion.rows.length) w.inspeccion.rows.push({ pos: w.pos || '3G', raiz: '', vista: '' });
      w.inspeccion.rows.forEach((row, i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><input value="${row.pos}" onchange="updateInspeccionRow(${i},'pos',this.value)" style="width:80px;" /></td>
          <td><label><input type="radio" name="raiz${i}" value="ok" ${row.raiz==='ok'?'checked':''} onchange="updateInspeccionRow(${i},'raiz','ok')"> OK</label> <label><input type="radio" name="raiz${i}" value="r" ${row.raiz==='r'?'checked':''} onchange="updateInspeccionRow(${i},'raiz','r')"> R</label></td>
          <td><label><input type="radio" name="vista${i}" value="ok" ${row.vista==='ok'?'checked':''} onchange="updateInspeccionRow(${i},'vista','ok')"> OK</label> <label><input type="radio" name="vista${i}" value="r" ${row.vista==='r'?'checked':''} onchange="updateInspeccionRow(${i},'vista','r')"> R</label></td>`;
        tbody.appendChild(tr);
      });
    }
    function updateInspeccionRow(index, field, value) { state.projects[state.activeProject].welders[currentInspeccionWelderIndex].inspeccion.rows[index][field] = value; }
    function addInspeccionRow() { state.projects[state.activeProject].welders[currentInspeccionWelderIndex].inspeccion.rows.push({ pos: '', raiz: '', vista: '' }); renderInspeccionTable(); }
    function saveInspeccion() { renderProjectWeldersTable(); showSaveSuccess('Inspecci\u00f3n visual guardada'); closeModal('inspeccionModal'); saveToStorage(); }

    // ===================== DOBLEZ MODAL =====================
    let currentDoblezWelderIndex = null;
    function openDoblezModal(index) {
      currentDoblezWelderIndex = index;
      const w = state.projects[state.activeProject].welders[index];
      const p = state.projects[state.activeProject];
      const wpsData = state.wps.find(x => x.no === (w.wps || p.wps)) || {};
      initDoblezData(w, p, wpsData);
      document.getElementById('doblezWelderInfo').textContent = `${w.id} - ${w.name}`;
      document.getElementById('doblezWelderName').value = w.name;
      document.getElementById('doblezWelderId').value = w.id;
      document.getElementById('doblezWps').value = w.wps || p.wps || '';
      document.getElementById('doblezWpq').value = w.wpq || '';
      document.getElementById('doblezPositions').value = w.pos || '';
      document.getElementById('doblezProcManual').checked = w.doblez.procManual;
      document.getElementById('doblezProcSemi').checked = w.doblez.procSemi;
      document.getElementById('doblezProcMech').checked = w.doblez.procMech;
      document.getElementById('doblezReportDate').value = w.doblez.reportDate;
      document.getElementById('doblezReportNo').value = w.doblez.reportNo;
      document.getElementById('doblezMaterialSpec').value = w.doblez.materialSpec;
      document.getElementById('doblezThickness').value = w.doblez.thickness;
      document.getElementById('doblezDiameter').value = w.doblez.diameter;
      document.getElementById('doblezDescription').value = w.doblez.description;
      document.getElementById('doblezBendMethod').value = w.doblez.bendMethod;
      document.getElementById('doblezStandard').value = w.doblez.standard;
      document.getElementById('doblezRemarks').value = w.doblez.remarks;
      document.getElementById('doblezResultadoFinal').value = w.doblez.result || '';
      updateDoblezResultColor();
      document.getElementById('doblezTestDate').value = w.doblez.testDate;
      document.getElementById('doblezPerformedBy').value = w.doblez.performedBy;
      document.getElementById('doblezApprovedBy').value = w.doblez.approvedBy;
      if (w.doblez.photo) { document.getElementById('doblezPhotoBox').innerHTML = `<img src="${w.doblez.photo}" />`; }
      else { document.getElementById('doblezPhotoBox').innerHTML = 'Sin foto'; }
      renderDoblezTable();
      document.getElementById('doblezModal').classList.add('show');
    }
    function renderDoblezTable() {
      const tbody = document.getElementById('doblezTableBody'); tbody.innerHTML = '';
      const w = state.projects[state.activeProject].welders[currentDoblezWelderIndex];
      if (!w.doblez.rows.length) { w.doblez.rows.push({ tipo: 'Side Bend', pos: '3G', resultado: '' }); w.doblez.rows.push({ tipo: 'Side Bend', pos: '4G', resultado: '' }); }
      w.doblez.rows.forEach((row, i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><select onchange="updateDoblezRow(${i},'tipo',this.value)" style="min-width:120px;">
            <option value="Side Bend" ${row.tipo==='Side Bend'?'selected':''}>Side Bend</option>
            <option value="Root Bend" ${row.tipo==='Root Bend'?'selected':''}>Root Bend</option>
            <option value="Face Bend" ${row.tipo==='Face Bend'?'selected':''}>Face Bend</option>
          </select></td>
          <td><input value="${row.pos}" onchange="updateDoblezRow(${i},'pos',this.value)" style="width:70px;" /></td>
          <td><select onchange="updateDoblezRow(${i},'resultado',this.value)">
            <option value="">\u2014</option>
            <option value="good" ${row.resultado==='good'?'selected':''}>Good</option>
            <option value="reject" ${row.resultado==='reject'?'selected':''}>Reject</option>
          </select></td>
          <td><button class="btn btn-sm btn-danger" onclick="deleteDoblezRow(${i})">\u2716</button></td>`;
        tbody.appendChild(tr);
      });
    }
    function updateDoblezRow(index, field, value) { state.projects[state.activeProject].welders[currentDoblezWelderIndex].doblez.rows[index][field] = value; }
    function addDoblezRow() { state.projects[state.activeProject].welders[currentDoblezWelderIndex].doblez.rows.push({ tipo: 'Side Bend', pos: '', resultado: '' }); renderDoblezTable(); }
    function deleteDoblezRow(index) { state.projects[state.activeProject].welders[currentDoblezWelderIndex].doblez.rows.splice(index, 1); renderDoblezTable(); }
    function updateDoblezResultColor() {
      const select = document.getElementById('doblezResultadoFinal');
      select.classList.remove('result-approved','result-rejected');
      if (select.value === 'aprobado') select.classList.add('result-approved');
      if (select.value === 'reprobado') select.classList.add('result-rejected');
      if (currentDoblezWelderIndex !== null && state.activeProject !== null) {
        state.projects[state.activeProject].welders[currentDoblezWelderIndex].doblez.result = select.value;
      }
    }
    function loadDoblezPhoto(event) {
      const file = event.target.files[0]; if (!file || currentDoblezWelderIndex === null) return;
      const reader = new FileReader();
      reader.onload = e => { state.projects[state.activeProject].welders[currentDoblezWelderIndex].doblez.photo = e.target.result; document.getElementById('doblezPhotoBox').innerHTML = `<img src="${e.target.result}" />`; };
      reader.readAsDataURL(file);
    }
    function saveDoblez() {
      if (currentDoblezWelderIndex === null || state.activeProject === null) return;
      const w = state.projects[state.activeProject].welders[currentDoblezWelderIndex];
      w.doblez.reportDate = document.getElementById('doblezReportDate').value;
      w.doblez.reportNo = document.getElementById('doblezReportNo').value;
      w.doblez.procManual = document.getElementById('doblezProcManual').checked;
      w.doblez.procSemi = document.getElementById('doblezProcSemi').checked;
      w.doblez.procMech = document.getElementById('doblezProcMech').checked;
      w.doblez.materialSpec = document.getElementById('doblezMaterialSpec').value;
      w.doblez.thickness = document.getElementById('doblezThickness').value;
      w.doblez.diameter = document.getElementById('doblezDiameter').value;
      w.doblez.description = document.getElementById('doblezDescription').value;
      w.doblez.bendMethod = document.getElementById('doblezBendMethod').value;
      w.doblez.standard = document.getElementById('doblezStandard').value;
      w.doblez.remarks = document.getElementById('doblezRemarks').value;
      w.doblez.testDate = document.getElementById('doblezTestDate').value;
      w.doblez.performedBy = document.getElementById('doblezPerformedBy').value;
      w.doblez.approvedBy = document.getElementById('doblezApprovedBy').value;
      renderProjectWeldersTable();
      showSaveSuccess('Prueba de Doblez guardada');
      saveToStorage();
    }
    function printDoblezFormat() {
      const w = state.projects[state.activeProject].welders[currentDoblezWelderIndex];
      const p = state.projects[state.activeProject];
      const d = w.doblez || {};
      const procText = [(d.procManual?'&#9746; Manual':'&#9744; Manual'),(d.procSemi?'&#9746; Semiautom\u00e1tico':'&#9744; Semiautom\u00e1tico'),(d.procMech?'&#9746; Mecanizado':'&#9744; Mecanizado')].join(' &nbsp;&nbsp; ');
      const htmlRows = (d.rows||[]).map(r => `<tr><td>${r.tipo}</td><td>${r.pos}</td><td style="font-weight:bold;color:${r.resultado==='good'?'#059669':(r.resultado==='reject'?'#dc2626':'#64748b')}">${r.resultado==='good'?'Good':(r.resultado==='reject'?'Reject':'\u2014')}</td></tr>`).join('');
      const finalResult = d.result === 'aprobado' ? 'APROBADO' : (d.result === 'reprobado' ? 'REPROBADO' : 'PENDIENTE');
      const resultColor = d.result === 'aprobado' ? '#059669' : (d.result === 'reprobado' ? '#dc2626' : '#94a3b8');
      const pw = window.open('', '_blank');
      pw.document.write(`<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Guided Bend Test - ${w.name}</title><style>*{box-sizing:border-box}body{font-family:Arial,sans-serif;padding:20px;color:#1B365D;font-size:11px;margin:0}.doc-header{display:flex;border:2px solid #1B365D;margin-bottom:0}.logo-box{padding:8px 12px;border-right:2px solid #1B365D;display:flex;align-items:center;justify-content:center;min-width:130px}.logo-box img{max-width:110px;max-height:70px}.title-box{flex:1;padding:8px;text-align:center;border-right:2px solid #1B365D}.co-name{font-size:9px;font-weight:bold;text-transform:uppercase}.doc-title{font-size:16px;font-weight:800;text-transform:uppercase;letter-spacing:1px;margin:2px 0}.id-box{padding:8px;font-size:9px;min-width:160px}.id-box div{margin-bottom:3px}.sec-head{background:#1B365D;color:#fff;padding:5px 10px;font-weight:800;font-size:10px;text-transform:uppercase}.sec-body{border:1px solid #1B365D;border-top:none;padding:8px}.ft{width:100%;border-collapse:collapse}.ft th,.ft td{border:1px solid #1B365D;padding:5px 8px;font-size:10px;text-align:left}.ft th{background:#e8eef5;font-weight:bold}.result-box{border:3px solid ${resultColor};padding:14px;text-align:center;font-size:22px;font-weight:800;color:${resultColor};letter-spacing:3px;margin:12px 0;border-radius:6px}@media print{@page{margin:12mm}}</style></head><body>
      <div class="doc-header"><div class="logo-box"><img src="${LOGO_URL}"></div><div class="title-box"><div class="co-name">TALLERES NAVALES DEL GOLFO S.A. DE C.V.</div><div class="doc-title">GUIDED BEND TEST REPORT</div></div><div class="id-box"><div><strong>REPORT:</strong> ${d.reportNo||'___'}</div><div><strong>FECHA:</strong> ${d.reportDate||new Date().toLocaleDateString()}</div></div></div>
      <div class="sec-head">Soldador</div><div class="sec-body"><table class="ft"><tr><th>Nombre</th><td>${w.name}</td><th>ID</th><td>${w.id}</td></tr><tr><th>Proceso</th><td colspan="3">${procText}</td></tr><tr><th>WPS</th><td>${w.wps||p.wps||'\u2014'}</td><th>Posici\u00f3n</th><td>${w.pos||'\u2014'}</td></tr></table></div>
      <div class="sec-head">Resultados</div><div class="sec-body"><table class="ft"><thead><tr><th>Tipo</th><th>Posici\u00f3n</th><th>Resultado</th></tr></thead><tbody>${htmlRows||'<tr><td colspan="3">Sin datos</td></tr>'}</tbody></table></div>
      <div class="result-box">${finalResult}</div>
      </body></html>`);
      pw.document.close(); pw.focus(); pw.print();
    }

    // ===================== CERTIFICADO MODAL =====================
    let currentCertificadoWelderIndex = null;
    function openCertificadoModal(index) {
      currentCertificadoWelderIndex = index;
      const w = state.projects[state.activeProject].welders[index];
      const p = state.projects[state.activeProject];
      const wpsData = state.wps.find(x => x.no === (w.wps || p.wps)) || {};
      initCertData(w, p, wpsData);
      document.getElementById('certificadoWelderInfo').textContent = `${w.id} - ${w.name}`;
      document.getElementById('certVessel').value = w.certificado.vessel;
      document.getElementById('certShipyard').value = w.certificado.shipyard || p.client || '';
      document.getElementById('certHullNo').value = w.certificado.hullNo;
      document.getElementById('certReportNo').value = w.certificado.reportNo;
      document.getElementById('certAbsId').value = w.certificado.absId;
      document.getElementById('certDate').value = w.certificado.date;
      document.getElementById('certPort').value = w.certificado.port;
      document.getElementById('certWelderName').value = w.name;
      document.getElementById('certWelderId').value = w.id;
      document.getElementById('certProcManual').checked = w.certificado.procManual;
      document.getElementById('certProcSemi').checked = w.certificado.procSemi;
      document.getElementById('certProcMachine').checked = w.certificado.procMachine;
      document.getElementById('certPosition').value = w.pos || '';
      document.getElementById('certWps').value = w.wps || p.wps || '';
      document.getElementById('certMaterialSpec').value = w.certificado.materialSpec;
      document.getElementById('certThicknessOrDia').value = w.certificado.thicknessOrDia;
      document.getElementById('certThicknessRange').value = w.certificado.thicknessRange;
      document.getElementById('certFillerSpec').value = w.certificado.fillerSpec;
      document.getElementById('certFillerClass').value = w.certificado.fillerClass;
      document.getElementById('certFillerNo').value = w.certificado.fillerNo;
      document.getElementById('certFillerDesc').value = w.certificado.fillerDesc;
      document.getElementById('certBackingStrip').value = w.certificado.backingStrip;
      document.getElementById('certFillerDia').value = w.certificado.fillerDia;
      document.getElementById('certFlux').value = w.certificado.flux;
      document.getElementById('certVisualAppearance').value = w.certificado.visualAppearance;
      document.getElementById('certUndercut').value = w.certificado.undercut;
      document.getElementById('certPipingPorosity').value = w.certificado.pipingPorosity;
      document.getElementById('certWitnessedBy').value = w.certificado.witnessedBy;
      document.getElementById('certContractor').value = w.certificado.contractor;
      document.getElementById('certSurveyorName').value = w.certificado.surveyorName;
      document.getElementById('certSignDate').value = w.certificado.signDate;
      renderCertBendTable(); renderCertRadioTable();
      document.getElementById('certificadoModal').classList.add('show');
    }
    function renderCertBendTable() {
      if (currentCertificadoWelderIndex === null) return;
      const w = state.projects[state.activeProject].welders[currentCertificadoWelderIndex];
      const tbody = document.getElementById('certBendTableBody'); tbody.innerHTML = '';
      w.certificado.bendRows.forEach((row, i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td><input value="${row.spec}" onchange="updateCertBendRow(${i},'spec',this.value)" style="min-width:130px;" /></td><td><input value="${row.figure}" onchange="updateCertBendRow(${i},'figure',this.value)" style="width:80px;" /></td><td><input value="${row.side}" onchange="updateCertBendRow(${i},'side',this.value)" style="width:60px;" /></td><td><input value="${row.sample}" onchange="updateCertBendRow(${i},'sample',this.value)" style="width:60px;" /></td><td><select onchange="updateCertBendRow(${i},'result',this.value)"><option value="">\u2014</option><option value="Good" ${row.result==='Good'?'selected':''}>Good</option><option value="Reject" ${row.result==='Reject'?'selected':''}>Reject</option></select></td>`;
        tbody.appendChild(tr);
      });
    }
    function updateCertBendRow(index, field, value) { state.projects[state.activeProject].welders[currentCertificadoWelderIndex].certificado.bendRows[index][field] = value; }
    function addCertBendRow() { state.projects[state.activeProject].welders[currentCertificadoWelderIndex].certificado.bendRows.push({ spec: 'A.W.S. D1.1:2020', figure: 'Fig. 6.11', side: '', sample: '', result: '' }); renderCertBendTable(); }
    function renderCertRadioTable() {
      if (currentCertificadoWelderIndex === null) return;
      const w = state.projects[state.activeProject].welders[currentCertificadoWelderIndex];
      const tbody = document.getElementById('certRadioTableBody'); tbody.innerHTML = '';
      w.certificado.radioRows.forEach((row, i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td><input value="${row.filmId}" onchange="updateCertRadioRow(${i},'filmId',this.value)" /></td><td><input value="${row.results}" onchange="updateCertRadioRow(${i},'results',this.value)" /></td><td><input value="${row.remarks}" onchange="updateCertRadioRow(${i},'remarks',this.value)" /></td><td><button class="btn btn-sm btn-danger" onclick="deleteCertRadioRow(${i})">\u2716</button></td>`;
        tbody.appendChild(tr);
      });
    }
    function updateCertRadioRow(index, field, value) { state.projects[state.activeProject].welders[currentCertificadoWelderIndex].certificado.radioRows[index][field] = value; }
    function addCertRadioRow() { state.projects[state.activeProject].welders[currentCertificadoWelderIndex].certificado.radioRows.push({ filmId: '', results: '', remarks: '' }); renderCertRadioTable(); }
    function deleteCertRadioRow(index) { state.projects[state.activeProject].welders[currentCertificadoWelderIndex].certificado.radioRows.splice(index, 1); renderCertRadioTable(); }

    function saveCertificado() {
      if (currentCertificadoWelderIndex === null || state.activeProject === null) return;
      const w = state.projects[state.activeProject].welders[currentCertificadoWelderIndex];
      const c = w.certificado;
      c.vessel = document.getElementById('certVessel').value; c.hullNo = document.getElementById('certHullNo').value;
      c.absId = document.getElementById('certAbsId').value; c.date = document.getElementById('certDate').value;
      c.port = document.getElementById('certPort').value;
      c.procManual = document.getElementById('certProcManual').checked;
      c.procSemi = document.getElementById('certProcSemi').checked;
      c.procMachine = document.getElementById('certProcMachine').checked;
      c.materialSpec = document.getElementById('certMaterialSpec').value;
      c.thicknessOrDia = document.getElementById('certThicknessOrDia').value;
      c.thicknessRange = document.getElementById('certThicknessRange').value;
      c.fillerSpec = document.getElementById('certFillerSpec').value;
      c.fillerClass = document.getElementById('certFillerClass').value;
      c.fillerNo = document.getElementById('certFillerNo').value;
      c.fillerDesc = document.getElementById('certFillerDesc').value;
      c.backingStrip = document.getElementById('certBackingStrip').value;
      c.fillerDia = document.getElementById('certFillerDia').value;
      c.flux = document.getElementById('certFlux').value;
      c.visualAppearance = document.getElementById('certVisualAppearance').value;
      c.undercut = document.getElementById('certUndercut').value;
      c.pipingPorosity = document.getElementById('certPipingPorosity').value;
      c.witnessedBy = document.getElementById('certWitnessedBy').value;
      c.contractor = document.getElementById('certContractor').value;
      c.surveyorName = document.getElementById('certSurveyorName').value;
      c.signDate = document.getElementById('certSignDate').value;
      c.saved = true;
      renderProjectWeldersTable();
      showSaveSuccess('Certificado guardado');
      saveToStorage();
    }
    function printCertificadoFormat() {
      const w = state.projects[state.activeProject].welders[currentCertificadoWelderIndex];
      const p = state.projects[state.activeProject];
      const c = w.certificado || {};
      const pw = window.open('', '_blank');
      pw.document.write(`<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Certificado - ${w.name}</title><style>*{box-sizing:border-box}body{font-family:Arial,sans-serif;padding:20px;color:#1B365D;font-size:11px;margin:0}.sec-head{background:#1B365D;color:#fff;padding:5px 10px;font-weight:800;font-size:10px;text-transform:uppercase}.sec-body{border:1px solid #1B365D;border-top:none;padding:8px}.ft{width:100%;border-collapse:collapse}.ft th,.ft td{border:1px solid #1B365D;padding:5px 8px;font-size:10px;text-align:left}.ft th{background:#e8eef5;font-weight:bold}@media print{@page{margin:10mm}}</style></head><body>
      <div style="text-align:center;margin-bottom:12px;"><img src="${LOGO_URL}" style="max-width:140px;"><h2 style="margin:4px 0;">WELDER QUALIFICATIONS</h2></div>
      <div class="sec-head">General</div><div class="sec-body"><table class="ft"><tr><th>Buque</th><td>${c.vessel||'\u2014'}</td><th>Cliente</th><td>${c.shipyard||p.client||'\u2014'}</td></tr><tr><th>WPQ</th><td>${c.reportNo||'\u2014'}</td><th>Fecha</th><td>${c.date||'\u2014'}</td></tr></table></div>
      <div class="sec-head">Soldador</div><div class="sec-body"><table class="ft"><tr><th>Nombre</th><td>${w.name}</td><th>ID</th><td>${w.id}</td></tr><tr><th>WPS</th><td>${w.wps||p.wps||'\u2014'}</td><th>Posici\u00f3n</th><td>${w.pos||'\u2014'}</td></tr></table></div>
      </body></html>`);
      pw.document.close(); pw.focus(); pw.print();
    }

    // ===================== LISTA INSPECCION =====================
    function openInspeccionListModal() {
      if (state.activeProject === null) return;
      const p = state.projects[state.activeProject];
      document.getElementById('inspeccionListProjectInfo').textContent = `${p.name} \u2014 ${p.client || 'Sin cliente'}`;
      let html = '<div class="table-shell" style="overflow-x:auto;"><table><thead><tr><th>Matr\u00edcula</th><th>Nombre</th><th>WPS</th><th>Posici\u00f3n</th><th>Inspecci\u00f3n</th><th>Doblez</th></tr></thead><tbody>';
      if (!p.welders.length) { html += '<tr><td colspan="6" style="text-align:center;padding:20px;color:#64748b;">No hay soldadores</td></tr>'; }
      else { p.welders.forEach(w => {
        const inspSt = getInspStatus(w); const doblezSt = getDoblezStatus(w);
        html += `<tr><td style="font-weight:700;">${w.id}</td><td>${w.name}</td><td style="font-weight:600;color:#0085b3;">${w.wps||p.wps||'\u2014'}</td><td><strong>${w.pos}</strong></td><td><span class="status-micro ${inspSt.cls}">${inspSt.text}</span></td><td><span class="status-micro ${doblezSt.cls}">${doblezSt.text}</span></td></tr>`;
      }); }
      html += '</tbody></table></div>';
      document.getElementById('inspeccionListContent').innerHTML = html;
      document.getElementById('inspeccionListModal').classList.add('show');
    }
    function printInspeccionList() {
      const p = state.projects[state.activeProject];
      const htmlRows = p.welders.map(w => {
        const inspSt = getInspStatus(w); const doblezSt = getDoblezStatus(w);
        return `<tr><td style="font-weight:700;">${w.id}</td><td>${w.name}</td><td>${w.wps||p.wps||'\u2014'}</td><td>${w.pos}</td><td>${inspSt.text}</td><td>${doblezSt.text}</td></tr>`;
      }).join('');
      const pw = window.open('', '_blank');
      pw.document.write(`<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Lista - ${p.name}</title><style>body{font-family:Arial,sans-serif;padding:20px;color:#1B365D;font-size:11px}table{width:100%;border-collapse:collapse}th{background:#1B365D;color:#fff;padding:7px 8px;font-size:10px;text-align:left}td{border:1px solid #cbd5e1;padding:7px 8px}@media print{@page{margin:10mm}}</style></head><body><img src="${LOGO_URL}" style="max-width:130px;"><h2>Lista de Inspecci\u00f3n - ${p.name}</h2><table><thead><tr><th>Matr\u00edcula</th><th>Nombre</th><th>WPS</th><th>Posici\u00f3n</th><th>Inspecci\u00f3n</th><th>Doblez</th></tr></thead><tbody>${htmlRows}</tbody></table></body></html>`);
      pw.document.close(); pw.focus(); pw.print();
    }

    // ===================== MASTER WELDERS =====================
    function renderMasterWelders() {
      const container = document.getElementById('masterWeldersCards');
      const searchTerm = (document.getElementById('weldersSearch')?.value || '').toLowerCase();
      const statusFilter = document.getElementById('weldersStatusFilter')?.value || '';
      const filtered = state.masterWelders.filter(w => {
        const matchSearch = !searchTerm || w.name.toLowerCase().includes(searchTerm) || w.id.toLowerCase().includes(searchTerm);
        const matchStatus = !statusFilter || w.status === statusFilter;
        return matchSearch && matchStatus;
      });
      container.innerHTML = '';
      if (!filtered.length) { container.innerHTML = '<div class="small" style="padding:20px;text-align:center;">No hay soldadores</div>'; updateSelectionCount(); return; }
      filtered.forEach(w => {
        const originalIndex = state.masterWelders.indexOf(w);
        const initials = w.name.split(' ').map(n => n[0]).slice(0, 2).join('').toUpperCase() || 'WW';
        const div = document.createElement('div');
        div.className = `welder-card ${w.selected ? 'selected' : ''}`;
        div.innerHTML = `<input type="checkbox" ${w.selected ? 'checked' : ''} onclick="event.stopPropagation(); toggleWelderSelection(${originalIndex})" style="width:auto;" /><div class="welder-avatar">${w.photo ? `<img src="${w.photo}" />` : initials}</div><div class="welder-main"><div class="welder-name">${w.name}</div><div class="welder-id-line">Matr\u00edcula: ${w.id}</div><div class="welder-meta"><span class="status-badge ${w.status}">${w.status}</span><span class="cert-count-badge">${w.certs.length} cert.</span></div></div>`;
        div.ondblclick = () => openWelderModal(originalIndex);
        container.appendChild(div);
      });
      updateSelectionCount();
    }
    function toggleWelderSelection(index) { state.masterWelders[index].selected = !state.masterWelders[index].selected; renderMasterWelders(); }
    function toggleSelectAllWelders() { const checked = document.getElementById('selectAllWelders').checked; state.masterWelders.forEach(w => w.selected = checked); renderMasterWelders(); }
    function clearSelectedWelders() { state.masterWelders.forEach(w => w.selected = false); document.getElementById('selectAllWelders').checked = false; renderMasterWelders(); }
    function updateSelectionCount() { const count = state.masterWelders.filter(w => w.selected).length; document.getElementById('selectionCount').textContent = `${count} seleccionados`; }
    function applyMassStatusChange() {
      const newStatus = document.getElementById('massStatusChange').value;
      if (!newStatus) { alert('Seleccione un estatus'); return; }
      const selected = state.masterWelders.filter(w => w.selected);
      if (!selected.length) { alert('Seleccione al menos un soldador'); return; }
      selected.forEach(w => w.status = newStatus);
      clearSelectedWelders(); document.getElementById('massStatusChange').value = '';
      showSaveSuccess(`Estatus cambiado a "${newStatus}" para ${selected.length} soldadores`);
      saveToStorage();
    }
    function addMasterWelder() {
      if (!canEdit('certificados')) { showToast('No tienes permiso', true); return; }
      const id = document.getElementById('masterWelderId').value.trim();
      const name = document.getElementById('masterWelderName').value.trim().toUpperCase();
      const status = document.getElementById('masterWelderStatus').value;
      if (!id || !name) { alert('Matr\u00edcula y nombre son requeridos'); return; }
      if (state.masterWelders.find(w => w.id === id)) { alert('Ya existe un soldador con esa matr\u00edcula'); return; }
      state.masterWelders.push({ id, name, status, certs: [], photo: '', selected: false });
      document.getElementById('masterWelderId').value = ''; document.getElementById('masterWelderName').value = '';
      renderMasterWelders(); saveToStorage();
    }

    // ===================== WELDER MODAL =====================
    function openWelderModal(index) {
      state.currentWelderIndex = index;
      const w = state.masterWelders[index];
      document.getElementById('modalWelderName').textContent = w.name;
      document.getElementById('modalWelderId').textContent = `Matr\u00edcula: ${w.id}`;
      document.getElementById('modalStatusChange').value = w.status;
      document.getElementById('modalBasicData').innerHTML = `<p style="margin:6px 0;"><strong>Nombre:</strong> ${w.name}</p><p style="margin:6px 0;"><strong>ID:</strong> ${w.id}</p><p style="margin:6px 0;"><strong>Estado:</strong> <span class="status-badge ${w.status}">${w.status}</span></p>`;
      const photoBox = document.getElementById('modalPhotoBox');
      photoBox.innerHTML = w.photo ? `<img src="${w.photo}" />` : 'Sin foto';
      const editable = canEdit('certificados');
      document.getElementById('modalStatusChange').disabled = !editable;
      document.getElementById('deleteWelderBtn').style.display = canDelete('certificados') ? '' : 'none';
      document.getElementById('welderPhotoInput').style.display = editable ? '' : 'none';
      document.getElementById('certAddForm').style.display = editable ? '' : 'none';
      document.getElementById('certAddForm2').style.display = editable ? '' : 'none';
      document.getElementById('certAddBtnRow').style.display = editable ? '' : 'none';
      renderModalCerts();
      document.getElementById('welderModal').classList.add('show');
    }
    function updateCurrentWelderStatus(status) { if (state.currentWelderIndex === null) return; state.masterWelders[state.currentWelderIndex].status = status; renderMasterWelders(); saveToStorage(); }
    function deleteCurrentWelder() { if (state.currentWelderIndex === null) return; if (!confirm('\u00bfEliminar este soldador?')) return; state.masterWelders.splice(state.currentWelderIndex, 1); closeModal('welderModal'); renderMasterWelders(); saveToStorage(); }
    function loadWelderPhoto(event) {
      const file = event.target.files[0]; if (!file || state.currentWelderIndex === null) return;
      const reader = new FileReader();
      reader.onload = e => { state.masterWelders[state.currentWelderIndex].photo = e.target.result; document.getElementById('modalPhotoBox').innerHTML = `<img src="${e.target.result}" />`; renderMasterWelders(); saveToStorage(); };
      reader.readAsDataURL(file);
    }
    function renderModalCerts() {
      const tbody = document.getElementById('modalCertTableBody'); tbody.innerHTML = '';
      if (state.currentWelderIndex === null) return;
      const w = state.masterWelders[state.currentWelderIndex];
      const editable = canEdit('certificados');
      if (!w.certs.length) { tbody.innerHTML = '<tr><td colspan="9" style="text-align:center;padding:20px;color:#64748b;">Sin certificaciones</td></tr>'; return; }
      w.certs.forEach((c, i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${c.wps||'\u2014'}</td><td>${c.position||'\u2014'}</td><td>${c.process||'\u2014'}</td><td>${c.thickness||'\u2014'}</td><td>${c.diameter||'\u2014'}</td><td>${c.qualDate||'\u2014'}</td><td>${c.expiryDate||'\u2014'}</td><td>${c.society||'\u2014'}</td><td>${editable ? `<button class="btn btn-sm btn-danger" onclick="deleteCert(${i})">\u2716</button>` : ''}</td>`;
        tbody.appendChild(tr);
      });
    }
    function addCertToCurrentWelder() {
      if (state.currentWelderIndex === null) return;
      const cert = { wps: document.getElementById('newCertWps').value.trim(), position: document.getElementById('newCertPosition').value.trim(), process: document.getElementById('newCertProcess').value.trim(), thickness: document.getElementById('newCertThickness').value.trim(), diameter: document.getElementById('newCertDiameter').value.trim(), qualDate: document.getElementById('newCertQualDate').value, expiryDate: document.getElementById('newCertExpiryDate').value, society: document.getElementById('newCertSociety').value };
      state.masterWelders[state.currentWelderIndex].certs.push(cert);
      ['newCertWps','newCertPosition','newCertProcess','newCertThickness','newCertDiameter','newCertQualDate','newCertExpiryDate'].forEach(id => document.getElementById(id).value = '');
      document.getElementById('newCertSociety').value = '';
      renderModalCerts(); renderMasterWelders(); saveToStorage();
    }
    function deleteCert(index) {
      if (state.currentWelderIndex === null) return;
      if (!confirm('\u00bfEliminar esta certificaci\u00f3n?')) return;
      state.masterWelders[state.currentWelderIndex].certs.splice(index, 1);
      renderModalCerts(); renderMasterWelders(); saveToStorage();
    }

    // ===================== ADMIN FUNCTIONS =====================
    function addConfianzaUser() {
      const name = document.getElementById('adminNewUserName').value.trim();
      const pass = document.getElementById('adminNewUserPass').value;
      if (!name || !pass) { showToast('Nombre y contrase\u00f1a son requeridos', true); return; }
      const id = 'user_' + Date.now();
      const modules = {
        stock: document.getElementById('adminPermStock').checked,
        calificacion: document.getElementById('adminPermCalif').checked,
        certificados: document.getElementById('adminPermCert').checked,
        wps: document.getElementById('adminPermWps').checked
      };
      state.users.push({ id, name, password: pass, modules });
      document.getElementById('adminNewUserName').value = '';
      document.getElementById('adminNewUserPass').value = '';
      renderAdminUsers();
      showSaveSuccess('Usuario creado exitosamente');
      saveToStorage();
    }
    function renderAdminUsers() {
      const container = document.getElementById('adminUsersList');
      if (!container) return;
      container.innerHTML = '';
      if (!state.users.length) { container.innerHTML = '<div class="small" style="padding:30px;text-align:center;color:var(--muted);">No hay usuarios de confianza registrados.<br>Cree uno desde el panel izquierdo.</div>'; return; }
      state.users.forEach((u, i) => {
        const modNames = [];
        if (u.modules.stock) modNames.push('Stock');
        if (u.modules.calificacion) modNames.push('Calificaci\u00f3n');
        if (u.modules.certificados) modNames.push('Certificados');
        if (u.modules.wps) modNames.push('WPS');
        const initials = u.name.split(' ').map(n => n[0]).slice(0, 2).join('').toUpperCase() || 'U';
        const div = document.createElement('div');
        div.className = 'admin-user-card';
        div.innerHTML = `
          <div class="admin-user-header">
            <div class="admin-user-avatar">${initials}</div>
            <div class="admin-user-info">
              <strong>${u.name}</strong>
              <small>Usuario de confianza</small>
            </div>
            <div class="admin-user-actions">
              <button class="btn btn-sm btn-warn" onclick="toggleEditUser(${i})" title="Editar">&#9998;</button>
              <button class="btn btn-sm btn-danger" onclick="deleteConfianzaUser(${i})" title="Eliminar">\u2716</button>
            </div>
          </div>
          <div class="admin-modules-badges">${modNames.map(m => `<span class="admin-mod-badge">${m}</span>`).join('')}${!modNames.length ? '<span class="small">Sin m\u00f3dulos asignados</span>' : ''}</div>
          <div class="admin-pass-row" id="adminEditRow_${i}" style="display:none;">
            <div class="pass-field-wrap" style="flex:1;"><input id="adminEditPass_${i}" type="password" value="${u.password}" placeholder="Nueva contrase\u00f1a" /><button class="eye-toggle" type="button" onclick="togglePassVisibility('adminEditPass_${i}', this)">&#128065;</button></div>
            <button class="btn btn-sm btn-success" onclick="saveUserPassword(${i})">Guardar</button>
          </div>`;
        container.appendChild(div);
      });
    }
    function toggleEditUser(index) {
      const row = document.getElementById('adminEditRow_' + index);
      if (row) row.style.display = row.style.display === 'none' ? 'flex' : 'none';
    }
    function saveUserPassword(index) {
      const pass = document.getElementById('adminEditPass_' + index).value;
      if (!pass) { showToast('La contrase\u00f1a no puede estar vac\u00eda', true); return; }
      state.users[index].password = pass;
      showSaveSuccess('Contrase\u00f1a actualizada');
      saveToStorage();
      document.getElementById('adminEditRow_' + index).style.display = 'none';
    }
    function deleteConfianzaUser(index) {
      if (!confirm('\u00bfEliminar este usuario?')) return;
      state.users.splice(index, 1);
      renderAdminUsers(); saveToStorage();
    }

    // ===================== PASSWORD UTILITIES =====================
    function togglePassVisibility(inputId, btn) {
      const input = document.getElementById(inputId);
      if (!input) return;
      if (input.type === 'password') { input.type = 'text'; btn.innerHTML = '&#128064;'; }
      else { input.type = 'password'; btn.innerHTML = '&#128065;'; }
    }

    function changeCreadorPassword() {
      const oldPass = document.getElementById('creadorOldPass').value;
      const newPass = document.getElementById('creadorNewPass').value;
      const newPass2 = document.getElementById('creadorNewPass2').value;
      const currentPass = state.creadorPassword || CREATOR_PASSWORD;
      if (oldPass !== currentPass) { showToast('La contrase\u00f1a actual es incorrecta', true); return; }
      if (!newPass || newPass.length < 3) { showToast('La nueva contrase\u00f1a debe tener al menos 3 caracteres', true); return; }
      if (newPass !== newPass2) { showToast('Las contrase\u00f1as no coinciden', true); return; }
      state.creadorPassword = newPass;
      document.getElementById('creadorOldPass').value = '';
      document.getElementById('creadorNewPass').value = '';
      document.getElementById('creadorNewPass2').value = '';
      showSaveSuccess('Contrase\u00f1a de Creador actualizada');
      saveToStorage();
    }

    // ===================== CLOSE DROPDOWNS =====================
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.search-dropdown')) document.querySelectorAll('.search-results').forEach(r => r.classList.remove('show'));
    });

    // ===================== MOBILE NAV =====================
    function toggleSidebar() {
      const sidebar = document.querySelector('.sidebar');
      const overlay = document.getElementById('sidebarOverlay');
      const toggle = document.getElementById('menuToggle');
      sidebar.classList.toggle('open');
      overlay.classList.toggle('show');
      toggle.classList.toggle('open');
    }
    function closeSidebar() {
      document.querySelector('.sidebar').classList.remove('open');
      document.getElementById('sidebarOverlay').classList.remove('show');
      document.getElementById('menuToggle').classList.remove('open');
    }
    function setBottomNav(pageId) {
      document.querySelectorAll('#bottomNav button').forEach(b => b.classList.toggle('active', b.dataset.page === pageId));
    }
    document.querySelectorAll('.nav-btn').forEach(btn => {
      btn.addEventListener('click', () => { if (window.innerWidth <= 900) closeSidebar(); });
    });

    // ===================== INDEXEDDB =====================
    const IDB_NAME = 'WW_LocalDB';
    const IDB_VERSION = 2;
    const IDB_STORE = 'appData';
    let _idb = null;

    function openDB() {
      return new Promise((resolve, reject) => {
        const req = indexedDB.open(IDB_NAME, IDB_VERSION);
        req.onupgradeneeded = e => {
          const db = e.target.result;
          if (!db.objectStoreNames.contains(IDB_STORE)) db.createObjectStore(IDB_STORE);
        };
        req.onsuccess = e => { _idb = e.target.result; resolve(); };
        req.onerror = e => reject(e.target.error);
        req.onblocked = () => reject(new Error('IndexedDB blocked'));
      });
    }

    function dbPut(key, value) {
      return new Promise((resolve, reject) => {
        if (!_idb) { resolve(); return; }
        const tx = _idb.transaction(IDB_STORE, 'readwrite');
        tx.objectStore(IDB_STORE).put(value, key);
        tx.oncomplete = resolve;
        tx.onerror = e => reject(e.target.error);
      });
    }

    function dbGet(key) {
      return new Promise((resolve, reject) => {
        if (!_idb) { resolve(undefined); return; }
        const tx = _idb.transaction(IDB_STORE, 'readonly');
        const req = tx.objectStore(IDB_STORE).get(key);
        req.onsuccess = e => resolve(e.target.result);
        req.onerror = e => reject(e.target.error);
      });
    }

    async function saveToStorage() {
      try {
        await Promise.all([
          dbPut('stock', state.stock),
          dbPut('wps', state.wps),
          dbPut('projects', state.projects),
          dbPut('masterWelders', state.masterWelders),
          dbPut('users', state.users),
          dbPut('auth', state.auth),
          dbPut('creadorPassword', state.creadorPassword)
        ]);
      } catch(e) {
        try {
          localStorage.setItem('ww_data_v3', JSON.stringify({
            stock: state.stock, wps: state.wps,
            projects: state.projects, masterWelders: state.masterWelders,
            users: state.users, auth: state.auth
          }));
        } catch(_) {}
      }
    }

    async function loadFromStorage() {
      try {
        const [stock, wps, projects, masterWelders, users, auth] = await Promise.all([
          dbGet('stock'), dbGet('wps'), dbGet('projects'), dbGet('masterWelders'), dbGet('users'), dbGet('auth')
        ]);
        if (Array.isArray(stock)) state.stock = stock;
        if (Array.isArray(wps)) state.wps = wps;
        if (Array.isArray(projects)) state.projects = projects;
        if (Array.isArray(masterWelders)) state.masterWelders = masterWelders;
        if (Array.isArray(users)) state.users = users;
        if (auth && auth.role) state.auth = auth;
      } catch(e) {
        try {
          const raw = localStorage.getItem('ww_data_v3') || localStorage.getItem('ww_data_v2') || localStorage.getItem('ww_app_data_v1');
          if (raw) {
            const d = JSON.parse(raw);
            if (Array.isArray(d.stock)) state.stock = d.stock;
            if (Array.isArray(d.wps)) state.wps = d.wps;
            if (Array.isArray(d.projects)) state.projects = d.projects;
            if (Array.isArray(d.masterWelders)) state.masterWelders = d.masterWelders;
            if (Array.isArray(d.users)) state.users = d.users;
            if (d.auth && d.auth.role) state.auth = d.auth;
          }
        } catch(_) {}
      }
      // Normalize WPS data
      state.wps = state.wps.map(normalizeWps);
      state.selectedStock = [];
      state.activeProject = null;
      state.currentWelderIndex = null;
      state.editingWelderIndex = null;
      state.masterWelders.forEach(w => w.selected = false);
    }

    async function clearAllData() {
      if (!confirm('\u00bfBorrar TODOS los datos? Esta acci\u00f3n no se puede deshacer.')) return;
      try {
        await Promise.all([
          dbPut('stock',[]), dbPut('wps',[]), dbPut('projects',[]), dbPut('masterWelders',[]), dbPut('users',[])
        ]);
        localStorage.removeItem('ww_data_v3');
        localStorage.removeItem('ww_data_v2');
        localStorage.removeItem('ww_app_data_v1');
      } catch(_) {}
      state.stock = []; state.selectedStock = []; state.wps = [];
      state.projects = []; state.activeProject = null;
      state.masterWelders = []; state.currentWelderIndex = null; state.editingWelderIndex = null;
      state.users = [];
      renderStock(); renderWpsCards(); renderProjects(); renderMasterWelders();
      showSaveSuccess('Datos borrados');
    }

    // ===================== INIT =====================
    async function initApp() {
      const loading = document.createElement('div');
      loading.style.cssText = 'position:fixed;inset:0;background:#1B365D;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:200000;';
      loading.innerHTML = `
        <img src="${LOGO_URL}" style="max-width:220px;margin-bottom:28px;filter:brightness(0) invert(1);">
        <div style="color:#00A9E0;font-size:15px;font-weight:700;font-family:'Plus Jakarta Sans',sans-serif;letter-spacing:1px;">Cargando base de datos...</div>
        <div style="width:200px;height:3px;background:rgba(255,255,255,.15);border-radius:3px;margin-top:16px;overflow:hidden;">
          <div style="height:100%;background:#00A9E0;border-radius:3px;animation:ldbar 1.2s ease infinite;"></div>
        </div>
        <style>@keyframes ldbar{0%{width:0%}100%{width:100%}}</style>`;
      document.body.prepend(loading);

      try {
        await openDB();
        await loadFromStorage();
      } catch(e) { console.warn('DB init failed:', e); }

      renderStock();
      renderWpsCards();
      renderProjects();
      renderMasterWelders();
      goToPage('inicio');
      setBottomNav('inicio');

      setTimeout(() => { if (loading.parentNode) loading.remove(); }, 400);

      // Sidebar tools
      const sidebar = document.getElementById('mainSidebar');
      const dbLabel = document.createElement('div');
      dbLabel.style.cssText = 'color:#00A9E0;font-size:10px;padding-top:16px;text-align:center;opacity:0.85;line-height:1.5;';
      dbLabel.innerHTML = '&#128190; Base de datos local activa<br><span style="color:#64748b;font-size:9px;">IndexedDB \u2014 guardado autom\u00e1tico</span>';
      sidebar.insertBefore(dbLabel, document.querySelector('.role-indicator'));

      const clearBtn = document.createElement('button');
      clearBtn.className = 'nav-btn';
      clearBtn.style.cssText = 'background:rgba(220,38,38,0.15);color:#fca5a5;margin-top:8px;font-size:12px;';
      clearBtn.textContent = '\u2716 Borrar todos los datos';
      clearBtn.onclick = clearAllData;
      sidebar.insertBefore(clearBtn, document.querySelector('.role-indicator'));

      // Check if we should show login or auto-login
      if (state.auth && state.auth.role && state.auth.role !== 'invitado') {
        // Previously logged in
        if (state.auth.role === 'creador') {
          finishLogin();
        } else if (state.auth.role === 'confianza') {
          const user = state.users.find(u => u.id === state.auth.userId);
          if (user) { finishLogin(); } else { state.auth = { role: 'invitado', userId: null, userName: '' }; }
        }
      }
      // Always show login overlay initially unless auto-logged
      if (document.getElementById('loginOverlay').classList.contains('hidden')) {
        // Already logged in
      } else {
        // Show it
        populateConfianzaSelect();
      }
      applyPermissions();
      updateRoleIndicator();
    }

    initApp();
  </script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v8c78df7c7c0f484497ecbca7046644da1771523124516" integrity="sha512-8DS7rgIrAmghBFwoOTujcf6D9rXvH8xm8JQ1Ja01h9QX8EzXldiszufYa4IFfKdLUKTTrnSFXLDkUEOTrZQ8Qg==" data-cf-beacon='{"version":"2024.11.0","token":"7f7b0fd8732c4326aae4b9d58d5c514a","server_timing":{"name":{"cfCacheStatus":true,"cfEdge":true,"cfExtPri":true,"cfL4":true,"cfOrigin":true,"cfSpeedBrain":true},"location_startswith":null}}' crossorigin="anonymous"></script>
</body>
</html>
