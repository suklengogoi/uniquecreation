"""UniqueCreation — Design C (cinematic noir). Builds pages + js/data.js.  Run: python3 build.py"""
import json, os
R = os.path.dirname(os.path.abspath(__file__)); os.chdir(R)
IMG = json.load(open("imgdata.json"))
V = "?v=1"
PH1, PH2 = "8486339975", "7002078910"
WA = "https://wa.me/91%s?text=Hi%%20UniqueCreation%%2C%%20I%%27d%%20like%%20to%%20enquire%%20about%%20photography." % PH1
IG1, IG2 = "https://www.instagram.com/uniquecreationphotography/", "https://www.instagram.com/pinkuuddip/"
SPRITE = open("src/sprite.html").read().strip()
ORDER = ["bridal", "celebration", "couples", "fashion", "family", "bihu", "festival", "scenery"]
BLURB = {
 "bridal": "Assamese brides in silk, gold and quiet window light.",
 "celebration": "Haldi, sangeet and the loud, joyful hours around the wedding.",
 "couples": "Pre-wedding, engagement and candid days for two people in love.",
 "fashion": "Gowns, shadows and colour. Portrait and fashion shoots with attitude.",
 "family": "Maternity, newborns and the softest first frames.",
 "bihu": "Bihu, rituals and Assamese culture, photographed with pride.",
 "festival": "Holi in full colour: crowds, masks, drums and faces.",
 "scenery": "Mountains, mist, monuments and skies from the road.",
}
F = {it["f"]: dict(it, k=k) for k, a in IMG.items() for it in a["items"]}
T = lambda k: IMG[k]["title"]
def em_last(t, cls="gold"):
    p = t.rsplit(" ", 1); return f'{p[0]} <em class="{cls}">{p[1]}</em>' if len(p) > 1 else f'<em class="{cls}">{t}</em>'
ICO = lambda i: f'<svg aria-hidden="true"><use href="#i-{i}"/></svg>'
def btn(label, href=WA, cls="btn", ext=True, icon="wa", cur=None):
    t = ' target="_blank" rel="noopener"' if ext else ""
    c = f' data-cursor="{cur}"' if cur else ""
    return f'<a class="{cls}" href="{href}"{t}{c}>{ICO(icon) if icon else ""}<span>{label}</span></a>'

FILMS = [("film1", "Haldi & Sangeet Highlights", "Wedding film"), ("film8", "Bridal Highlights", "Wedding film"),
 ("film2", "An Assamese Pre-wedding Story", "Pre-wedding"), ("film3", "Cinematic Pre-wedding Teaser", "Pre-wedding"),
 ("film6", "Wedding Night & Baraat", "Wedding film"), ("film7", "Ceremony & Rituals", "Wedding film"),
 ("film4", "Hills & Valleys, Pre-wedding", "Pre-wedding"), ("film5", "Pre-wedding on the Ridge", "Pre-wedding"),
 ("film10", "The Wedding Day", "Wedding film"), ("film9", "A First Birthday Story", "Family")]
REELS = [("reel1", "Fashion reel"), ("reel3", "Bridal reel"), ("reel2", "Gown shoot")]
BTS = [("bts1", "Fashion shoot", "fashion", ["fashion-03", "fashion-07", "fashion-10"], "Fashion &amp; Portraits",
        "Studio lights, styling and direction on set. What you take home: edited frames ready for print and Instagram.", "BTS vs output"),
       ("bts2", "Newborn shoot", "family", ["family-20", "family-18", "family-22"], "Maternity &amp; Newborn",
        "Gentle light, props and a lot of patience around a sleeping baby. What you take home: soft, timeless first portraits.", "Setup to final frame")]

data = {"contact": {"whatsapp": "91" + PH1, "phones": [PH1, PH2], "instagram": IG1, "instagram2": IG2},
 "albums": {k: {"title": T(k), "blurb": BLURB[k], "items": [[i["f"], i["w"], i["h"]] for i in IMG[k]["items"]]} for k in ORDER},
 "films": [{"id": a, "title": b, "tag": c} for a, b, c in FILMS], "reels": [{"id": a, "title": b} for a, b in REELS]}
open("js/data.js", "w").write("/* UniqueCreation — site content (Design C). Edit albums, films, reels and contact details here. */\nwindow.UC = " + json.dumps(data, indent=1) + ";\n")

