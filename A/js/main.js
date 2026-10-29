/* UniqueCreation — behaviour. Vanilla JS, no dependencies. */
(function () {
  "use strict";
  var D = window.UC, $ = function (s, r) { return (r || document).querySelector(s); }, $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = window.matchMedia("(hover:hover) and (pointer:fine)").matches;
  var lerp = function (a, b, t) { return a + (b - a) * t; };
  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };

  /* ---------- header / menu ---------- */
  var hdr = $(".hdr"), burger = $(".burger"), menu = $(".menu"), lastY = 0;
  function setMenu(o) {
    if (!burger) return;
    burger.setAttribute("aria-expanded", o); menu.classList.toggle("open", o); menu.setAttribute("aria-hidden", !o);
    document.documentElement.style.overflow = o ? "hidden" : "";
  }
  if (burger) {
    burger.addEventListener("click", function () { setMenu(burger.getAttribute("aria-expanded") !== "true"); });
    $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
  }
  $$("[data-year]").forEach(function (n) { n.textContent = new Date().getFullYear(); });
  $$("[data-top]").forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); }); });

  /* ---------- word masks + reveals ---------- */
  $$("[data-words]").forEach(function (el) {
    var k = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (c) {
        if (c.nodeType === 3) {
          var frag = document.createDocumentFragment();
          c.textContent.split(/(\s+)/).forEach(function (t) {
            if (!t) return;
            if (/^\s+$/.test(t)) { frag.appendChild(document.createTextNode(" ")); return; }
            var w = document.createElement("span"); w.className = "wd"; var i = document.createElement("i"); i.style.setProperty("--k", k++); i.textContent = t; w.appendChild(i); frag.appendChild(w);
          });
          c.parentNode.replaceChild(frag, c);
        } else if (c.nodeType === 1 && c.tagName !== "BR") walk(c);
      });
    })(el);
  });
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
  }, { threshold: .15, rootMargin: "0px 0px -6% 0px" }) : null;
  $$(".rv,[data-words]").forEach(function (n) { io ? io.observe(n) : n.classList.add("in"); });

  /* statement: words fill with scroll */
  var say = $(".say p"), sayW = [];
  if (say) {
    say.innerHTML = say.textContent.trim().split(/\s+/).map(function (w) {
      var em = /^\*/.test(w); w = w.replace(/\*/g, "");
      return '<span class="w' + (em ? " em" : "") + '">' + w + "</span>";
    }).join(" ");
    sayW = $$(".w", say);
  }

  /* ---------- hero ring ---------- */
  var ringWrap = $(".ring-wrap"), ring = $(".ring"), cards = ring ? $$(".rc", ring) : [];
  var spin = 0, dragV = 0, dragging = false, lastX = 0, R = 0, step = 0, cw = 0;
  function sizeRing() {
    if (!ring) return;
    var vw = window.innerWidth;
    cw = clamp(vw * (vw < 700 ? .4 : .135), 112, 220);
    var n = cards.length; step = 360 / n;
    R = (cw / 2) / Math.tan(Math.PI / n) * 1.16;
    ring.style.setProperty("--cw", cw + "px"); ring.style.setProperty("--R", R + "px"); ring.style.setProperty("--step", step + "deg");
  }
  if (ring) {
    cards.forEach(function (c, i) { c.style.setProperty("--i", i); });
    sizeRing();
    ringWrap.addEventListener("pointerdown", function (e) { dragging = true; lastX = e.clientX; dragV = 0; });
    window.addEventListener("pointermove", function (e) { if (!dragging) return; var dx = e.clientX - lastX; lastX = e.clientX; dragV = dx * .32; spin += dragV; });
    window.addEventListener("pointerup", function () { dragging = false; });
  }

  /* ---------- band velocity ---------- */
  var bandAnim = null;
  var bt = $(".band__track");
  if (bt && bt.getAnimations) { setTimeout(function () { bandAnim = bt.getAnimations()[0]; }, 200); }

  /* ---------- genre preview ---------- */
  var gpv = $(".gpv"), gx = 0, gy = 0, tx = 0, ty = 0, gOn = false;
  if (gpv && fine) {
    var gimgs = $$("img", gpv);
    $$(".g").forEach(function (g) {
      g.addEventListener("mouseenter", function () {
        var i = +g.dataset.i; gimgs.forEach(function (im, k) { im.classList.toggle("on", k === i); });
        gpv.classList.add("on"); gOn = true;
      });
      g.addEventListener("mouseleave", function () { gpv.classList.remove("on"); gOn = false; });
    });
    window.addEventListener("mousemove", function (e) { tx = e.clientX; ty = e.clientY; if (!gx && !gy) { gx = tx; gy = ty; } });
  }

  /* ---------- reels strip ---------- */
  var strip = $(".rstrip"), drift = true, sDown = false, sx0 = 0, sl0 = 0, moved = 0;
  if (strip) {
    var kids = $$(".rl", strip);
    kids.forEach(function (k) { var c = k.cloneNode(true); c.setAttribute("aria-hidden", "true"); c.tabIndex = -1; strip.appendChild(c); });
    strip.addEventListener("pointerdown", function (e) { sDown = true; moved = 0; sx0 = e.clientX; sl0 = strip.scrollLeft; strip.classList.add("drag"); });
    window.addEventListener("pointermove", function (e) { if (!sDown) return; var dx = e.clientX - sx0; moved = Math.max(moved, Math.abs(dx)); strip.scrollLeft = sl0 - dx; });
    window.addEventListener("pointerup", function () { sDown = false; strip.classList.remove("drag"); });
    strip.addEventListener("click", function (e) { if (moved > 6) { e.stopImmediatePropagation(); e.preventDefault(); } }, true);
    strip.addEventListener("mouseenter", function () { drift = false; });
    strip.addEventListener("mouseleave", function () { drift = true; });
    strip.addEventListener("touchstart", function () { drift = false; }, { passive: true });
    strip.addEventListener("touchend", function () { setTimeout(function () { drift = true; }, 2200); }, { passive: true });
  }
  var vio = "IntersectionObserver" in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      var v = e.target; if (e.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } else v.pause();
    });
  }, { threshold: .25 }) : null;
  $$("video[data-pv]").forEach(function (v) { v.muted = true; vio && vio.observe(v); });
  /* film card hover previews */
  $$(".fc").forEach(function (c) {
    var v = $("video", c); if (!v) return;
    c.addEventListener("mouseenter", function () { v.classList.add("on"); var p = v.play(); if (p && p.catch) p.catch(function () {}); });
    c.addEventListener("mouseleave", function () { v.classList.remove("on"); v.pause(); });
  });

  /* ---------- still section ---------- */
  var still = $(".still"), stillT = $$(".still__t");

  /* ---------- main loop ---------- */
  var sy = window.scrollY, vel = 0, prog = $(".progress i"), vh = window.innerHeight;
  function frame() {
    var y = window.scrollY, dy = y - sy; sy = y; vel = lerp(vel, dy, .12);
    var max = document.documentElement.scrollHeight - vh;
    if (prog) prog.parentNode.style.setProperty("--sp", max > 0 ? y / max : 0);
    if (hdr) { hdr.classList.toggle("is-solid", y > 30); hdr.classList.toggle("is-hide", y > 420 && dy > 3 && !(menu && menu.classList.contains("open"))); if (dy < -3) hdr.classList.remove("is-hide"); }

    if (ring && y < vh * 1.4) {
      if (!dragging) { dragV *= .94; spin += dragV; }
      spin += reduce ? 0 : .09 + dy * .12;
      ring.style.transform = "rotateX(-5deg) rotateY(" + spin + "deg)";
      var base = spin;
      for (var i = 0; i < cards.length; i++) {
        var a = ((i * step + base) % 360 + 360) % 360, c = Math.cos(a * Math.PI / 180);
        var o = .28 + .72 * ((c + 1) / 2);
        cards[i].style.opacity = o.toFixed(3);
        cards[i].style.filter = c < 0 ? "saturate(" + (.55 + .45 * (c + 1)).toFixed(2) + ")" : "none";
      }
    }
    if (bandAnim) bandAnim.playbackRate = 1 + clamp(Math.abs(vel) * .45, 0, 7);
    if (gpv && fine) { gx = lerp(gx, tx, .14); gy = lerp(gy, ty, .14); var rot = clamp((tx - gx) * .12, -14, 14); gpv.style.transform = "translate3d(" + (gx + 30) + "px," + (gy - 150) + "px,0) rotate(" + rot + "deg) scale(" + (gOn ? 1 : .7) + ")"; }
    if (sayW.length) {
      var r = say.getBoundingClientRect(), p0 = clamp((vh * .86 - r.top) / (r.height + vh * .3), 0, 1);
      for (var j = 0; j < sayW.length; j++) { var f = clamp(p0 * (sayW.length + 6) - j, 0, 1); sayW[j].style.setProperty("--f", f.toFixed(2)); }
    }
    if (strip && drift && !sDown && !reduce) {
      var half = strip.scrollWidth / 2; strip.scrollLeft += .6 + Math.abs(vel) * .15;
      if (strip.scrollLeft >= half) strip.scrollLeft -= half;
      if (strip.scrollLeft <= 0 && !sDown) strip.scrollLeft += 0;
    }
    if (strip && sDown) { var h2 = strip.scrollWidth / 2; if (strip.scrollLeft >= h2) { strip.scrollLeft -= h2; sl0 -= h2; } if (strip.scrollLeft <= 0) { strip.scrollLeft += h2; sl0 += h2; } }
    if (still) {
      var sr = still.getBoundingClientRect();
      if (sr.bottom > 0 && sr.top < vh) {
        var sp = clamp(-sr.top / (sr.height - vh), 0, 1);
        stillT.forEach(function (t, k) { t.style.transform = "translate3d(" + (k % 2 ? sp * 20 - 20 : -sp * 20) + "vw,0,0)"; });
      }
    }
    requestAnimationFrame(frame);
  }
  window.addEventListener("resize", function () { vh = window.innerHeight; sizeRing(); });
  requestAnimationFrame(frame);

  /* ---------- video modal ---------- */
  var fm = $(".fm");
  if (fm) {
    var fmT = $("h3", fm), fmS = $(".fm__stage", fm), fmV = null;
    var openFM = function (src, title, poster) {
      fmV = document.createElement("video"); fmV.src = src; fmV.poster = poster || ""; fmV.controls = true; fmV.autoplay = true; fmV.playsInline = true; fmV.setAttribute("playsinline", "");
      fmS.innerHTML = ""; fmS.appendChild(fmV); fmT.textContent = title; fm.classList.add("open"); fm.setAttribute("aria-hidden", "false"); document.documentElement.style.overflow = "hidden";
      var p = fmV.play(); if (p && p.catch) p.catch(function () {});
    };
    var closeFM = function () { fm.classList.remove("open"); fm.setAttribute("aria-hidden", "true"); document.documentElement.style.overflow = ""; if (fmV) { fmV.pause(); fmV.removeAttribute("src"); fmV.load(); } fmS.innerHTML = ""; };
    document.addEventListener("click", function (e) {
      var t = e.target.closest("[data-play]"); if (t) { e.preventDefault(); openFM(t.dataset.play, t.dataset.title || "", t.dataset.poster); return; }
      if (e.target.closest(".fm__x") || e.target === fm || e.target === fmS) closeFM();
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && fm.classList.contains("open")) closeFM(); });
  }

  /* ---------- enquiry form -> WhatsApp ---------- */
  var enq = $(".enq");
  if (enq) enq.addEventListener("submit", function (e) {
    e.preventDefault();
    var f = new FormData(enq), parts = ["Hi UniqueCreation, I'd like to enquire about photography."];
    if (f.get("name")) parts.push("Name: " + f.get("name"));
    if (f.get("type")) parts.push("Looking for: " + f.get("type"));
    if (f.get("date")) parts.push("Date: " + f.get("date"));
    if (f.get("msg")) parts.push(f.get("msg"));
    window.open("https://wa.me/" + D.contact.whatsapp + "?text=" + encodeURIComponent(parts.join("\n")), "_blank", "noopener");
  });

  /* ---------- gallery page ---------- */
  var mas = $("#mas");
  if (mas) {
    var keys = Object.keys(D.albums), chips = $(".chips"), more = $("#more"), PER = 24, cur = "all", shown = 0, list = [];
    var allItems = [];
    keys.forEach(function (k) { D.albums[k].items.forEach(function (it) { allItems.push({ k: k, f: it[0], w: it[1], h: it[2] }); }); });
    // interleave albums so "All" is varied
    var inter = [], idx = {}; keys.forEach(function (k) { idx[k] = 0; });
    for (var n = 0, left = allItems.length; left > 0 && n < 4000; n++) { var k2 = keys[n % keys.length]; var arr = D.albums[k2].items; if (idx[k2] < arr.length) { var it = arr[idx[k2]++]; inter.push({ k: k2, f: it[0], w: it[1], h: it[2] }); left--; } }
    var mkChip = function (key, label, count) { var b = document.createElement("button"); b.type = "button"; b.dataset.k = key; b.setAttribute("aria-pressed", "false"); b.innerHTML = label + "<small>" + count + "</small>"; chips.appendChild(b); return b; };
    mkChip("all", "All", inter.length);
    keys.forEach(function (k) { mkChip(k, D.albums[k].title, D.albums[k].items.length); });
    var draw = function (reset) {
      if (reset) { mas.innerHTML = ""; shown = 0; list = cur === "all" ? inter : D.albums[cur].items.map(function (it) { return { k: cur, f: it[0], w: it[1], h: it[2] }; }); }
      var slice = list.slice(shown, shown + PER), frag = document.createDocumentFragment();
      slice.forEach(function (it, i) {
        var a = document.createElement("a"); a.className = "gi"; a.href = "assets/img/" + it.f + ".webp"; a.dataset.i = shown + i; a.style.animationDelay = Math.min(i, 12) * 0.04 + "s";
        a.innerHTML = '<img src="assets/img/' + it.f + '-t.webp" width="' + it.w + '" height="' + it.h + '" loading="lazy" decoding="async" alt="' + D.albums[it.k].title + ' photograph by UniqueCreation">';
        frag.appendChild(a);
      });
      mas.appendChild(frag); shown += slice.length; more.hidden = shown >= list.length;
    };
    var setCur = function (k, push) {
      cur = D.albums[k] || k === "all" ? k : "all";
      $$("button", chips).forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.k === cur); });
      $("#galTitle").innerHTML = cur === "all" ? "The <em>gallery</em>" : D.albums[cur].title.replace(/(\S+)$/, "<em>$1</em>");
      $("#galSub").textContent = cur === "all" ? "A mix from every album. Pick a category to go deeper." : D.albums[cur].blurb;
      if (push) { var u = new URL(location.href); cur === "all" ? u.searchParams.delete("a") : u.searchParams.set("a", cur); history.replaceState(null, "", u); }
      draw(true);
    };
    chips.addEventListener("click", function (e) { var b = e.target.closest("button"); if (b) setCur(b.dataset.k, true); });
    more.addEventListener("click", function () { draw(false); });
    setCur(new URL(location.href).searchParams.get("a") || "all", false);
    // lightbox
    var lb = $("#lb"), lbImg = $("img", lb), lbC = $("#lbCount"), li = 0;
    var show = function (i) { li = (i + list.length) % list.length; lbImg.style.opacity = 0; var im = new Image(); im.onload = function () { lbImg.src = im.src; lbImg.style.opacity = 1; }; im.src = "assets/img/" + list[li].f + ".webp"; lbC.textContent = (li + 1) + " / " + list.length; };
    var openLB = function (i) { show(i); lb.classList.add("open"); lb.setAttribute("aria-hidden", "false"); document.documentElement.style.overflow = "hidden"; };
    var closeLB = function () { lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); document.documentElement.style.overflow = ""; };
    mas.addEventListener("click", function (e) { var a = e.target.closest(".gi"); if (a) { e.preventDefault(); openLB(+a.dataset.i); } });
    $(".lb__x", lb).addEventListener("click", closeLB);
    $(".lb__nav--p", lb).addEventListener("click", function () { show(li - 1); });
    $(".lb__nav--n", lb).addEventListener("click", function () { show(li + 1); });
    document.addEventListener("keydown", function (e) { if (!lb.classList.contains("open")) return; if (e.key === "Escape") closeLB(); if (e.key === "ArrowLeft") show(li - 1); if (e.key === "ArrowRight") show(li + 1); });
    var tx0 = null; lb.addEventListener("touchstart", function (e) { tx0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) { if (tx0 === null) return; var d = e.changedTouches[0].clientX - tx0; if (Math.abs(d) > 50) show(li + (d < 0 ? 1 : -1)); tx0 = null; }, { passive: true });
    lb.addEventListener("click", function (e) { if (e.target.classList.contains("lb__stage")) closeLB(); });
  }
})();
