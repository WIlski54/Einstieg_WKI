/* Fokus-Reader für das Original-Arbeitsblatt: Rasterseiten, PDF-Ansicht (Desktop), separater Link,
   Schließen oben und unten, Escape, Fokusrückgabe, gesperrtes Hintergrundscrolling. Standard §19. */
WK.reader = (() => {
  "use strict";
  const { $, $$, esc } = WK;
  const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  let pages = [], index = 0, trigger = null, pdfMode = false;

  function init() {
    const r = $("#reader"); if (!r) return;
    pages = JSON.parse(r.dataset.pages || "[]");
    if (isIOS) { const b = $("#reader-pdf-toggle"); if (b) b.hidden = true; }
  }
  function render() {
    const p = pages[index]; if (!p) return;
    $("#reader-img").src = p.src; $("#reader-img").alt = p.alt;
    $("#reader-page").textContent = `Seite ${index + 1} von ${pages.length}`;
    $("#reader-prev").disabled = index === 0; $("#reader-next").disabled = index >= pages.length - 1;
    $("#reader-img").hidden = pdfMode; $("#reader-frame").hidden = !pdfMode;
    if (pdfMode && !$("#reader-frame").src) $("#reader-frame").src = $("#reader").dataset.pdf + "#page=" + (index + 1);
  }
  function open(el) {
    trigger = el; index = parseInt(el.dataset.page || "1", 10) - 1; pdfMode = false;
    const r = $("#reader"); r.hidden = false; document.body.classList.add("no-scroll");
    render();
    setTimeout(() => $("#reader-close-top").focus(), 30);
  }
  function close() {
    $("#reader").hidden = true; document.body.classList.remove("no-scroll");
    if (trigger && trigger.focus) trigger.focus();
  }
  WK.actions["reader-open"] = open;
  WK.actions["reader-close"] = close;
  WK.actions["reader-prev"] = () => { if (index > 0) { index--; render(); } };
  WK.actions["reader-next"] = () => { if (index < pages.length - 1) { index++; render(); } };
  WK.actions["reader-pdf"] = () => { pdfMode = !pdfMode; render(); };
  document.addEventListener("keydown", e => {
    const r = $("#reader"); if (!r || r.hidden) return;
    if (e.key === "Escape") { e.preventDefault(); close(); }
    if (e.key === "ArrowRight") WK.actions["reader-next"]();
    if (e.key === "ArrowLeft") WK.actions["reader-prev"]();
  });
  // Nur ein Original gleichzeitig ausklappen
  document.addEventListener("toggle", e => {
    if (e.target.classList && e.target.classList.contains("material-details") && e.target.open && !WK.pruefmodus) {   // Prüfmodus: alles bleibt offen
      $$(".material-details").forEach(d => { if (d !== e.target) d.open = false; });
    }
  }, true);
  return { init, open, close };
})();
