/* UniqueCreation — Design C behaviour. Vanilla JS, no dependencies. */
(function () {
  "use strict";
  var D = window.UC;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = matchMedia("(hover:hover) and (pointer:fine)").matches;
  var clamp = function (v, a, b) { return v < a ? a : v > b ? b : v; };
  var lerp = function (a, b, t) { return a + (b - a) * t; };
  var ease = function (t) { return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };
  var play = function (v) { var p = v.play(); if (p && p.catch) p.catch(function () {}); };
  var pad = function (n) { return (n < 10 ? "0" : "") + n; };
  var html = document.documentElement, vw = innerWidth, vh = innerHeight;
  var hero = $(".hero");

  /* ---------- iris loader ---------- */
  var ld = $(".ld");
  var go = function () { if (hero) hero.classList.add("go"); };
  if (ld && html.classList.contains("js-ld")) {
    var lc = $(".ld__c", ld), t0 = performance.now(), dur = reduce ? 10 : 1700, R = Math.hypot(vw, vh) / 2 + 20;
    (function tick(now) {
      var p = clamp((now - t0) / dur, 0, 1);
      lc.textContent = pad(Math.round(p * 100)) + (p >= 1 ? "" : "") + " %";
      if (p < 1) return requestAnimationFrame(tick);
      try { sessionStorage.setItem("ucc", "1"); } catch (x) {}
      var o0 = performance.now();
      setTimeout(go, 250);
      (function open(n) {
        var q = clamp((n - o0) / 1100, 0, 1), e = ease(q);
        ld.style.setProperty("--h", e * R + "px");
        if (q < 1) requestAnimationFrame(open); else ld.remove();
      })(o0);
    })(t0);
  } else { if (ld) ld.remove(); setTimeout(go, 60); }

  /* ---------- cursor ---------- */
  var cur = $(".cur"), cx = -99, cy = -99, kx = -99, ky = -99;
  if (cur && fine) {
    var cr = $(".cur__r", cur), cd = $(".cur__d", cur), cl = $("span", cur), rx = -99, ry = -99;
    addEventListener("mousemove", function (e) { kx = e.clientX; ky = e.clientY; cur.classList.add("on"); });
    document.addEventListener("mouseleave", function () { cur.classList.remove("on"); });
    document.addEventListener("mouseover", function (e) {
      var t = e.target.closest("[data-cursor]");
      if (t) { cl.textContent = t.dataset.cursor; cur.classList.add("big"); } else cur.classList.remove("big");
      cur.classList.toggle("hide", !!e.target.closest(".hero:not(.hero--na)") && !e.target.closest("a,button"));
    });
  }

  /* ---------- header & menu ---------- */
  var hd = $(".hd"), mb = $(".mb"), mn = $(".mn");
  var setMenu = function (o) { if (!mn) return; mn.classList.toggle("open", o); mn.setAttribute("aria-hidden", !o); if (mb) mb.setAttribute("aria-expanded", o); html.style.overflow = o ? "hidden" : ""; };
  if (mb) mb.addEventListener("click", function () { setMenu(true); });
  $$(".mn [data-close], .mn nav a").forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
  $$("[data-year]").forEach(function (n) { n.textContent = new Date().getFullYear(); });
  $$("[data-top]").forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); }); });

  /* ---------- reveals ---------- */
  $$("[data-lines]").forEach(function (el) { $$(".ln>span", el).forEach(function (s, i) { s.style.setProperty("--k", i); }); });
  var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: .15, rootMargin: "0px 0px -6% 0px" });
  $$(".rv,[data-lines],.iv__p").forEach(function (n) { io.observe(n); });

  /* ---------- hero: slides + colour lens ---------- */
  var sl = hero ? $$(".sl", hero) : [], si = 0, hBar = hero && $(".hero__bar i", hero), hNo = hero && $(".hero__meta b", hero), hCat = hero && $(".hero__cat", hero);
  var mx = vw / 2, my = vh / 2, tmx = mx, tmy = my, rad = 0, trad = 0, inHero = false, tAuto = 0;
  if (sl.length) {
    sl[0].classList.add("on");
    var restartBar = function () { hBar.classList.remove("run"); void hBar.offsetWidth; hBar.classList.add("run"); };
    var nextSlide = function () {
      sl.forEach(function (s) { s.classList.remove("was"); });
      sl[si].classList.remove("on"); sl[si].classList.add("was");
      si = (si + 1) % sl.length; sl[si].classList.add("on");
      hNo.textContent = pad(si + 1) + " / " + pad(sl.length); hCat.textContent = sl[si].dataset.label;
      restartBar();
    };
    restartBar();
    if (!reduce) setInterval(function () { if (!document.hidden && scrollY < vh) nextSlide(); }, 6000);
    if (fine) {
      hero.addEventListener("mousemove", function (e) { var r = hero.getBoundingClientRect(); tmx = e.clientX - r.left; tmy = e.clientY - r.top; if (!inHero) { mx = tmx; my = tmy; } inHero = true; trad = Math.max(170, Math.min(vw, vh) * .26); hero.classList.add("touched"); });
      hero.addEventListener("mouseleave", function () { inHero = false; trad = 0; });
      setTimeout(function () { if (!inHero) { trad = Math.max(150, Math.min(vw, vh) * .2); } }, 2200);
    } else { setTimeout(function () { trad = Math.min(vw, vh) * .34; }, 1400); }
  }
  var lens = hero && $(".lens", hero);
  function heroFrame(now) {
    if (!sl.length || scrollY > vh * 1.2) return;
    if (!inHero) { tAuto = now / 1000; tmx = vw * (.5 + .26 * Math.sin(tAuto * .45)); tmy = vh * (.46 + .16 * Math.sin(tAuto * .7 + 1)); }
    mx = lerp(mx, tmx, inHero ? .16 : .04); my = lerp(my, tmy, inHero ? .16 : .04); rad = lerp(rad, trad, .07);
    hero.style.setProperty("--mx", mx + "px"); hero.style.setProperty("--my", my + "px"); hero.style.setProperty("--rad", rad + "px");
    var d = rad * 2 - 60; lens.style.transform = "translate3d(" + (mx - d / 2) + "px," + (my - d / 2) + "px,0)"; lens.style.opacity = rad > 80 ? 1 : 0;
  }

  /* ---------- stacking chapters ---------- */
  var cards = $$(".card");
  function cardsFrame() {
    for (var i = 0; i < cards.length - 1; i++) {
      var nr = cards[i + 1].getBoundingClientRect(), top = parseFloat(getComputedStyle(cards[i]).top) || vh * .1;
      if (nr.top > vh || cards[i].getBoundingClientRect().bottom < -50) { if (cards[i]._p !== 0) { cards[i].style.transform = ""; cards[i].style.filter = ""; cards[i]._p = 0; } continue; }
      var p = clamp(1 - (nr.top - top) / (vh - top), 0, 1); cards[i]._p = p;
      cards[i].style.transform = "scale(" + (1 - p * .07).toFixed(4) + ")"; cards[i].style.filter = "brightness(" + (1 - p * .55).toFixed(3) + ")";
    }
  }

  /* ---------- lightbox (shared) ---------- */
  var lb = $("#lb"), LB = [], li = 0;
  if (lb) {
    var lbI = $("img", lb), lbC = $(".lb__bt", lb), lbT = $("h3", lb);
    var show = function (i) { li = (i + LB.length) % LB.length; var it = LB[li]; lbI.style.opacity = 0; var im = new Image(); im.onload = function () { lbI.src = im.src; lbI.style.opacity = 1; }; im.src = "assets/img/" + it.f + ".webp"; lbC.textContent = pad(li + 1) + " — " + pad(LB.length); lbT.textContent = D.albums[it.k].title; };
    window.openLB = function (list, i) { LB = list; show(i); lb.classList.add("open"); lb.setAttribute("aria-hidden", "false"); html.style.overflow = "hidden"; };
    var closeLB = function () { lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); html.style.overflow = ""; };
    $(".x", lb).addEventListener("click", closeLB);
    $(".lb__nv--p", lb).addEventListener("click", function () { show(li - 1); });
    $(".lb__nv--n", lb).addEventListener("click", function () { show(li + 1); });
    lb.addEventListener("click", function (e) { if (e.target.classList.contains("lb__st")) closeLB(); });
    document.addEventListener("keydown", function (e) { if (!lb.classList.contains("open")) return; if (e.key === "Escape") closeLB(); if (e.key === "ArrowLeft") show(li - 1); if (e.key === "ArrowRight") show(li + 1); });
    var sx = null; lb.addEventListener("touchstart", function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) { if (sx === null) return; var d = e.changedTouches[0].clientX - sx; if (Math.abs(d) > 50) show(li + (d < 0 ? 1 : -1)); sx = null; }, { passive: true });
  }

  /* ---------- infinite wall ---------- */
  var wall = $(".wall"), W = null;
  if (wall) {
    var wl = JSON.parse(wall.dataset.list);
    W = { ox: 0, oy: 0, vx: 0, vy: 0, down: false, moved: 0, lx: 0, ly: 0, tiles: [], cols: 0, rows: 0, tw: 0, th: 0, vis: false, touch: false };
    var buildWall = function () {
      $$(".wall__t", wall).forEach(function (t) { t.remove(); });
      W.tw = vw < 700 ? 170 : vw < 1100 ? 240 : 290; W.th = Math.round(W.tw * 1.28);
      W.cols = Math.ceil(vw / W.tw) + 2; W.rows = Math.ceil(Math.max(vh, 600) / W.th) + 2; W.tiles = [];
      wall.style.setProperty("--tw", W.tw + "px"); wall.style.setProperty("--th", W.th + "px");
      var n = 0, f = document.createDocumentFragment();
      for (var c = 0; c < W.cols; c++) for (var r = 0; r < W.rows; r++) {
        var it = wl[(c * 5 + r * 3 + n) % wl.length]; n++;
        var t = document.createElement("div"); t.className = "wall__t"; t.dataset.i = wl.indexOf(it);
        t.innerHTML = '<img src="assets/img/' + it.f + '-t.webp" alt="" loading="lazy" draggable="false">';
        t._c = c; t._r = r; f.appendChild(t); W.tiles.push(t);
      }
      wall.insertBefore(f, wall.firstChild);
    };
    buildWall();
    wall.addEventListener("pointerdown", function (e) { W.down = true; W.moved = 0; W.lx = e.clientX; W.ly = e.clientY; W.touch = e.pointerType !== "mouse"; W.vx = W.vy = 0; wall.classList.add("drag"); });
    addEventListener("pointermove", function (e) {
      if (!W.down) return; var dx = e.clientX - W.lx, dy = W.touch ? 0 : e.clientY - W.ly; W.lx = e.clientX; W.ly = e.clientY;
      W.moved += Math.abs(dx) + Math.abs(dy); W.ox += dx; W.oy += dy; W.vx = dx; W.vy = dy;
    });
    var up = function () { W.down = false; wall.classList.remove("drag"); };
    addEventListener("pointerup", up); addEventListener("pointercancel", up);
    wall.addEventListener("click", function (e) { var t = e.target.closest(".wall__t"); if (!t || W.moved > 8 || !window.openLB) return; window.openLB(wl, +t.dataset.i); });
    wall.addEventListener("mouseover", function (e) { wall.classList.toggle("hov", !!e.target.closest(".wall__t")); });
    wall.addEventListener("mouseleave", function () { wall.classList.remove("hov"); });
    new IntersectionObserver(function (es) { W.vis = es[0].isIntersecting; }).observe(wall);
  }
  function wallFrame() {
    if (!W || !W.vis) return;
    if (!W.down) { W.vx *= .94; W.vy *= .94; W.ox += W.vx + (reduce ? 0 : -.35); W.oy += W.vy + (reduce ? 0 : -.18); }
    var TW = W.cols * W.tw, TH = W.rows * W.th;
    for (var i = 0; i < W.tiles.length; i++) {
      var t = W.tiles[i], off = (t._c % 2) * W.th * .5;
      var x = ((t._c * W.tw + W.ox) % TW + TW) % TW - W.tw, y = ((t._r * W.th + W.oy + off) % TH + TH) % TH - W.th;
      t.style.transform = "translate3d(" + x + "px," + y + "px,0)";
    }
  }

  /* ---------- landscape zoom grid ---------- */
  var lz = $(".lz"), lzG = lz && $(".lz__g", lz), lzO = lz && $(".lz__o", lz), lzH = lz && $(".lz__h", lz), LZ = {};
  function sizeLZ() {
    if (!lz) return;
    var mob = vw < 760; LZ.tw = mob ? vw * .62 : Math.min(vw * .3, 520); LZ.th = mob ? vh * .3 : LZ.tw * .64; LZ.gp = mob ? 12 : 22;
    lzG.style.setProperty("--tw", LZ.tw + "px"); lzG.style.setProperty("--th", LZ.th + "px"); lzG.style.setProperty("--gp", LZ.gp + "px");
    LZ.S = Math.max(vw / LZ.tw, vh / LZ.th) * 1.02;
  }
  function lzFrame() {
    if (!lz) return;
    var r = lz.getBoundingClientRect(); if (r.bottom < 0 || r.top > vh) return;
    var p = clamp(-r.top / (r.height - vh), 0, 1), e = ease(clamp((p - .08) / .62, 0, 1)), s0 = vw < 760 ? .82 : .9;
    lzG.style.transform = "scale(" + lerp(s0, LZ.S, e).toFixed(4) + ")"; lzG.style.setProperty("--rr", (1 - e).toFixed(3));
    lzH.style.opacity = 1 - clamp(p / .2, 0, 1); lzH.style.transform = "translateY(" + (-p * 120) + "px)";
    var o = clamp((p - .66) / .2, 0, 1); lzO.style.opacity = o; lzO.classList.toggle("live", o > .5);
  }

  /* ---------- now showing ---------- */
  var ns = $(".screen");
  if (ns) {
    var nsV = $("video", ns), nsI = $("img", ns), nsT = $(".screen__t", ns), nsG = $(".screen__g", ns), nsB = $(".screen .btn"), ths = $$(".th"), nsVis = false, cur2 = -1, timer = null, user = false;
    var pick = function (i, byUser) {
      if (i === cur2) return; cur2 = i; var t = ths[i];
      ths.forEach(function (x) { x.classList.toggle("on", x === t); });
      nsT.classList.add("sw"); setTimeout(function () { nsT.textContent = t.dataset.title; nsG.textContent = t.dataset.tag; nsT.classList.remove("sw"); }, 300);
      nsI.src = t.dataset.poster; nsV.classList.remove("on"); nsV.src = t.dataset.src; nsV.load();
      nsV.oncanplay = function () { nsV.classList.add("on"); }; if (nsVis) play(nsV);
      nsB.dataset.play = t.dataset.src; nsB.dataset.title = t.dataset.title; nsB.dataset.poster = t.dataset.poster;
      if (byUser) user = true;
      clearTimeout(timer); if (!user) timer = setTimeout(function () { if (nsVis) pick((cur2 + 1) % ths.length); }, 12000);
      var st = t.parentNode; if (!byUser && st.scrollWidth > st.clientWidth) st.scrollTo({ left: t.offsetLeft - 20, behavior: "smooth" });
    };
    ths.forEach(function (t, i) {
      t.addEventListener("click", function () { if (cur2 === i) openVM(t.dataset.src, t.dataset.title, t.dataset.poster); else pick(i, true); });
      if (fine) t.addEventListener("mouseenter", function () { pick(i, true); });
    });
    new IntersectionObserver(function (es) {
      nsVis = es[0].isIntersecting;
      if (nsVis) { if (cur2 < 0) pick(0); else { play(nsV); if (!user) { clearTimeout(timer); timer = setTimeout(function () { pick((cur2 + 1) % ths.length); }, 12000); } } }
      else { nsV.pause(); clearTimeout(timer); }
    }, { threshold: .25 }).observe(ns);
  }

  /* ---------- BTS orbs ---------- */
  var orbs = $$(".orb"), orbOn = [];
  if (orbs.length) {
    var oio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        var v = $("video", e.target);
        if (e.isIntersecting) { if (!v.getAttribute("src")) v.src = v.dataset.src; play(v); if (orbOn.indexOf(e.target) < 0) orbOn.push(e.target); }
        else { v.pause(); orbOn = orbOn.filter(function (x) { return x !== e.target; }); }
      });
    }, { threshold: .3 });
    orbs.forEach(function (o) { oio.observe(o); o.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); o.click(); } }); });
  }
  function orbFrame() {
    for (var i = 0; i < orbOn.length; i++) {
      var t = $("video", orbOn[i]).currentTime || 0;
      $(".orb__tc", orbOn[i]).textContent = "00:" + pad(Math.floor(t / 60)) + ":" + pad(Math.floor(t % 60)) + ":" + pad(Math.floor((t % 1) * 25));
    }
  }

  /* ---------- reels ---------- */
  $$(".rc").forEach(function (r) {
    var v = $("video", r);
    var on = function () { if (!v.getAttribute("src")) v.src = v.dataset.src; r.classList.add("play"); play(v); };
    var off = function () { r.classList.remove("play"); v.pause(); };
    if (fine) { r.addEventListener("mouseenter", on); r.addEventListener("mouseleave", off); }
    else new IntersectionObserver(function (es) { es[0].isIntersecting ? on() : off(); }, { threshold: .6 }).observe(r);
  });

  /* ---------- main loop ---------- */
  var lastY = scrollY, waF = $(".wa");
  function frame(now) {
    var y = scrollY, dy = y - lastY; lastY = y;
    if (waF) waF.classList.toggle("off", !!hero && y < vh * .6);
    if (hd) { hd.classList.toggle("solid", y > 40); if (y > vh && dy > 4) hd.classList.add("hide"); else if (dy < -4 || y < 100) hd.classList.remove("hide"); }
    if (cur && fine) { cx = lerp(cx, kx, .9); cy = lerp(cy, ky, .9); rx = lerp(rx, kx, .18); ry = lerp(ry, ky, .18); cd.style.transform = "translate3d(" + cx + "px," + cy + "px,0)"; cr.style.transform = "translate3d(" + rx + "px," + ry + "px,0)"; }
    heroFrame(now); cardsFrame(); wallFrame(); lzFrame(); orbFrame();
    requestAnimationFrame(frame);
  }
  addEventListener("resize", function () {
    var w0 = vw; vw = innerWidth; vh = innerHeight; sizeLZ();
    if (W && Math.abs(w0 - vw) > 40) buildWall();
  });
  sizeLZ(); requestAnimationFrame(frame);

  /* ---------- video modal ---------- */
  var vm = $(".vm"), vmS = vm && $(".vm__st", vm), vmT = vm && $("h3", vm), vmV = null;
  function openVM(src, title, poster) {
    if (!vm) return;
    $$("video").forEach(function (v) { if (!v.closest(".vm")) v.pause(); });
    vmV = document.createElement("video"); vmV.src = src; vmV.poster = poster || ""; vmV.controls = true; vmV.autoplay = true; vmV.playsInline = true; vmV.setAttribute("playsinline", "");
    vmS.innerHTML = ""; vmS.appendChild(vmV); vmT.textContent = title || ""; vm.classList.add("open"); vm.setAttribute("aria-hidden", "false"); html.style.overflow = "hidden"; play(vmV);
  }
  function closeVM() {
    if (!vm || !vm.classList.contains("open")) return;
    vm.classList.remove("open"); vm.setAttribute("aria-hidden", "true"); html.style.overflow = ""; if (vmV) { vmV.pause(); vmV.removeAttribute("src"); vmV.load(); } vmS.innerHTML = "";
    orbOn.forEach(function (o) { play($("video", o)); }); if (ns && nsVis) play(nsV);
  }
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-play]");
    if (t && !t.classList.contains("th")) { e.preventDefault(); openVM(t.dataset.play, t.dataset.title, t.dataset.poster); return; }
    if (vm && (e.target.closest(".vm .x") || e.target === vmS)) closeVM();
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") { closeVM(); setMenu(false); } });

  /* ---------- enquiry form ---------- */
  var form = $(".form");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var f = new FormData(form), m = ["Hi UniqueCreation, I'd like to enquire about photography."];
    ["name:Name", "type:Looking for", "date:Date", "place:Venue"].forEach(function (k) { var a = k.split(":"); if (f.get(a[0])) m.push(a[1] + ": " + f.get(a[0])); });
    if (f.get("msg")) m.push(f.get("msg"));
    open("https://wa.me/" + D.contact.whatsapp + "?text=" + encodeURIComponent(m.join("\n")), "_blank", "noopener");
  });

  /* ---------- gallery page ---------- */
  var mas = $("#mas");
  if (mas) {
    var keys = Object.keys(D.albums), tabs = $(".tabs"), more = $("#more"), PER = 28, cat = "all", shown = 0, list = [], all = [], idx = {};
    keys.forEach(function (k) { idx[k] = 0; });
    var total = keys.reduce(function (s, k) { return s + D.albums[k].items.length; }, 0);
    for (var n = 0; all.length < total && n < 5000; n++) { var k = keys[n % keys.length], a = D.albums[k].items; if (idx[k] < a.length) { var it = a[idx[k]++]; all.push({ k: k, f: it[0], w: it[1], h: it[2] }); } }
    var tab = function (key, label, cnt) { var b = document.createElement("button"); b.type = "button"; b.dataset.k = key; b.setAttribute("aria-pressed", "false"); b.innerHTML = label + "<sup>" + cnt + "</sup>"; tabs.appendChild(b); };
    tab("all", "All", total); keys.forEach(function (k) { tab(k, D.albums[k].title, D.albums[k].items.length); });
    var draw = function (reset) {
      if (reset) { mas.innerHTML = ""; shown = 0; list = cat === "all" ? all : D.albums[cat].items.map(function (it) { return { k: cat, f: it[0], w: it[1], h: it[2] }; }); }
      var f = document.createDocumentFragment(), to = Math.min(list.length, shown + PER);
      list.slice(shown, to).forEach(function (it, i) {
        var el = document.createElement("a"); el.className = "mi"; el.href = "assets/img/" + it.f + ".webp"; el.dataset.i = shown + i; el.dataset.cursor = "View"; el.style.animationDelay = Math.min(i, 14) * .04 + "s";
        el.innerHTML = '<img src="assets/img/' + it.f + '-t.webp" width="' + it.w + '" height="' + it.h + '" alt="' + D.albums[it.k].title + ' photograph by UniqueCreation" loading="lazy" decoding="async"><span>' + D.albums[it.k].title + "</span>";
        f.appendChild(el);
      });
      mas.appendChild(f); shown = to; more.hidden = shown >= list.length;
    };
    var setTab = function (key, push) {
      cat = D.albums[key] ? key : "all";
      $$("button", tabs).forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.k === cat); });
      $("#gT").innerHTML = cat === "all" ? 'The <em class="gold">collection</em>' : D.albums[cat].title.replace(/(\S+)$/, '<em class="gold">$1</em>');
      $("#gS").textContent = cat === "all" ? "Every chapter, gathered in one place. Choose one to go deeper." : D.albums[cat].blurb;
      if (push) { var u = new URL(location.href); cat === "all" ? u.searchParams.delete("a") : u.searchParams.set("a", cat); history.replaceState(null, "", u); }
      draw(true);
    };
    tabs.addEventListener("click", function (e) { var b = e.target.closest("button"); if (!b) return; setTab(b.dataset.k, true); var top = mas.getBoundingClientRect().top + scrollY - 120; if (scrollY > top) scrollTo({ top: top, behavior: "smooth" }); });
    more.addEventListener("click", function () { draw(false); });
    mas.addEventListener("click", function (e) { var a = e.target.closest(".mi"); if (a && window.openLB) { e.preventDefault(); window.openLB(list, +a.dataset.i); } });
    setTab(new URL(location.href).searchParams.get("a") || "all", false);
  }
})();