NAV = [("index.html#chapters", "Chapters"), ("films.html", "Films"), ("index.html#bts", "Behind the lens"), ("gallery.html", "Collection"), ("index.html#contact", "Contact")]

def head(title, desc, page, loader=False):
    pre = "<script>try{if(!sessionStorage.getItem('ucc'))document.documentElement.classList.add('js-ld')}catch(e){}</script>" if loader else ""
    iris = "".join(f'<path d="M50 50 L{50+44*__import__("math").cos(a)} {50+44*__import__("math").sin(a)} A44 44 0 0 1 {50+44*__import__("math").cos(a+1.05)} {50+44*__import__("math").sin(a+1.05)}" transform="rotate(18 50 50)"/>' for a in [i*1.0472 for i in range(6)])
    ldr = f'<div class="ld" aria-hidden="true"><div class="ld__in"><svg class="ld__iris" viewBox="0 0 100 100"><circle cx="50" cy="50" r="46" fill="none" stroke="currentColor" stroke-width="1"/>{iris}<circle cx="50" cy="50" r="13" fill="none" stroke="currentColor" stroke-width="1.2"/></svg><p class="ld__n">Unique<em class="gold">Creation</em></p><span class="ld__c">00 %</span></div></div>' if loader else ""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0c0a08">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="assets/brand/og-image.jpg"><meta property="og:type" content="website">
<link rel="icon" href="assets/brand/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/corm.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="css/style.css{V}">
{pre}
</head>
<body data-page="{page}" id="top">
{SPRITE}
{ldr}
<a class="sr-only" href="#main">Skip to content</a>
<div class="cur" aria-hidden="true"><div class="cur__r"><span></span></div><div class="cur__d"></div></div>
<header class="hd">
  <a class="logo" href="index.html" aria-label="UniqueCreation, home"><i>Uc</i><span>Unique<em>Creation</em></span></a>
  <nav aria-label="Main">{"".join(f'<a href="{h}">{t}</a>' for h, t in NAV)}</nav>
  {btn("Book a date", cls="btn hd__cta", icon="")}
  <button class="mb" type="button" aria-expanded="false" aria-controls="mn">Menu<i></i></button>
</header>
<div class="mn" id="mn" aria-hidden="true">
  <div class="mn__t"><span class="logo"><i>Uc</i><span>Unique<em>Creation</em></span></span><button class="x" type="button" data-close aria-label="Close menu">{ICO("close")}</button></div>
  <nav aria-label="Mobile">{"".join(f'<a href="{h}"><small>0{i+1}</small>{t}</a>' for i, (h, t) in enumerate(NAV))}</nav>
  <div class="mn__f"><span class="eyebrow">Call or WhatsApp</span><a href="tel:+91{PH1}">{PH1[:5]} {PH1[5:]}</a><a href="tel:+91{PH2}">{PH2[:5]} {PH2[5:]}</a></div>
</div>
<main id="main">
'''

FOOT = f'''</main>
<footer class="ft">
  <div class="wrap">
    <p class="ft__big" aria-hidden="true"><span>Unique</span><em class="gold">Creation</em></p>
    <p class="ft__tag">We care for your emotions, we click for memories.</p>
    <div class="ft__row">
      <span>&copy; <span data-year>2026</span> UniqueCreation &middot; Uddip Phukan &middot; {PH1} &middot; {PH2}</span>
      <nav aria-label="Footer"><a href="gallery.html">Collection</a><a href="films.html">Films</a><a href="{IG1}" target="_blank" rel="noopener">Instagram</a><a href="{IG2}" target="_blank" rel="noopener">@pinkuuddip</a><a href="#top" data-top>Top &uarr;</a></nav>
    </div>
  </div>
