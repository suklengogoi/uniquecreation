"""UniqueCreation — Design B. Builds pages + js/data.js.  Run: python3 build.py"""
import json, os
R = os.path.dirname(os.path.abspath(__file__)); os.chdir(R)
IMG = json.load(open("imgdata.json"))
V = "?v=3"
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
F = {}
for k, a in IMG.items():
    for it in a["items"]: F[it["f"]] = it
def T(k): return IMG[k]["title"]
def em_last(t):
    p = t.rsplit(" ", 1); return f"{p[0]} <em>{p[1]}</em>" if len(p) > 1 else f"<em>{t}</em>"

FILMS = [("film1", "Haldi & Sangeet Highlights", "Wedding film"), ("film8", "Bridal Highlights", "Wedding film"),
 ("film2", "An Assamese Pre-wedding Story", "Pre-wedding"), ("film3", "Cinematic Pre-wedding Teaser", "Pre-wedding"),
 ("film6", "Wedding Night & Baraat", "Wedding film"), ("film7", "Ceremony & Rituals", "Wedding film"),
 ("film4", "Hills & Valleys, Pre-wedding", "Pre-wedding"), ("film5", "Pre-wedding on the Ridge", "Pre-wedding"),
 ("film10", "The Wedding Day", "Wedding film"), ("film9", "A First Birthday Story", "Family")]
REELS = [("reel1", "Fashion reel"), ("reel3", "Bridal reel"), ("reel2", "Gown shoot")]

data = {"contact": {"whatsapp": "91" + PH1, "phones": [PH1, PH2], "instagram": IG1, "instagram2": IG2},
 "albums": {k: {"title": T(k), "blurb": BLURB[k], "items": [[i["f"], i["w"], i["h"]] for i in IMG[k]["items"]]} for k in ORDER},
 "films": [{"id": a, "title": b, "tag": c} for a, b, c in FILMS], "reels": [{"id": a, "title": b} for a, b in REELS]}
open("js/data.js", "w").write("/* UniqueCreation — site content (Design B). Edit albums, films, reels and contact details here. */\nwindow.UC = " + json.dumps(data, indent=1) + ";\n")

NAV = [("index.html#work", "Work"), ("films.html", "Films"), ("index.html#bts", "Behind the lens"), ("gallery.html", "Portfolio"), ("index.html#contact", "Contact")]
ICO = lambda i: f'<svg aria-hidden="true"><use href="#i-{i}"/></svg>'

def head(title, desc, page, loader=False):
    pre = "<script>try{if(!sessionStorage.getItem('ucb'))document.documentElement.classList.add('js-ld')}catch(e){}</script>" if loader else ""
    ldr = '<div class="ld" aria-hidden="true"><p class="ld__n"><span>Unique</span><span>Creation</span></p><div class="ld__b"><span class="lbl">Weddings &middot; Candid &middot; Films &middot; Scenery</span><span class="ld__c">000</span></div><i class="ld__bar"></i></div>' if loader else ""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#f2ede4">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="assets/brand/og-image.jpg"><meta property="og:type" content="website">
<link rel="icon" href="assets/brand/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/bodoni.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="css/style.css{V}">
{pre}
</head>
<body data-page="{page}" id="top">
{SPRITE}
{ldr}
<a class="sr-only" href="#main">Skip to content</a>
<div class="cur" aria-hidden="true"><span></span></div>
<header class="hd">
  <nav class="hd__l" aria-label="Main">{"".join(f'<a href="{h}">{t}</a>' for h, t in NAV[:3])}</nav>
  <a class="logo" href="index.html" aria-label="UniqueCreation, home">Unique<em>Creation</em></a>
  <div class="hd__r"><a class="d" href="index.html#studio">Studio</a><a class="d" href="{WA}" target="_blank" rel="noopener">Enquire</a><button class="mbtn" type="button" aria-expanded="false" aria-controls="mn">Menu<i></i></button></div>
</header>
<div class="mn" id="mn" aria-hidden="true">
  <div class="mn__top"><span class="logo">Unique<em>Creation</em></span><button class="x" type="button" data-close aria-label="Close menu">{ICO("close")}</button></div>
  <nav aria-label="Mobile">{"".join(f'<a href="{h}"><small>0{i+1}</small>{t}</a>' for i, (h, t) in enumerate(NAV))}</nav>
  <div class="mn__f"><span class="lbl" style="color:var(--turmeric)">Call or WhatsApp</span><a href="tel:+91{PH1}">{PH1}</a><a href="tel:+91{PH2}">{PH2}</a></div>
