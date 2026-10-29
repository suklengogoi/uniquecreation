/* UniqueCreation — Design B behaviour. Vanilla JS. */
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
  var html = document.documentElement, vw = innerWidth, vh = innerHeight;

  /* ---------- loader (first visit per session) ---------- */
  var ld = $(".ld");
  if (ld && html.classList.contains("js-ld")) {
    var c = $(".ld__c", ld), t0 = performance.now(), dur = reduce ? 10 : 1500;
    (function tick(now) {
      var p = clamp((now - t0) / dur, 0, 1), e = 1 - Math.pow(1 - p, 3);
      c.textContent = String(Math.round(e * 100)).padStart(3, "0"); ld.style.setProperty("--p", e);
      if (p < 1) requestAnimationFrame(tick);
      else { ld.classList.add("done"); try { sessionStorage.setItem("ucb", "1"); } catch (x) {} setTimeout(function () { ld.remove(); }, 1300); }
    })(t0);
  } else if (ld) ld.remove();

  /* ---------- cursor ---------- */
  var cur = $(".cur"), cx = -100, cy = -100, kx = -100, ky = -100;
  if (cur && fine) {
    var cl = $("span", cur);
    addEventListener("mousemove", function (e) { kx = e.clientX; ky = e.clientY; cur.classList.add("on"); });
    document.addEventListener("mouseleave", function () { cur.classList.remove("on"); });
    document.addEventListener("mouseover", function (e) {
      var t = e.target.closest("[data-cursor]");
      if (t) { cl.textContent = t.dataset.cursor; cur.classList.add("big"); } else cur.classList.remove("big");
    });
  }

  /* ---------- header + menu ---------- */
  var hd = $(".hd"), mb = $(".mbtn"), mn = $(".mn");
  var setMenu = function (o) { if (!mn) return; mn.classList.toggle("open", o); mn.setAttribute("aria-hidden", !o); mb.setAttribute("aria-expanded", o); html.style.overflow = o ? "hidden" : ""; };
  if (mb) mb.addEventListener("click", function () { setMenu(true); });
  $$(".mn [data-close], .mn nav a").forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
  $$("[data-year]").forEach(function (n) { n.textContent = new Date().getFullYear(); });
  $$("[data-top]").forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); }); });

  /* ---------- word splitting + reveals ---------- */
  $$("[data-words]").forEach(function (el) {
    var k = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var f = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (w) {
            if (!w) return;
            if (/^\s+$/.test(w)) { f.appendChild(document.createTextNode(" ")); return; }
            var s = document.createElement("span"); s.className = "wd"; var i = document.createElement("i"); i.style.setProperty("--k", k++); i.textContent = w; s.appendChild(i); f.appendChild(s);
          });
          n.parentNode.replaceChild(f, n);
        } else if (n.nodeType === 1 && n.tagName !== "BR") walk(n);
      });
    })(el);
  });
  var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: .12, rootMargin: "0px 0px -8% 0px" });
  $$(".rv,[data-words],.strip,.fan").forEach(function (n) { io.observe(n); });

  /* ---------- zoom hero ---------- */
  var zh = $(".zh"), zf = zh && $(".zh__f", zh), zImgs = zf ? $$("img", zf) : [], zi = 0;
  var zCap = zh && $(".zh__cap", zh), zLab = zh && $(".zh__cap .c", zh), zMsg = zh && $(".zh__msg", zh), zT1 = zh && $(".zh__t--1", zh), zT2 = zh && $(".zh__t--2", zh);
  if (zImgs.length) {
    zImgs[0].classList.add("on");
    var next = function () {
      var prev = zImgs[zi]; zi = (zi + 1) % zImgs.length;
      zImgs.forEach(function (im) { im.classList.remove("was"); });
      prev.classList.remove("on"); prev.classList.add("was");
      var n = zImgs[zi]; n.classList.remove("on"); void n.offsetWidth; n.classList.add("on");
      if (zLab) zLab.innerHTML = "<b>No. " + String(zi + 1).padStart(2, "0") + " / " + String(zImgs.length).padStart(2, "0") + "</b>" + n.dataset.label;
    };
    if (!reduce) setInterval(function () { if (scrollY < vh * 2.6 && !document.hidden) next(); }, 3200);
  }
  function heroFrame() {
    if (!zh) return;
    var r = zh.getBoundingClientRect(); if (r.bottom < 0) return;
    var p = clamp(-r.top / (r.height - vh), 0, 1), e = ease(clamp(p / .78, 0, 1));
    var mob = vw < 900, fw = mob ? Math.min(vw * .68, vh * .42) : Math.min(vw * .3, vh * .6), fh = fw;
    var t = (vh - fh) / 2 * (1 - e) + (mob ? 0 : 0), l = (vw - fw) / 2 * (1 - e);
    zf.style.setProperty("--t", t + "px"); zf.style.setProperty("--l", l + "px");
    zf.style.setProperty("--r", (fw / 2) * (1 - e) + "px");
    for (var q = 0; q < zImgs.length; q++) {
      var im = zImgs[q], iw = +im.dataset.w || 3, ih = +im.dataset.h || 4, k = Math.max(vw / iw, vh / ih), W = iw * k, H = ih * k;
      var s0 = Math.max(fw / W, fh / H) * 1.04;
      im.style.width = W + "px"; im.style.height = H + "px";
      im.style.transform = "translate(-50%,-50%) scale(" + lerp(Math.min(s0, 1), 1, e).toFixed(4) + ")";
    }
    zf.style.setProperty("--sh", clamp((p - .45) / .35, 0, 1));
    var mo = clamp((p - .62) / .25, 0, 1); zMsg.style.setProperty("--mo", mo); zMsg.classList.toggle("live", mo > .5);
    zT1.style.transform = "translate3d(" + (-e * 60) + "vw,0,0)"; zT2.style.transform = "translate3d(" + (e * 60) + "vw,0,0)";
    zT1.style.opacity = zT2.style.opacity = 1 - clamp(e * 1.4, 0, 1);
    zCap.classList.toggle("light", e > .55);
  }

  /* ---------- intro parallax image ---------- */
  var stImg = $(".st__side img");

  /* ---------- horizontal categories ---------- */
  var hs = $(".hs"), hTrack = hs && $(".hs__track", hs), hBar = hs && $(".hs__bar", hs), hCnt = hs && $(".hs__cnt", hs), hMax = 0;
  function sizeHS() {
    if (!hs) return;
    if (vw < 820) { hs.style.height = ""; hMax = 0; return; }
    hMax = hTrack.scrollWidth - vw; hs.style.height = (hMax + vh) + "px";
  }
  function hsFrame() {
    if (!hs || !hMax) return;
    var r = hs.getBoundingClientRect(); if (r.bottom < 0 || r.top > vh) return;
    var p = clamp(-r.top / (r.height - vh), 0, 1);
    hTrack.style.transform = "translate3d(" + (-p * hMax) + "px,0,0)";
    hBar.style.setProperty("--hp", p);
    var n = $$(".hp", hTrack).length; hCnt.textContent = String(Math.min(n, Math.floor(p * n) + 1)).padStart(2, "0") + " / " + String(n).padStart(2, "0");
  }

  /* ---------- contact sheet loupe ---------- */
  var lp = $(".loupe"), lOn = false, lx = 0, ly = 0, lr = null, lZ = 2.6;
  if (lp && fine) {
    $$(".fr").forEach(function (f) {
      f.addEventListener("mouseenter", function () { lp.style.backgroundImage = "url(" + f.dataset.full + ")"; lr = f; lp.classList.add("on"); lOn = true; });
      f.addEventListener("mouseleave", function () { lp.classList.remove("on"); lOn = false; });
      f.addEventListener("mousemove", function (e) { lx = e.clientX; ly = e.clientY; });
    });
  }
  function loupeFrame() {
    if (!lOn || !lr) return;
    var r = lr.getBoundingClientRect(), img = lr.querySelector("img");
    // object-fit cover: rendered image size = frame size scaled to cover
    var iw = img.naturalWidth || 3, ih = img.naturalHeight || 2, s = Math.max(r.width / iw, r.height / ih), rw = iw * s, rh = ih * s;
    var ox = (rw - r.width) / 2, oy = (rh - r.height) / 2, px = lx - r.left + ox, py = ly - r.top + oy;
    lp.style.left = lx + "px"; lp.style.top = ly + "px";
    lp.style.backgroundSize = rw * lZ + "px " + rh * lZ + "px";
    lp.style.backgroundPosition = (-px * lZ + 115) + "px " + (-py * lZ + 115) + "px";
  }

  /* ---------- films player ---------- */
  var fl = $(".fl");
  if (fl) {
    var fv = $(".fl__pl video", fl), fimg = $(".fl__pl img", fl), fbtn = $(".fl__btn", fl), fcap = $(".fl__cap span", fl), fits = $$(".fl__it", fl), fVis = false;
    var setFilm = function (it) {
      fits.forEach(function (x) { x.classList.toggle("on", x === it); });
      fimg.src = it.dataset.poster; fv.classList.remove("on");
      fv.src = it.dataset.src; fv.load();
      fv.oncanplay = function () { fv.classList.add("on"); };
      if (fVis) play(fv);
      fbtn.dataset.play = it.dataset.src; fbtn.dataset.title = it.dataset.title; fbtn.dataset.poster = it.dataset.poster;
      fcap.textContent = it.dataset.title;
    };
    fits.forEach(function (it) {
      it.addEventListener("mouseenter", function () { if (fine && !it.classList.contains("on")) setFilm(it); });
      it.addEventListener("click", function () { if (!it.classList.contains("on")) setFilm(it); else openVM(it.dataset.src, it.dataset.title, it.dataset.poster); });
    });
    new IntersectionObserver(function (es) { fVis = es[0].isIntersecting; if (fVis) { if (!fv.getAttribute("src")) setFilm(fits[0]); else play(fv); } else fv.pause(); }, { threshold: .2 }).observe($(".fl__pl", fl));
  }

  /* ---------- reels hover play ---------- */
  $$(".rc2").forEach(function (r) {
    var v = $("video", r); if (!v) return;
    r.addEventListener("mouseenter", function () { if (!v.getAttribute("src")) v.src = v.dataset.src; r.classList.add("play"); play(v); });
    r.addEventListener("mouseleave", function () { r.classList.remove("play"); v.pause(); });
  });
  if (!fine) {
    var rio = new IntersectionObserver(function (es) { es.forEach(function (e) { var r = e.target, v = $("video", r); if (!v) return; if (e.isIntersecting) { if (!v.getAttribute("src")) v.src = v.dataset.src; r.classList.add("play"); play(v); } else { v.pause(); } }); }, { threshold: .6 });
    $$(".rc2").forEach(function (r) { rio.observe(r); });
  }

  /* ---------- behind-the-lens viewfinders ---------- */
  var vfs = $$(".vf"), vfOn = [];
  if (vfs.length) {
    var vio2 = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        var v = $("video", e.target);
        if (e.isIntersecting) { if (!v.getAttribute("src")) v.src = v.dataset.src; play(v); if (vfOn.indexOf(e.target) < 0) vfOn.push(e.target); }
        else { v.pause(); vfOn = vfOn.filter(function (x) { return x !== e.target; }); }
      });
    }, { threshold: .35 });
    vfs.forEach(function (f) {
      vio2.observe(f);
      f.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); f.click(); } });
    });
  }
  var pad = function (n) { return (n < 10 ? "0" : "") + n; };
  function vfFrame() {
    for (var i = 0; i < vfOn.length; i++) {
      var v = $("video", vfOn[i]), t = v.currentTime || 0, tc = $(".vf__tc", vfOn[i]);
      tc.textContent = "00:" + pad(Math.floor(t / 60)) + ":" + pad(Math.floor(t % 60)) + ":" + pad(Math.floor((t % 1) * 25));
    }
  }

  /* ---------- landscape parallax ---------- */
  var ls = $(".ls"), lsCols = ls ? $$(".ls__col", ls) : [];
  function lsFrame() {
    if (!ls) return;
    var r = ls.getBoundingClientRect(); if (r.bottom < 0 || r.top > vh) return;
    var p = (vh - r.top) / (r.height + vh) - .5;
    lsCols.forEach(function (c, i) { var s = [-.18, .14, -.28][i] || 0; c.style.transform = "translate3d(0," + (p * s * r.height) + "px,0)"; });
  }

  /* ---------- films page floating preview ---------- */
  var fpv = $(".fpv"), fx = 0, fy = 0, ftx = 0, fty = 0;
  if (fpv && fine) {
    var fpvV = $("video", fpv);
    $$(".frow").forEach(function (r) {
      r.addEventListener("mouseenter", function () { fpvV.src = r.dataset.pv; play(fpvV); fpv.classList.add("on"); });
      r.addEventListener("mouseleave", function () { fpv.classList.remove("on"); fpvV.pause(); });
    });
    addEventListener("mousemove", function (e) { ftx = e.clientX; fty = e.clientY; });
  }

  /* ---------- main loop ---------- */
  var lastY = scrollY;
  function frame() {
    var y = scrollY, dy = y - lastY; lastY = y;
    if (hd) { if (y > vh * 2.6 && dy > 4) hd.classList.add("hide"); else if (dy < -4 || y < 100) hd.classList.remove("hide"); }
    if (cur && fine) { cx = lerp(cx, kx, .2); cy = lerp(cy, ky, .2); cur.style.transform = "translate3d(" + cx + "px," + cy + "px,0)"; }
    heroFrame(); hsFrame(); loupeFrame(); lsFrame(); vfFrame();
    if (stImg) { var sr = stImg.parentNode.getBoundingClientRect(); if (sr.bottom > 0 && sr.top < vh) stImg.style.setProperty("--py", ((sr.top + sr.height / 2 - vh / 2) * -.08) + "px"); }
    if (fpv && fine) { fx = lerp(fx, ftx, .12); fy = lerp(fy, fty, .12); fpv.style.transform = "translate3d(" + (fx + 24) + "px," + (fy - 120) + "px,0) rotate(" + clamp((ftx - fx) * .05, -6, 6) + "deg)"; }
    requestAnimationFrame(frame);
  }
  addEventListener("resize", function () { vw = innerWidth; vh = innerHeight; sizeHS(); });
  addEventListener("load", sizeHS);
  sizeHS(); requestAnimationFrame(frame);

  /* ---------- video modal ---------- */
  var vm = $(".vm"), vmS = vm && $(".vm__st", vm), vmT = vm && $("h3", vm), vmV = null;
  function openVM(src, title, poster) {
    if (!vm) return;
    vmV = document.createElement("video"); vmV.src = src; vmV.poster = poster || ""; vmV.controls = true; vmV.autoplay = true; vmV.playsInline = true; vmV.setAttribute("playsinline", "");
    vmS.innerHTML = ""; vmS.appendChild(vmV); vmT.textContent = title || ""; vm.classList.add("open"); vm.setAttribute("aria-hidden", "false"); html.style.overflow = "hidden"; play(vmV);
    var fvid = $(".fl__pl video"); if (fvid) fvid.pause(); $$(".vf video").forEach(function (x) { x.pause(); });
  }
  function closeVM() { if (!vm) return; vm.classList.remove("open"); vm.setAttribute("aria-hidden", "true"); html.style.overflow = ""; vfOn.forEach(function (f) { play($("video", f)); }); if (vmV) { vmV.pause(); vmV.removeAttribute("src"); vmV.load(); } vmS.innerHTML = ""; }
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-play]");
    if (t && !t.classList.contains("fl__it")) { e.preventDefault(); openVM(t.dataset.play, t.dataset.title, t.dataset.poster); return; }
    if (vm && (e.target.closest(".vm .x") || e.target === vmS)) closeVM();
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeVM(); });

  /* ---------- enquiry form ---------- */
  var form = $(".form");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var f = new FormData(form), m = ["Hi UniqueCreation, I'd like to enquire about photography."];
    ["name:Name", "type:Looking for", "date:Date", "place:Venue"].forEach(function (k) { var a = k.split(":"); if (f.get(a[0])) m.push(a[1] + ": " + f.get(a[0])); });
    if (f.get("msg")) m.push(f.get("msg"));
    open("https://wa.me/" + D.contact.whatsapp + "?text=" + encodeURIComponent(m.join("\n")), "_blank", "noopener");
  });

  /* ---------- gallery (justified rows) ---------- */
  var jg = $("#jg");
  if (jg) {
    var keys = Object.keys(D.albums), tabs = $(".tabs"), more = $("#more"), PER = 30, cur2 = "all", shown = 0, list = [], all = [];
    var idx = {}; keys.forEach(function (k) { idx[k] = 0; });
    var total = keys.reduce(function (s, k) { return s + D.albums[k].items.length; }, 0);
    for (var n = 0; all.length < total && n < 5000; n++) { var k = keys[n % keys.length], a = D.albums[k].items; if (idx[k] < a.length) { var it = a[idx[k]++]; all.push({ k: k, f: it[0], w: it[1], h: it[2] }); } }
    var tab = function (key, label, cnt) { var b = document.createElement("button"); b.type = "button"; b.dataset.k = key; b.setAttribute("aria-pressed", "false"); b.innerHTML = label + "<sup>" + cnt + "</sup>"; tabs.appendChild(b); };
    tab("all", "All work", total); keys.forEach(function (k) { tab(k, D.albums[k].title, D.albums[k].items.length); });
    var rowH = function () { return vw < 600 ? 150 : vw < 1000 ? 220 : 290; };
    var add = function (from, to) {
      var f = document.createDocumentFragment(), h = rowH();
      list.slice(from, to).forEach(function (it, i) {
        var r = it.w / it.h, el = document.createElement("a");
        el.href = "assets/img/" + it.f + ".webp"; el.dataset.i = from + i; el.dataset.cursor = "View";
        el.style.flexGrow = r * 100; el.style.width = (r * h) + "px"; el.style.aspectRatio = r; el.style.animationDelay = Math.min(i, 14) * .035 + "s";
        el.innerHTML = '<img src="assets/img/' + it.f + '-t.webp" alt="' + D.albums[it.k].title + ' photograph by UniqueCreation" loading="lazy" decoding="async"><i></i>';
        f.appendChild(el);
      });
      jg.appendChild(f);
    };
    var draw = function (reset) {
      if (reset) { jg.innerHTML = ""; shown = 0; list = cur2 === "all" ? all : D.albums[cur2].items.map(function (it) { return { k: cur2, f: it[0], w: it[1], h: it[2] }; }); }
      var to = Math.min(list.length, shown + PER); add(shown, to); shown = to; more.hidden = shown >= list.length;
    };
    var setTab = function (k, push) {
      cur2 = D.albums[k] ? k : "all";
      $$("button", tabs).forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.k === cur2); });
      var t = cur2 === "all" ? "The <em>portfolio</em>" : D.albums[cur2].title.replace(/(\S+)$/, "<em>$1</em>");
      $("#gT").innerHTML = t; $("#gS").textContent = cur2 === "all" ? "Every category, mixed together. Choose one to go deeper." : D.albums[cur2].blurb;
      if (push) { var u = new URL(location.href); cur2 === "all" ? u.searchParams.delete("a") : u.searchParams.set("a", cur2); history.replaceState(null, "", u); }
      draw(true);
    };
    tabs.addEventListener("click", function (e) { var b = e.target.closest("button"); if (b) { setTab(b.dataset.k, true); var top = jg.getBoundingClientRect().top + scrollY - 140; if (scrollY > top) scrollTo({ top: top, behavior: "smooth" }); } });
    more.addEventListener("click", function () { draw(false); });
    var rt; addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(function () { var h = rowH(); $$("a", jg).forEach(function (a, i) { var it = list[+a.dataset.i]; a.style.width = (it.w / it.h * h) + "px"; }); }, 150); });
    setTab(new URL(location.href).searchParams.get("a") || "all", false);

    var lb = $("#lb"), lbI = $("img", lb), lbC = $(".lb__bt", lb), lbT = $("h3", lb), li = 0;
    var show = function (i) { li = (i + list.length) % list.length; lbI.style.opacity = 0; var im = new Image(); im.onload = function () { lbI.src = im.src; lbI.style.opacity = 1; }; im.src = "assets/img/" + list[li].f + ".webp"; lbC.textContent = String(li + 1).padStart(2, "0") + " — " + String(list.length).padStart(2, "0"); lbT.textContent = D.albums[list[li].k].title; };
    var openLB = function (i) { show(i); lb.classList.add("open"); lb.setAttribute("aria-hidden", "false"); html.style.overflow = "hidden"; };
    var closeLB = function () { lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); html.style.overflow = ""; };
    jg.addEventListener("click", function (e) { var a = e.target.closest("a"); if (a) { e.preventDefault(); openLB(+a.dataset.i); } });
    $(".x", lb).addEventListener("click", closeLB);
    $(".lb__nv--p", lb).addEventListener("click", function () { show(li - 1); });
    $(".lb__nv--n", lb).addEventListener("click", function () { show(li + 1); });
    document.addEventListener("keydown", function (e) { if (!lb.classList.contains("open")) return; if (e.key === "Escape") closeLB(); if (e.key === "ArrowLeft") show(li - 1); if (e.key === "ArrowRight") show(li + 1); });
    var sx = null; lb.addEventListener("touchstart", function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) { if (sx === null) return; var d = e.changedTouches[0].clientX - sx; if (Math.abs(d) > 50) show(li + (d < 0 ? 1 : -1)); sx = null; }, { passive: true });
  }
})();