</footer>
<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp" data-cursor="Chat">{ICO("wa")}</a>
'''
LB = f'''<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Photo viewer" aria-hidden="true"><div class="lb__top"><h3></h3><button class="x" type="button" aria-label="Close">{ICO("close")}</button></div><div class="lb__st"><button class="x lb__nv lb__nv--p" type="button" aria-label="Previous">{ICO("left")}</button><img alt="" src=""><button class="x lb__nv lb__nv--n" type="button" aria-label="Next">{ICO("right")}</button></div><div class="lb__bt"></div></div>
'''
VM = f'''<div class="vm" role="dialog" aria-modal="true" aria-label="Video player" aria-hidden="true"><div class="vm__top"><h3></h3><button class="x" type="button" aria-label="Close video">{ICO("close")}</button></div><div class="vm__st"></div></div>
'''
TAIL = f'''<script src="js/data.js{V}"></script>
<script src="js/main.js{V}"></script>
</body>
</html>
'''
def lines(*ls):
    return "".join(f'<span class="ln"><span>{l}</span></span>' for l in ls)

# ---------- shared blocks ----------
def now_showing(films, head_html):
    ths = "".join(f'<button class="th" type="button" data-src="assets/video/{f}.mp4" data-title="{t}" data-tag="{g}" data-poster="assets/video/{f}.jpg" data-cursor="Play"><span class="th__m"><img src="assets/video/{f}.jpg" alt="" loading="lazy"><span class="th__p"></span></span><span class="th__t"><b>{i+1:02d}</b>{t}</span></button>' for i, (f, t, g) in enumerate(films))
    f0 = films[0]
    pt = '' if head_html else ' style="padding-top:clamp(40px,5vw,70px)"'
    return f'''<section class="ns" id="films"{pt}><div class="wrap">
  {head_html}
  <div class="screen rv">
    <img src="assets/video/{f0[0]}.jpg" alt="" loading="lazy"><video muted loop playsinline preload="none"></video>
    <span class="screen__sh"></span><span class="screen__live"><i></i>Now showing</span>
    <div class="screen__in"><span class="eyebrow screen__g">{f0[2]}</span><h3 class="screen__t">{f0[1]}</h3><a class="btn" href="#" data-play="assets/video/{f0[0]}.mp4" data-title="{f0[1]}" data-poster="assets/video/{f0[0]}.jpg">{ICO("play")}<span>Play with sound</span></a></div>
  </div>
  <div class="strip">{ths}</div>
</div></section>
'''

def bts_section():
    cases = ""
    ring = "Behind the scenes &#183; UniqueCreation &#183; Behind the scenes &#183; UniqueCreation &#183; "
    for n, (vid, name, alb, imgs, atitle, desc, tag) in enumerate(BTS):
        res = "".join(f'<img src="assets/img/{f}-t.webp" alt="{atitle} by UniqueCreation" loading="lazy">' for f in imgs)
        cases += f'''
  <article class="case{' case--r' if n % 2 else ''}">
    <div class="orb rv" role="button" tabindex="0" data-play="assets/video/{vid}.mp4" data-title="Behind the lens: {name}" data-poster="assets/video/{vid}.jpg" data-cursor="Sound" aria-label="Play behind the scenes video: {name}">
      <svg class="orb__ring" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="or{n}" d="M100 100m-92 0a92 92 0 1 1 184 0a92 92 0 1 1-184 0"/></defs><text><textPath href="#or{n}" textLength="572" lengthAdjust="spacing">{ring}</textPath></text></svg>
      <div class="orb__v"><video data-src="assets/video/{vid}.mp4" poster="assets/video/{vid}.jpg" muted loop playsinline preload="none"></video><span class="orb__rec"><i></i>REC</span><span class="orb__tc">00:00:00:00</span><span class="orb__pl">Watch<br>with sound</span></div>
    </div>
    <div class="case__ar" aria-hidden="true"><svg viewBox="0 0 160 60"><path d="M4 40C40 6 96 6 150 30"/><path d="M138 18l13 12-17 6"/></svg><em>becomes</em></div>
    <div class="case__res rv" style="--d:.15s">
      <span class="case__tag">Case 0{n+1} &middot; {name} &middot; {tag}</span>
      <div class="fan">{res}</div>
      <h3>{em_last(atitle)}</h3><p>{desc}</p>
      {btn("See the full set", f"gallery.html?a={alb}", "lnk", False, "arrow")}
    </div>
  </article>'''
    return f'''<section class="bt" id="bts"><div class="wrap">
  <div class="sh"><div><span class="eyebrow rv">Behind the lens</span><h2 class="disp" data-lines style="margin-top:22px">{lines("See how the", '<em class="gold">magic</em> is made')}</h2></div>
  <div class="rv"><p>Every shoot is planned, lit and directed. This is what a session looks like on the day, and what you take home after. Tap a video for sound.</p>
  <ul class="bt__inc"><li>Light set-up on location</li><li>Posing &amp; direction</li><li>Edited final photographs</li><li>Reels &amp; highlight films</li></ul></div></div>{cases}