</div>
<main id="main">
'''

FOOT = f'''</main>
<footer class="ft">
  <div class="wrap">
    <p class="ft__big" aria-hidden="true">Unique<em>Creation</em></p>
    <p class="ft__tag">We care for your emotions, we click for memories.</p>
    <div class="ft__row">
      <span>&copy; <span data-year>2026</span> UniqueCreation &middot; Uddip Phukan &middot; {PH1} &middot; {PH2}</span>
      <nav aria-label="Footer"><a href="gallery.html">Portfolio</a><a href="films.html">Films</a><a href="{IG1}" target="_blank" rel="noopener">Instagram</a><a href="{IG2}" target="_blank" rel="noopener">@pinkuuddip</a><a href="#top" data-top>Top &uarr;</a></nav>
    </div>
  </div>
</footer>
<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp" data-cursor="Chat">{ICO("wa")}</a>
'''
VM = f'''<div class="vm" role="dialog" aria-modal="true" aria-label="Video player" aria-hidden="true"><div class="vm__top"><h3></h3><button class="x" type="button" aria-label="Close video">{ICO("close")}</button></div><div class="vm__st"></div></div>
'''
TAIL = f'''<script src="js/data.js{V}"></script>
<script src="js/main.js{V}"></script>
</body>
</html>
'''
def btn(label, href=WA, cls="btn", ext=True, icon="wa"):
    t = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="{cls}" href="{href}"{t}>{ICO(icon) if icon else ""}<span>{label}</span></a>'

def reel(f, t):
    return f'''<button class="rc2" type="button" data-play="assets/video/{f}.mp4" data-title="{t}" data-poster="assets/video/{f}.jpg" data-cursor="Play" aria-label="Play {t}"><img src="assets/video/{f}.jpg" alt="" loading="lazy"><video data-src="assets/video/{f}-pv.mp4" muted loop playsinline preload="none"></video><span class="rc2__c"><span>{t}</span>{ICO("play")}</span></button>'''

import sys; sys.path.insert(0, "src")
from bts import bts_section
BTS_HTML = bts_section(ICO, btn)
# ---------------- index ----------------
HERO = [("bridal-02", "bridal"), ("couples-18", "couples"), ("bihu-08", "bihu"), ("fashion-07", "fashion"), ("festival-02", "festival"), ("family-18", "family"), ("couples-26", "couples"), ("scenery-11", "scenery")]
slides = "".join(f'<img src="assets/img/{f}.webp" alt="" data-w="{F[f]['w']}" data-h="{F[f]['h']}" data-label="{T(k)}" {"fetchpriority=high" if i == 0 else "loading=lazy"} decoding="async">' for i, (f, k) in enumerate(HERO))
COVER = {"bridal": "bridal-02", "celebration": "celebration-03", "couples": "couples-04", "fashion": "fashion-03", "family": "family-18", "bihu": "bihu-08", "festival": "festival-02", "scenery": "scenery-11"}
panels = "".join(f'''<a class="hp" href="gallery.html?a={k}" data-cursor="Open"><span class="hp__m"><img src="assets/img/{COVER[k]}-t.webp" alt="{T(k)} by UniqueCreation" loading="lazy"><span class="hp__n">No. 0{i+1}</span></span><span class="hp__t"><h3>{em_last(T(k))}</h3><span>{len(IMG[k]["items"])} PHOTOS</span></span></a>''' for i, k in enumerate(ORDER))
SHEET = ["couples-04", "celebration-06", "bihu-15", "scenery-13", "couples-11", "fashion-21", "celebration-01", "scenery-08", "bihu-17", "couples-07", "scenery-23", "celebration-12", "couples-01", "scenery-05", "fashion-18", "bihu-14", "couples-29", "scenery-03"]
MARK = {2: "circle", 7: "circle", 13: "circle", 10: "ok", 4: "ok"}
CIRC = '<svg class="fr__mark" viewBox="0 0 120 80" preserveAspectRatio="none" aria-hidden="true"><path d="M60 6C26 4 6 18 7 40c1 24 30 35 58 34 30-1 50-15 49-36C113 16 88 5 54 8"/></svg>'
alb = lambda f: f.split("-")[0]
fr = []
for n, f in enumerate(SHEET):
    m = MARK.get(n); extra = CIRC if m == "circle" else ('<span class="fr__ok">&#10003;</span>' if m == "ok" else "")
    fr.append(f'<a class="fr" href="gallery.html?a={alb(f)}" data-full="assets/img/{f}.webp" aria-label="{T(alb(f))}"><img src="assets/img/{f}-t.webp" alt="" loading="lazy">{extra}<span class="fr__no">&#9656; {n+12}{"A" if n % 2 else ""}</span></a>')
frames = "".join('<div class="strip"><div class="strip__in">' + "".join(fr[i:i + 6]) + "</div></div>" for i in range(0, len(fr), 6))
flist = "".join(f'<button class="fl__it{" on" if i == 0 else ""}" type="button" data-src="assets/video/{f}.mp4" data-title="{t}" data-poster="assets/video/{f}.jpg" data-cursor="Play"><b>0{i+1}</b><span>{t}</span><small>{g}</small></button>' for i, (f, t, g) in enumerate(FILMS[:6]))
cols = [["scenery-02", "scenery-16", "scenery-04"], ["scenery-11", "scenery-14", "scenery-08"], ["scenery-07", "scenery-18", "scenery-13"]]
lscols = "".join('<div class="ls__col">' + "".join(f'<img src="assets/img/{f}-t.webp" alt="Landscape by UniqueCreation" loading="lazy" width="{F[f]["w"]}" height="{F[f]["h"]}">' for f in c) + "</div>" for c in cols)

index = head("UniqueCreation by Uddip Phukan | Weddings, candid, films & landscapes",
 "UniqueCreation by Uddip Phukan: wedding, pre-wedding, candid, newborn, fashion and landscape photography and films. We care for your emotions, we click for memories.", "home", loader=True) + f'''
