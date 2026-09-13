/* SVG-Karte mit echten Küstenlinien (Natural Earth) und tippbaren Hotspots. */
WK.karte = (() => {
  "use strict";
  const { INHALTE, state, $, $$, esc, cfgOf, niveauOf, body, showFb, markComplete, dirty, aufgabenByNr } = WK;
  const MAP_W = 900, MAP_H = 638;
  const px = lon => ((lon + 12) * 17).toFixed(1);
  const py = lat => ((63 - lat) * 22).toFixed(1);
  const poly = pts => pts.map(p => `${px(p[0])},${py(p[1])}`).join(" ");
  // Beschriftungen, die sich sonst überlappen, bekommen feste Versätze (dx, dy relativ zum Punkt).
  const LABEL_OFFSET = {
    "europa1914:bruessel": { dx: -26, dy: -30 }, "europa1914:belgrad": { dx: 34, dy: 36 }, "europa1914:wien": { dx: 0, dy: -30 },
    "europa1920:saar": { dx: -8, dy: 36 }, "europa1920:strassburg": { dx: 0, dy: -30 }, "europa1920:prag": { dx: -30, dy: -30 },
    "europa1920:wien": { dx: 40, dy: 36 }, "europa1920:budapest": { dx: 36, dy: 36 }, "europa1920:danzig": { dx: 0, dy: -30 },
    "europa1920:riga": { dx: 44, dy: -6 }, "europa1920:warschau": { dx: 26, dy: 36 }, "kriegsende:brest": { dx: 0, dy: -30 },
    "kriegsende:spa": { dx: 30, dy: -30 }, "kriegsende:compiegne": { dx: -10, dy: 36 }, "kriegsende:amiens": { dx: -40, dy: -30 },
    "julikrise:bruessel": { dx: -30, dy: -30 }, "julikrise:paris": { dx: -34, dy: 36 }, "fronten:westfront": { dx: -30, dy: 36 },
  };

  function buildMapSVG(spec, nr, karteKey) {
    const pointById = Object.fromEntries(spec.punkte.map(p => [p.id, p]));
    const linien = (spec.linien || []).map(([a, b, bloc]) => { const A = pointById[a], B = pointById[b]; return `<line class="map-line map-line-${bloc}" x1="${px(A.lon)}" y1="${py(A.lat)}" x2="${px(B.lon)}" y2="${py(B.lat)}"/>`; }).join("");
    const fronten = (spec.fronten || []).map(f => `<polyline class="map-front" points="${poly(f.punkte)}"><title>${esc(f.name)}</title></polyline>`).join("");
    const punkte = spec.punkte.map(p => {
      const off = LABEL_OFFSET[`${karteKey}:${p.id}`] || { dx: 0, dy: 36 };
      return `
      <g class="hs-dot hs-${p.bloc}" data-action="spot" data-nr="${nr}" data-spot="${p.id}" role="button" tabindex="0" aria-label="${esc(p.titel)}">
        <circle cx="${px(p.lon)}" cy="${py(p.lat)}" r="22"/>
        <text class="hs-icon" x="${px(p.lon)}" y="${py(p.lat)}" text-anchor="middle" dominant-baseline="central" aria-hidden="true">${p.icon}</text>
        <text class="hs-label" x="${(parseFloat(px(p.lon)) + off.dx).toFixed(1)}" y="${(parseFloat(py(p.lat)) + off.dy).toFixed(1)}" text-anchor="middle">${esc(p.label)}</text>
      </g>`;
    }).join("");
    const legende = (spec.legende || []).map(([k, l]) => `<span class="legend-item"><i class="legend-dot hs-${k}"></i>${esc(l)}</span>`).join("");
    const land = window.WK_KARTE_LAND ? `<path class="map-land-poly" d="${window.WK_KARTE_LAND}"/>` : "";
    return `
      <div class="map-wrap">
        <svg viewBox="0 0 ${MAP_W} ${MAP_H}" class="map-svg" xmlns="http://www.w3.org/2000/svg" role="group" aria-label="${esc(spec.titel)}">
          <rect width="${MAP_W}" height="${MAP_H}" class="map-water"/>
          ${land}
          ${fronten}${linien}${punkte}
        </svg>
      </div>
      <div class="map-legend">${legende}<span class="legend-note">vereinfachte Karte (Natural Earth)</span></div>`;
  }

  function render(t) {
    const spec = INHALTE.karten[t.karte];
    const cfg = cfgOf(t);
    const needed = Math.min(t.benoetigt[niveauOf(t.nr)] || 3, spec.punkte.length);
    state.runtime[t.nr] = { visited: new Set(), needed };
    return `${buildMapSVG(spec, t.nr, t.karte)}
      <div class="feedback-box feedback-info show map-info" id="mapinfo-${t.nr}" role="status">👆 Tippe auf die Punkte der Karte. Erkunde mindestens <strong>${needed}</strong> Orte, dann erscheint die Frage. <span class="map-progress" id="mapprog-${t.nr}">0/${needed}</span></div>
      ${WK.aufgaben.renderMC(t.nr, cfg, true)}`;
  }

  function zeigeOrt(nr, p, still) {
    const t = aufgabenByNr[nr]; const rt = state.runtime[nr];
    $$(".hs-dot.active", body(nr)).forEach(e => e.classList.remove("active"));
    const g = $(`.hs-dot[data-spot="${p.id}"]`, body(nr));
    if (g) g.classList.add("active", "visited");
    rt.visited.add(p.id);
    const info = document.getElementById("mapinfo-" + nr);
    const n = Math.min(rt.visited.size, rt.needed);
    info.innerHTML = `<strong>${p.icon} ${esc(p.titel)}</strong><br><span>${esc(p.text)}</span><span class="map-progress" id="mapprog-${nr}">${n}/${rt.needed}</span>`;
    if (rt.visited.size >= rt.needed) { const mc = document.getElementById("mc-" + nr); if (mc && mc.hidden) { mc.hidden = false; if (!still) showFb(nr, "info", "🗺️ Gut erkundet! Jetzt die Frage beantworten."); } }
    if (!still) dirty();
  }
  WK.actions.spot = g => {
    const nr = g.dataset.nr; const t = aufgabenByNr[nr];
    const p = INHALTE.karten[t.karte].punkte.find(x => x.id === g.dataset.spot);
    if (p) zeigeOrt(nr, p);
  };
  document.addEventListener("keydown", e => {
    if ((e.key === "Enter" || e.key === " ") && e.target.classList && e.target.classList.contains("hs-dot")) { e.preventDefault(); WK.actions.spot(e.target); }
  });

  function collect(nr) {
    const rt = state.runtime[nr]; if (!rt || !rt.visited) return undefined;
    if (!rt.visited.size && !rt.mc) return undefined;
    return { typ: "karte", besucht: Array.from(rt.visited), mc: rt.mc || null };
  }
  function restore(nr, d) {
    const t = aufgabenByNr[nr]; const rt = state.runtime[nr]; if (!t || !rt || !d) return;
    const punkte = INHALTE.karten[t.karte].punkte;
    (d.besucht || []).forEach(id => { const p = punkte.find(x => x.id === id); if (p) { zeigeOrt(nr, p, true); } });
    if (d.mc && Array.isArray(d.mc.gewaehlt)) {
      const group = $(`#mc-${nr} .mc-options`);
      if (group) {
        if (d.mc.fertig) WK.aufgaben.mcAuswerten(nr, group, d.mc.gewaehlt, true);
        else $$(".mc-btn", group).forEach(b => b.classList.toggle("selected-multi", d.mc.gewaehlt.includes(parseInt(b.dataset.idx, 10))));
      }
    }
  }

  return { render, collect, restore };
})();