</div></section>
'''

def reel(f, t):
    return f'<button class="rc" type="button" data-play="assets/video/{f}.mp4" data-title="{t}" data-poster="assets/video/{f}.jpg" data-cursor="Play" aria-label="Play {t}"><img src="assets/video/{f}.jpg" alt="" loading="lazy"><video data-src="assets/video/{f}-pv.mp4" muted loop playsinline preload="none"></video><span class="rc__c"><span>{t}</span>{ICO("play")}</span></button>'

REELS_SEC = f'''<section class="rl" id="reels"><div class="wrap">
  <div class="sh"><div><span class="eyebrow rv">Reels</span><h2 class="disp" data-lines style="margin-top:22px">{lines('Made for the <em class="gold">feed</em>')}</h2></div><p class="rv">Short cuts from real shoots, made to be shared. Hover to play, tap for sound.</p></div></div>
  <div class="rl__g">{"".join(reel(f, t) for f, t in REELS)}</div>
</section>
'''

# ---------- index ----------
HERO = [("couples-55", "Pre-wedding"), ("celebration-03", "Haldi &amp; Sangeet"), ("couples-59", "Pre-wedding"), ("couples-53", "Engagement"), ("bihu-14", "Rituals"), ("couples-04", "Candid")]
slides = "".join(f'<div class="sl" data-label="{lab}"><img class="sl__b" src="assets/img/{f}.webp" alt="" {"fetchpriority=high" if i == 0 else "loading=lazy"}><div class="sl__c"><img src="assets/img/{f}.webp" alt="" {"" if i == 0 else "loading=lazy"}></div></div>' for i, (f, lab) in enumerate(HERO))
def letters(w, k0):
    return "".join(f'<i style="--k:{k0+i}">{c}</i>' for i, c in enumerate(w))
COVER = {"bridal": "bridal-02", "celebration": "celebration-04", "couples": "couples-18", "fashion": "fashion-07", "family": "family-18", "bihu": "bihu-08", "festival": "festival-02", "scenery": "scenery-11"}
cards = ""
for i, k in enumerate(ORDER):
    items = [x["f"] for x in IMG[k]["items"] if x["f"] != COVER[k]]
    th = "".join(f'<img src="assets/img/{f}-t.webp" alt="" loading="lazy">' for f in (items[2], items[5], items[8]))
    cards += f'''<a class="card" href="gallery.html?a={k}" style="--i:{i}" data-cursor="Open">
      <span class="card__m"><img src="assets/img/{COVER[k]}.webp" alt="{T(k)} by UniqueCreation" loading="lazy"><span class="card__no">Chapter {i+1:02d}</span></span>
      <span class="card__b"><span><span class="eyebrow">{len(IMG[k]["items"])} frames</span><h3 style="margin-top:20px">{em_last(T(k))}</h3></span><p>{BLURB[k]}</p><span class="card__th">{th}</span><span class="card__f"><span>No. {i+1:02d} / {len(ORDER):02d}</span><span class="lnk">Open chapter{ICO("arrow")}</span></span></span>
    </a>'''
WALL = ["bridal-01", "couples-12", "fashion-04", "bihu-02", "festival-05", "family-04", "scenery-14", "celebration-08", "couples-20", "bridal-12", "fashion-13", "festival-09", "bihu-10", "couples-26", "family-11", "scenery-16", "celebration-10", "bridal-19", "couples-34", "fashion-16", "festival-13", "family-21", "bihu-12", "scenery-20", "couples-40", "bridal-07", "fashion-01", "festival-11", "couples-22", "family-07", "bihu-05", "scenery-18", "couples-15", "bridal-15", "celebration-09", "festival-15"]
wl = json.dumps([{"f": f, "k": F[f]["k"]} for f in WALL]).replace('"', "&quot;")
LZ = ["scenery-08", "scenery-04", "scenery-05", "scenery-13", "scenery-11", "scenery-23", "scenery-12", "scenery-03", "scenery-09"]
pi = lambda f, r=False, d=".2s": f'<span class="pi{" pi--r" if r else ""}" style="--d:{d}"><img src="assets/img/{f}-t.webp" alt="" loading="lazy"></span>'

index = head("UniqueCreation by Uddip Phukan | Wedding, candid, films & landscape photography",
 "UniqueCreation by Uddip Phukan: wedding, pre-wedding, candid, newborn, fashion and landscape photography and films. We care for your emotions, we click for memories.", "home", loader=True) + f'''