<section class="zh" aria-label="Introduction">
  <div class="zh__s">
    <div class="zh__f">{slides}<span class="zh__sh"></span></div>
    <h1 class="zh__t zh__t--1"><i><b>Unique</b></i></h1>
    <p class="zh__t zh__t--2" aria-hidden="true"><i><b>Creation</b></i></p>
    <div class="zh__msg"><span class="lbl">Uddip Phukan &middot; Photography &amp; films</span><p>We care for your emotions, <em>we click for memories.</em></p><div class="row">{btn("Check my date", cls="btn btn--light")}<a class="btn btn--line" href="gallery.html">See the portfolio</a></div></div>
    <div class="zh__cap"><span class="l lbl">Weddings &middot; Candid &middot; Films &middot; Scenery</span><span class="c"><b>No. 01 / 0{len(HERO)}</b>{T(HERO[0][1])}</span><span class="r lbl">Scroll<i></i></span></div>
  </div>
</section>

<section class="st" id="studio"><div class="wrap st__g">
  <span class="lbl lbl--soft rv">(The studio)</span>
  <p class="st__p" data-words>UniqueCreation is the studio of <em>Uddip Phukan.</em> Weddings are the heart of it, but the camera keeps going: candid moments, newborns, fashion, <em>Bihu, Holi</em> and the hills beyond.</p>
  <div class="st__side rv"><figure><img src="assets/img/couples-18-t.webp" alt="Couple under a terracotta arch, by UniqueCreation" loading="lazy"></figure><p>Every frame starts with a feeling. The job is making sure it lasts, in photographs and in film.</p>{btn("Follow on Instagram", IG1, "ulink", True, "")}</div>
</div></section>

<section class="hs" id="work" aria-label="Categories">
  <div class="hs__wrapi"><h2 class="h-xl">Eight ways to <em>tell</em> a story</h2></div>
  <div class="hs__s">
    <div class="hs__track">
      <div class="hs__intro" aria-hidden="false"><span class="lbl lbl--soft">(Work)</span><h2 class="h-xl">Eight ways to <em>tell</em> a story</h2><p>Not only weddings. Pick a chapter and step inside.</p>{btn("Full portfolio", "gallery.html", "ulink", False, "")}</div>
      {panels}
    </div>
    <div class="hs__bar"><i></i></div><span class="hs__cnt">01 / 08</span>
  </div>
</section>

