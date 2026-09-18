/* [MARKENNAME] — site scripts. Progressive enhancement only: the pages work
   without JavaScript (native <details> FAQ, plain links). */
(function () {
  "use strict";

  /* --- Navigation drawer (≤ 1024px) --------------------------------------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  var backdrop = document.querySelector(".nav-backdrop");

  function setOpen(open) {
    if (!toggle || !nav) return;
    toggle.setAttribute("aria-expanded", String(open));
    nav.classList.toggle("is-open", open);
    if (backdrop) {
      backdrop.hidden = !open;
      backdrop.classList.toggle("is-open", open);
    }
    document.body.style.overflow = open ? "hidden" : "";
    var label = toggle.querySelector(".visually-hidden");
    if (label) label.textContent = open ? "Menü schließen" : "Menü öffnen";
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });
    if (backdrop) backdrop.addEventListener("click", function () { setOpen(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        toggle.focus();
      }
    });
    // Closing on resize back to desktop keeps the scroll lock from sticking.
    window.addEventListener("resize", function () {
      if (window.innerWidth > 1024 && toggle.getAttribute("aria-expanded") === "true") setOpen(false);
    });
  }

  /* --- Contact form: no backend yet (PH-06) -------------------------------- */
  var form = document.querySelector("form[data-placeholder]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form__status");
      if (status) {
        status.hidden = false;
        status.textContent = "Das Formular ist noch nicht angebunden (Platzhalter PH-06). Bitte nutzen Sie bis dahin die Kontaktdaten unten.";
        status.focus();
      }
    });
  }
})();