<section class="hero" aria-label="Introduction">
  {slides}
  <div class="hero__v"></div>
  <div class="lens" aria-hidden="true"><b></b><i></i></div>
  <span class="hero__hint">Move to see it in colour</span>
  <div class="hero__in">
    <h1 class="hero__t" aria-label="UniqueCreation"><span>{letters("Unique", 0)}</span><span class="gold">{letters("Creation", 6)}</span></h1>
    <div class="hero__row">
      <p class="hero__tag">We care for your emotions, <em>we click for memories.</em></p>
      <div class="hero__cta">{btn("Check my date", cur=None)}<a class="btn btn--ghost" href="#chapters">Explore the work</a></div>
      <div class="hero__meta"><b>01 / 0{len(HERO)}</b><span class="hero__bar"><i></i></span><span class="hero__cat">{HERO[0][1]}</span></div>
    </div>
  </div>
</section>

<section class="iv" id="studio"><div class="wrap">
  <span class="eyebrow rv">The studio of Uddip Phukan</span>
  <p class="iv__p">We care for your {pi("bridal-02")} emotions, we click for {pi("family-18", True, ".35s")} memories. Weddings, candid days {pi("couples-04", False, ".5s")}, newborns, <em>Bihu, Holi</em> {pi("festival-02", True, ".65s")} and the hills beyond {pi("scenery-11", False, ".8s")}.</p>
  <div class="iv__g">
    <p class="rv">UniqueCreation is a photography and films studio led by Uddip Phukan. Weddings are the heart of it, but the camera keeps going wherever there is a feeling worth keeping.</p>
    <p class="rv" style="--d:.1s">Every story is photographed and filmed with the same care: planned light, gentle direction and honest moments, delivered as photographs, films and reels.</p>
    <div class="rv" style="--d:.2s"><p class="iv__sig">Uddip Phukan<small>Photographer &amp; filmmaker</small></p><p style="margin-top:22px">{btn("@uniquecreationphotography", IG1, "lnk", True, "ig")}</p></div>
  </div>
</div></section>

<section class="ch" id="chapters"><div class="wrap">
  <div class="sh"><div><span class="eyebrow rv">Chapters</span><h2 class="disp" data-lines style="margin-top:22px">{lines("Eight ways to", 'tell a <em class="gold">story</em>')}</h2></div><p class="rv">Not only weddings. Each chapter is its own world. Scroll through, then open one to see the full set.</p></div>
  <div class="stack">{cards}</div>
</div></section>

<section class="wall" aria-label="Photo wall" data-list="{wl}">
  <div class="wall__o"><div><h2 class="disp">Wander the <em class="gold">wall</em></h2><p>{ICO("arrow")}Drag to explore &middot; click to view</p></div></div>
</section>

<section class="lz" aria-label="Landscapes">
  <div class="lz__s">
    <div class="lz__h"><span class="eyebrow">Beyond the wedding</span></div>
    <div class="lz__g">{"".join(f'<img src="assets/img/{f}{"" if j == 4 else "-t"}.webp" alt="Landscape by UniqueCreation" loading="lazy">' for j, f in enumerate(LZ))}</div>
    <div class="lz__o"><div><span class="eyebrow">Beyond the wedding</span><h2 class="disp" style="margin-top:20px">Mist, hills &amp; <em class="gold">monuments</em></h2><p>Uddip keeps shooting long after the last guest leaves: mountains, skies and old stone.</p>{btn("See landscapes", "gallery.html?a=scenery", "btn", False, "", "Open")}</div></div>
  </div>
</section>