<section class="cs" aria-label="Contact sheet"><div class="wrap">
  <div class="cs__h"><h2 class="h-xl" data-words>From the <em>contact</em> sheet</h2><p class="rv">Frames straight off the shoot, picks circled. Hover a frame to look closer, or open its album.</p></div>
  {frames}
  <div class="cs__f"><a class="btn" href="gallery.html" data-cursor="Open">{ICO("cam")}<span>Open the portfolio</span></a></div>
</div></section>
<div class="loupe" aria-hidden="true"></div>

<section class="fl" id="films"><div class="wrap">
  <span class="lbl" style="color:var(--turmeric)">(Films)</span>
  <h2 class="h-xl" data-words>Moving <em>pictures</em></h2>
  <div class="fl__g">
    <div class="fl__list">{flist}</div>
    <div class="fl__pl"><img src="assets/video/{FILMS[0][0]}.jpg" alt="" loading="lazy"><video muted loop playsinline preload="none"></video><button class="fl__btn" type="button" data-play="assets/video/{FILMS[0][0]}.mp4" data-title="{FILMS[0][1]}" data-poster="assets/video/{FILMS[0][0]}.jpg">Watch<br>with sound</button><div class="fl__cap"><span>{FILMS[0][1]}</span><b>&#9679; Preview</b></div></div>
  </div>
  <div class="fl__more">{btn("All films &amp; reels", "films.html", "ulink", False, "")}</div>
</div></section>

''' + BTS_HTML + f'''
<section class="rf" id="reels"><div class="wrap rf__h"><span class="lbl lbl--soft">(Reels)</span><h2 class="h-xl" data-words>Made for the <em>feed</em></h2><p class="rv">Short cuts from shoots. Hover to play, click for sound.</p></div>
  <div class="fan fan--3">{"".join(reel(f, t) for f, t in REELS)}</div>
  <div class="rf__f">{btn("Watch on Instagram", IG1, "ulink", True, "")}</div>
</section>

<section class="ls" aria-label="Landscapes">
  <div class="ls__cols">{lscols}</div>
  <div class="ls__txt"><div class="ls__card"><span class="lbl lbl--soft">(Beyond the wedding)</span><h2 class="h-xl">Mist, hills <em>&amp; monuments</em></h2><p>Uddip keeps shooting long after the last guest leaves: mountains, skies and old stone.</p>{btn("See landscapes", "gallery.html?a=scenery", "btn", False, "")}</div></div>
</section>

<section class="pr"><div class="wrap">
  <span class="lbl lbl--soft">(How it works)</span>
  <h2 class="h-xl" data-words>Simple from <em>hello</em> to album</h2>
  <div class="pr__g">
    <div class="pr__i rv"><b>i.</b><h3>Say hello</h3><p>Send your date and what you are planning on WhatsApp or call. We check availability and talk it through.</p></div>
    <div class="pr__i rv" style="--d:.1s"><b>ii.</b><h3>Plan the story</h3><p>Rituals, locations, timings and the people who matter. We plan the shots so you can enjoy the day.</p></div>
    <div class="pr__i rv" style="--d:.2s"><b>iii.</b><h3>Relive it</h3><p>Edited photographs, highlight films and reels, made to feel like the day did.</p></div>
  </div>
</div></section>

<section class="ct" id="contact"><div class="wrap">
  <span class="lbl lbl--soft">(Contact)</span>
  <h2 class="h-xl" data-words>Let&#8217;s make <em>memories</em></h2>
  <div class="ct__g">
    <div class="ct__nums">
      <span class="lbl lbl--soft">Call or WhatsApp</span>
      <a href="tel:+91{PH1}" data-cursor="Call">{PH1[:5]} {PH1[5:]}</a>
      <a href="tel:+91{PH2}" data-cursor="Call">{PH2[:5]} {PH2[5:]}</a>
      <span class="lbl lbl--soft">Instagram</span>
      <a href="{IG1}" target="_blank" rel="noopener" style="font-size:clamp(26px,2.8vw,42px)" data-cursor="Follow">@uniquecreationphotography</a>
      <a href="{IG2}" target="_blank" rel="noopener" style="font-size:clamp(26px,2.8vw,42px)" data-cursor="Follow">@pinkuuddip</a>
    </div>
    <form class="form rv" action="#" novalidate>
      <div class="two"><div class="f"><label for="n">Your name</label><input id="n" name="name" autocomplete="name"></div><div class="f"><label for="d">Event date</label><input id="d" name="date" type="date"></div></div>
      <div class="two"><div class="f"><label for="t">Looking for</label><select id="t" name="type"><option>Wedding</option><option>Pre-wedding</option><option>Engagement</option><option>Candid / portraits</option><option>Maternity or newborn</option><option>Fashion shoot</option><option>Films &amp; reels</option><option>Something else</option></select></div><div class="f"><label for="p">Venue / town</label><input id="p" name="place"></div></div>
      <div class="f"><label for="m">Anything else</label><textarea id="m" name="msg"></textarea></div>
      <div><button class="btn" type="submit" data-cursor="Send">{ICO("wa")}<span>Send on WhatsApp</span></button></div>
      <small>Opens WhatsApp with your details filled in.</small>
    </form>
  </div>