''' + now_showing(FILMS[:8], f'<div class="sh"><div><span class="eyebrow rv">Films</span><h2 class="disp" data-lines style="margin-top:22px">{lines("Now", "<em class=\"gold\">showing</em>")}</h2></div><p class="rv">Wedding highlights and pre-wedding stories. Hover a title to preview it on the big screen, click for sound.</p></div>') + bts_section() + REELS_SEC + f'''
<section class="ct" id="contact"><div class="wrap">
  <span class="eyebrow rv">Contact</span>
  <h2 class="disp" data-lines style="margin-top:22px">{lines("Let&#8217;s make", '<em class="gold">memories</em>')}</h2>
  <div class="ct__g">
    <div class="ct__n rv">
      <span class="eyebrow">Call or WhatsApp</span>
      <a href="tel:+91{PH1}" data-cursor="Call">{PH1[:5]} {PH1[5:]}</a>
      <a href="tel:+91{PH2}" data-cursor="Call">{PH2[:5]} {PH2[5:]}</a>
      <span class="eyebrow">Instagram</span>
      <a class="sm" href="{IG1}" target="_blank" rel="noopener" data-cursor="Follow">@uniquecreationphotography</a>
      <a class="sm" href="{IG2}" target="_blank" rel="noopener" data-cursor="Follow">@pinkuuddip</a>
    </div>
    <form class="form rv" action="#" novalidate style="--d:.1s">
      <h3>Check your <em class="gold">date</em></h3>
      <div class="two"><div class="f"><label for="n">Your name</label><input id="n" name="name" autocomplete="name"></div><div class="f"><label for="d">Event date</label><input id="d" name="date" type="date"></div></div>
      <div class="two"><div class="f"><label for="t">Looking for</label><select id="t" name="type"><option>Wedding</option><option>Pre-wedding</option><option>Engagement</option><option>Candid / portraits</option><option>Maternity or newborn</option><option>Fashion shoot</option><option>Films &amp; reels</option><option>Something else</option></select></div><div class="f"><label for="p">Venue / town</label><input id="p" name="place"></div></div>
      <div class="f"><label for="m">Anything else</label><textarea id="m" name="msg"></textarea></div>
      <div><button class="btn" type="submit">{ICO("wa")}<span>Send on WhatsApp</span></button></div>
      <small>Opens WhatsApp with your details filled in.</small>
    </form>
  </div>
</div></section>
''' + FOOT + LB + VM + TAIL
open("index.html", "w").write(index)

# ---------- gallery ----------
gal = head("The collection | UniqueCreation", "The UniqueCreation collection: weddings, bridal, pre-wedding, candid, newborn, fashion, Bihu, Holi and landscapes.", "gallery") + f'''
<section class="ph"><div class="wrap"><span class="eyebrow">The collection</span><h1 class="disp" id="gT" style="margin-top:22px">The <em class="gold">collection</em></h1><p id="gS"></p>
<div class="tabs" role="group" aria-label="Filter by chapter"></div></div></section>
<div class="wrap"><div class="mas" id="mas"></div><div class="more"><button class="btn btn--ghost" type="button" id="more">Show more</button></div></div>
<section class="cta2"><div class="wrap"><h2 class="disp">Like what you <em class="gold">see?</em></h2><div class="row">{btn("Check my date")}<a class="btn btn--ghost" href="films.html">Watch the films</a></div></div></section>
''' + FOOT + LB + TAIL
open("gallery.html", "w").write(gal)

# ---------- films ----------
films = head("Films & reels | UniqueCreation", "Wedding films, pre-wedding stories, behind the scenes and reels by UniqueCreation, Uddip Phukan.", "films") + f'''
<section class="ph" style="padding-bottom:0"><div class="wrap"><span class="eyebrow">Films</span><h1 class="disp" style="margin-top:22px">Films <em class="gold">&amp; reels</em></h1><p>Wedding highlights, pre-wedding stories, a look behind the lens and the reels in between.</p></div></section>
''' + now_showing(FILMS, "") + bts_section() + REELS_SEC + f'''
<section class="cta2"><div class="wrap"><h2 class="disp">Want a film like <em class="gold">this?</em></h2><div class="row">{btn("Check my date")}<a class="btn btn--ghost" href="gallery.html">See the collection</a></div></div></section>
''' + FOOT + VM + TAIL
open("films.html", "w").write(films)

nf = head("Page not found | UniqueCreation", "Page not found.", "404") + f'''
<section class="ph" style="min-height:80vh"><div class="wrap"><span class="eyebrow">404</span><h1 class="disp" style="margin-top:22px">Out of <em class="gold">frame</em></h1><p>This page wandered off. The pictures are this way.</p><p style="margin-top:34px">{btn("Back home", "index.html", "btn", False, "")}</p></div></section>
''' + FOOT + TAIL
open("404.html", "w").write(nf)
print("built")