</div></section>
''' + FOOT + VM + TAIL
open("index.html", "w").write(index)

# ---------------- gallery ----------------
gal = head("Portfolio | UniqueCreation", "The UniqueCreation portfolio: weddings, bridal, pre-wedding, candid, newborn, fashion, Bihu, Holi and landscapes.", "gallery") + f'''
<section class="ph"><div class="wrap"><span class="lbl lbl--soft">(Portfolio)</span><h1 class="h-xl" id="gT">The <em>portfolio</em></h1><p id="gS"></p>
<div class="tabs" role="group" aria-label="Filter by category"></div></div></section>
<div class="wrap"><div class="jg" id="jg"></div><div class="more"><button class="btn" type="button" id="more">Show more</button></div></div>
<section class="ctaband"><div class="wrap"><h2 class="h-xl">Like what you <em>see?</em></h2><div class="row">{btn("Check my date")}<a class="btn btn--line" href="films.html">Watch the films</a></div></div></section>
''' + FOOT + f'''<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Photo viewer" aria-hidden="true"><div class="lb__top"><h3></h3><button class="x" type="button" aria-label="Close">{ICO("close")}</button></div><div class="lb__st"><button class="x lb__nv lb__nv--p" type="button" aria-label="Previous">{ICO("left")}</button><img alt="" src=""><button class="x lb__nv lb__nv--n" type="button" aria-label="Next">{ICO("right")}</button></div><div class="lb__bt"></div></div>
''' + TAIL
open("gallery.html", "w").write(gal)

# ---------------- films ----------------
rows = "".join(f'<button class="frow" type="button" data-play="assets/video/{f}.mp4" data-title="{t}" data-poster="assets/video/{f}.jpg" data-pv="assets/video/{f}-pv.mp4" data-cursor="Play"><b>{i+1:02d}</b><span>{t}</span><small>{g}</small><span class="th"><img src="assets/video/{f}.jpg" alt="" loading="lazy"></span></button>' for i, (f, t, g) in enumerate(FILMS))
films = head("Films & reels | UniqueCreation", "Wedding films, pre-wedding stories and reels by UniqueCreation, Uddip Phukan.", "films") + f'''
<section class="ph"><div class="wrap"><span class="lbl lbl--soft">(Films)</span><h1 class="h-xl">Films <em>&amp; reels</em></h1><p>Wedding highlights, pre-wedding stories and the reels in between. Click any title to watch.</p></div></section>
<section class="wrap"><div class="flist">{rows}</div></section>
''' + BTS_HTML + f'''
<section class="wrap" style="padding-top:clamp(60px,8vw,110px)"><h2 class="h-xl sub" id="reels" style="font-size:clamp(46px,7vw,110px)">The <em>reels</em></h2>
<div class="rgrid">{"".join(reel(f, t) for f, t in REELS)}</div></section>
<section class="ctaband"><div class="wrap"><h2 class="h-xl">Want a film like <em>this?</em></h2><div class="row">{btn("Check my date")}<a class="btn btn--line" href="gallery.html">See the portfolio</a></div></div></section>
<div class="fpv" aria-hidden="true"><video muted loop playsinline></video></div>
''' + FOOT + VM + TAIL
open("films.html", "w").write(films)

nf = head("Page not found | UniqueCreation", "Page not found.", "404") + f'''
<section class="ph" style="min-height:80vh"><div class="wrap"><span class="lbl lbl--soft">(404)</span><h1 class="h-xl">Out of <em>frame</em></h1><p>This page wandered off. The pictures are this way.</p><p style="margin-top:30px">{btn("Back home", "index.html", "btn", False, "")}</p></div></section>
''' + FOOT + TAIL
open("404.html", "w").write(nf)
print("built")
