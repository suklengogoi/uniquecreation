"""Builds the static pages + js/data.js for UniqueCreation.
Run:  python3 build.py   (needs imgdata.json beside it)"""
import json, os
R = os.path.dirname(os.path.abspath(__file__)); os.chdir(R)
IMG = json.load(open("imgdata.json"))
V = "?v=1"
PH1, PH2 = "8486339975", "7002078910"
WA = "https://wa.me/91%s?text=Hi%%20UniqueCreation%%2C%%20I%%27d%%20like%%20to%%20enquire%%20about%%20photography." % PH1
IG1 = "https://www.instagram.com/uniquecreationphotography/"
IG2 = "https://www.instagram.com/pinkuuddip/"
SPRITE = open("src/sprite.html").read().strip()

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
ORDER = ["bridal", "celebration", "couples", "fashion", "family", "bihu", "festival", "scenery"]
src = {}
for k, a in IMG.items():
    for it in a["items"]:
        src[it["src"]] = it["f"]
COVER = {"bridal": "2.2", "celebration": "1.3", "couples": "3.5", "fashion": "21.3", "family": "34.2", "bihu": "44.3", "festival": "46.2", "scenery": "48.5"}
RING = ["13.4", "2.2", "24.2", "44.3", "46.2", "27.1", "30.3", "21.3", "23.4", "28.1"]

FILMS = [
 ("film1", "Haldi & Sangeet Highlights", "Wedding film"),
 ("film8", "Bridal Highlights", "Wedding film"),
 ("film2", "An Assamese Pre-wedding Story", "Pre-wedding"),
 ("film3", "Cinematic Pre-wedding Teaser", "Pre-wedding"),
 ("film6", "Wedding Night & Baraat", "Wedding film"),
 ("film7", "Ceremony & Rituals", "Wedding film"),
 ("film4", "Hills & Valleys, Pre-wedding", "Pre-wedding"),
 ("film5", "Pre-wedding on the Ridge", "Pre-wedding"),
 ("film10", "The Wedding Day", "Wedding film"),
 ("film9", "A First Birthday Story", "Family"),
]
REELS = [
 ("reel3", "Bridal reel"),
 ("reel1", "Fashion reel"),
 ("reel2", "Gown shoot"),
 ("reel4", "Behind the scenes"),
 ("reel5", "Newborn shoot BTS"),
]

# ---- data.js
albums = {}
for k in ORDER:
    albums[k] = {"title": IMG[k]["title"], "blurb": BLURB[k], "items": [[i["f"], i["w"], i["h"]] for i in IMG[k]["items"]]}
data = {"contact": {"whatsapp": "91" + PH1, "phones": [PH1, PH2], "instagram": IG1, "instagram2": IG2}, "albums": albums,
        "films": [{"id": f, "title": t, "tag": g} for f, t, g in FILMS], "reels": [{"id": f, "title": t} for f, t in REELS]}
open("js/data.js", "w").write("/* UniqueCreation — site content. Edit albums, films, reels or contact details here. */\nwindow.UC = " + json.dumps(data, indent=1) + ";\n")

# ---- partials
def wa(label="WhatsApp us", cls="pill pill--cobalt"):
    return f'<a class="{cls}" href="{WA}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-wa"/></svg><span>{label}</span></a>'

NAV = [("index.html#genres", "Work"), ("films.html", "Films &amp; reels"), ("gallery.html", "Gallery"), ("index.html#about", "About"), ("index.html#contact", "Contact")]

def head(title, desc, page):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#f5efe3">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="assets/brand/og-image.jpg"><meta property="og:type" content="website">
<link rel="icon" href="assets/brand/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/is.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="css/style.css{V}">
</head>
<body data-page="{page}" id="top">
{SPRITE}
<a class="sr-only" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"><i></i></div>
<header class="hdr">
  <a class="brand" href="index.html" aria-label="UniqueCreation, home">Unique<em>Creation</em><b></b></a>
  <nav class="hdr__nav" aria-label="Main">{"".join(f'<a href="{h}">{t}</a>' for h, t in NAV)}</nav>
  {wa("WhatsApp us", "pill pill--cobalt hdr__cta")}
  <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><i></i><i></i></button>
</header>
<div class="menu" id="menu" aria-hidden="true">
  <nav aria-label="Mobile">{"".join(f'<a href="{h}"><small>0{i+1}</small>{t}</a>' for i, (h, t) in enumerate(NAV))}</nav>
  <div class="menu__foot">
    {wa("WhatsApp us", "pill pill--ink")}
    <div class="menu__soc">
      <a class="round" href="{IG1}" target="_blank" rel="noopener" aria-label="Instagram"><svg aria-hidden="true"><use href="#i-ig"/></svg></a>
      <a class="round" href="tel:+91{PH1}" aria-label="Call {PH1}"><svg aria-hidden="true"><use href="#i-phone"/></svg></a>
    </div>
    <p>{PH1} &middot; {PH2}</p>
  </div>
</div>
<main id="main">
'''

def foot(fm=False):
    s = f'''</main>
<footer class="foot">
  <div class="wrap">
    <p class="foot__big" aria-hidden="true">Unique<em>Creation</em></p>
    <div class="foot__row">
      <span>&copy; <span data-year>2026</span> UniqueCreation &middot; Uddip Phukan</span>
      <nav aria-label="Footer">
        <a href="gallery.html">Gallery</a><a href="films.html">Films &amp; reels</a>
        <a href="{IG1}" target="_blank" rel="noopener">Instagram</a>
        <a href="{IG2}" target="_blank" rel="noopener">@pinkuuddip</a>
        <a href="#top" data-top>Back to top</a>
      </nav>
    </div>
  </div>
</footer>
<a class="fab" href="{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><svg aria-hidden="true"><use href="#i-wa"/></svg></a>
'''
    return s

FM = '''<div class="fm" role="dialog" aria-modal="true" aria-label="Video player" aria-hidden="true">
  <div class="fm__top"><h3></h3><button class="round fm__x" type="button" aria-label="Close video"><svg aria-hidden="true"><use href="#i-close"/></svg></button></div>
  <div class="fm__stage"></div>
</div>
'''
TAIL = '''<script src="js/data.js''' + V + '''"></script>
<script src="js/main.js''' + V + '''"></script>
</body>
</html>
'''

def film_card(f, t, g, eager=False):
    return f'''<button class="fc rv" type="button" data-play="assets/video/{f}.mp4" data-title="{t}" data-poster="assets/video/{f}.jpg">
        <span class="fc__m"><img src="assets/video/{f}.jpg" alt="" loading="lazy" width="960" height="540"><video data-none src="assets/video/{f}-pv.mp4" muted loop playsinline preload="none"></video><span class="fc__pl"><svg aria-hidden="true"><use href="#i-play"/></svg>Play film</span></span>
        <span class="fc__t"><h3>{t}</h3><span>{g}</span></span>
      </button>'''

def reel_card(f, t, auto=True):
    return f'''<button class="rl" type="button" data-play="assets/video/{f}.mp4" data-title="{t}" data-poster="assets/video/{f}.jpg" aria-label="Play {t}">
        <img src="assets/video/{f}.jpg" alt="" loading="lazy"><video data-pv src="assets/video/{f}-pv.mp4" muted loop playsinline preload="none"></video>
        <span class="rl__b"><span>{t}</span><span class="rl__p"><svg aria-hidden="true"><use href="#i-play"/></svg></span></span>
      </button>'''

# ---- index
ring = "".join(f'<div class="rc"><img src="assets/img/{src[k]}-t.webp" alt="" width="640" height="853" {"loading=eager fetchpriority=high" if i < 4 else ""}></div>' for i, k in enumerate(RING))
genres = ""
for i, k in enumerate(ORDER):
    a = IMG[k]; ttl = a["title"]; n = len(a["items"])
    parts = ttl.rsplit(" ", 1); tt = f'{parts[0]} <em>{parts[1]}</em>' if len(parts) > 1 else f'<em>{ttl}</em>'
    th = "".join(f'<img src="assets/img/{a["items"][j]["f"]}-t.webp" alt="" loading="lazy">' for j in (0, 1, 2) if j < n)
    genres += f'''<a class="g rv" href="gallery.html?a={k}" data-i="{i}"><span class="g__n">0{i+1}</span><span class="g__t">{tt.replace("&amp;", "&amp;")}</span><span class="g__c">{n} photographs</span><span class="g__a"><svg aria-hidden="true"><use href="#i-arrow"/></svg></span><span class="g__th">{th}</span></a>
      '''
gpv = "".join(f'<img src="assets/img/{src[COVER[k]]}-t.webp" alt="">' for k in ORDER)
words = ["Weddings", "Candid", "Pre-wedding", "Bridal", "Newborn", "Fashion", "Bihu", "Holi", "Landscapes", "Films"]
row = "".join(f'<span>{w}</span><svg class="st" aria-hidden="true"><use href="#i-star"/></svg>' for w in words)
band = f'<div class="band" aria-hidden="true"><div class="band__track"><div class="band__row">{row}</div><div class="band__row">{row}</div></div></div>'
films_idx = "\n      ".join(film_card(f, t, g) for f, t, g in FILMS[:4])
reels_idx = "\n      ".join(reel_card(f, t) for f, t in REELS)
still_img = src["48.5"]
pols = [("13.4", "Pre-wedding"), ("44.3", "Bihu"), ("34.2", "Newborn")]
pol = "".join(f'<figure><img src="assets/img/{src[k]}-t.webp" alt="" loading="lazy"><figcaption>{c}</figcaption></figure>' for k, c in pols)

index = head("UniqueCreation | Uddip Phukan, wedding, candid and landscape photography",
             "UniqueCreation by Uddip Phukan: wedding, pre-wedding, candid, newborn, fashion and landscape photography and films. We care for your emotions, we click for memories.", "home") + f'''
<section class="hero" id="hero">
  <span class="hero__blob hero__blob--1" aria-hidden="true"></span><span class="hero__blob hero__blob--2" aria-hidden="true"></span>
  <h1 class="hero__type" aria-label="UniqueCreation"><span><i>Unique</i></span><span><i>Creation</i></span></h1>
  <div class="sticker" aria-hidden="true"><svg viewBox="0 0 100 100"><defs><path id="cp" d="M50 50m-37 0a37 37 0 1 1 74 0a37 37 0 1 1-74 0"/></defs><circle class="disc" cx="50" cy="50" r="48"/><text><textPath href="#cp" textLength="228" lengthAdjust="spacing">weddings &#183; candid &#183; films &#183; </textPath></text><path d="M50 36c.7 5 4.4 8.7 9.4 9.4-5 .7-8.7 4.4-9.4 9.4-.7-5-4.4-8.7-9.4-9.4 5-.7 8.7-4.4 9.4-9.4z" fill="#15161c" transform="translate(0 4)"/></svg></div>
  <div class="ring-wrap" aria-hidden="true"><div class="ring">{ring}</div></div>
  <div class="hero__bar">
    <p class="hero__tag">We care for your emotions, <em>we click for memories.</em></p>
    <div class="hero__cta">{wa("Check my date")}<a class="pill" href="gallery.html">See the work</a></div>
    <span class="hero__hint">Drag the ring &#8596;</span>
  </div>
</section>
{band}

<section class="say"><div class="wrap">
  <p class="rv">Every frame starts with a *feeling.* We just make sure it *lasts.*</p>
  <div class="say__meta rv"><span class="chip chip--b">Weddings</span><span class="chip chip--p">Candid</span><span class="chip">Pre-wedding</span><span class="chip chip--c">Films &amp; reels</span><span class="chip">Fashion</span><span class="chip chip--b">Landscapes</span></div>
</div></section>

<section class="genres" id="genres"><div class="wrap">
  <div class="sec-h"><h2 data-words>Pick a <em>story</em></h2><p class="rv">Not only weddings. Eight kinds of work, one eye for the feeling in the frame.</p></div>
  <div class="glist">
      {genres}</div>
</div></section>
<div class="gpv" aria-hidden="true">{gpv}</div>

<section class="reels" id="reels">
  <div class="wrap"><div class="sec-h"><h2 data-words>Fresh <em>reels</em></h2><p class="rv">Short, loud and made to be shared. Drag, or just watch them drift.</p></div></div>
  <div class="rstrip" aria-label="Reels">
      {reels_idx}
  </div>
  <div class="reels__cta"><a class="pill pill--ink" href="films.html#reels">All reels<svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div>
</section>

<section class="still" aria-label="Landscape photography">
  <img src="assets/img/{still_img}.webp" alt="Misty green hills photographed by UniqueCreation" decoding="async">
  <div class="still__in">
    <div><div class="still__t">Beyond the <em>wedding</em></div><div class="still__t">mist, hills &amp; <em>monuments</em></div></div>
    <div class="glass"><h3>Scenery, too.</h3><p>Mountains, monuments and long skies from the road. The same patience, a different kind of light.</p><a class="pill pill--butter" href="gallery.html?a=scenery">See landscapes<svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div>
  </div>
</section>

<section class="films" id="films"><div class="wrap">
  <div class="sec-h"><h2 data-words>Wedding <em>films</em></h2><p class="rv">Cinematic highlights and pre-wedding stories, edited to feel like the day.</p></div>
  <div class="fgrid">
      {films_idx}
  </div>
  <div class="films__cta"><a class="pill pill--cobalt" href="films.html">All films<svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div>
</div></section>

<section class="about" id="about"><div class="wrap about__g">
  <div>
    <h2 data-words>Made by <em>Uddip</em> Phukan</h2>
    <p class="rv">UniqueCreation is a photography and films studio led by Uddip Phukan. Weddings are the heart of it, but the camera keeps going: candid moments, pre-wedding days, newborns, fashion shoots, Bihu, Holi and the hills beyond.</p>
    <p class="rv">The promise is simple and it is the studio's own line: we care for your emotions, we click for memories.</p>
    <div class="about__ig rv"><a class="pill" href="{IG1}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-ig"/></svg>@uniquecreationphotography</a><a class="pill" href="{IG2}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-ig"/></svg>@pinkuuddip</a></div>
  </div>
  <div class="pol rv" aria-hidden="true">{pol}</div>
</div></section>

<section class="contact" id="contact"><div class="wrap">
  <h2 data-words>Let&#8217;s make <em>memories.</em></h2>
  <div class="contact__g">
    <div class="contact__l">
      <p class="rv">Tell us the date and what you have in mind. We reply on WhatsApp.</p>
      {wa("WhatsApp " + PH1)}
      <a class="pill pill--butter" href="tel:+91{PH1}"><svg aria-hidden="true"><use href="#i-phone"/></svg>Call {PH1}</a>
      <a class="pill" href="tel:+91{PH2}"><svg aria-hidden="true"><use href="#i-phone"/></svg>Call {PH2}</a>
      <a class="pill" href="{IG1}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-ig"/></svg>Instagram</a>
    </div>
    <form class="enq rv" action="#" novalidate>
      <h3>Check my date</h3>
      <div class="enq__2"><label>Your name<input name="name" autocomplete="name" placeholder="Name"></label>
      <label>Event date<input name="date" type="date"></label></div>
      <label>I need<select name="type"><option>Wedding</option><option>Pre-wedding</option><option>Engagement</option><option>Candid / portrait</option><option>Maternity or newborn</option><option>Fashion shoot</option><option>Film / reel</option><option>Something else</option></select></label>
      <label>Message<textarea name="msg" placeholder="Venue, number of days, anything else"></textarea></label>
      <button class="pill pill--cobalt" type="submit"><svg aria-hidden="true"><use href="#i-wa"/></svg>Send on WhatsApp</button>
      <small>Opens WhatsApp with your details filled in.</small>
    </form>
  </div>
</div></section>
''' + foot() + FM + TAIL
open("index.html", "w").write(index)

# ---- gallery
gal = head("Gallery | UniqueCreation", "Browse UniqueCreation photographs: weddings, bridal, pre-wedding, candid, newborn, fashion, festivals and landscapes.", "gallery") + f'''
<section class="pagehead"><div class="wrap">
  <h1 id="galTitle">The <em>gallery</em></h1>
  <p id="galSub"></p>
  <div class="chips" role="group" aria-label="Filter by category"></div>
</div></section>
<div class="wrap"><div class="mas" id="mas"></div><div class="more"><button class="pill pill--ink" id="more" type="button">Show more</button></div></div>
<section class="gal-cta"><div class="wrap"><h2>Like what you <em>see?</em></h2><div class="hero__cta">{wa("Check my date")}<a class="pill" href="films.html">Watch the films</a></div></div></section>
''' + foot() + '''<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Photo viewer" aria-hidden="true">
  <div class="lb__top"><span class="lb__count" id="lbCount"></span><button class="round lb__x" type="button" aria-label="Close viewer"><svg aria-hidden="true"><use href="#i-close"/></svg></button></div>
  <div class="lb__stage"><button class="round lb__nav lb__nav--p" type="button" aria-label="Previous photo"><svg aria-hidden="true"><use href="#i-left"/></svg></button><img alt="" src=""><button class="round lb__nav lb__nav--n" type="button" aria-label="Next photo"><svg aria-hidden="true"><use href="#i-right"/></svg></button></div>
</div>
''' + TAIL
open("gallery.html", "w").write(gal)

# ---- films
fl = head("Films & reels | UniqueCreation", "Wedding films, pre-wedding stories and reels by UniqueCreation, Uddip Phukan.", "films") + f'''
<section class="pagehead"><div class="wrap"><h1>Films <em>&amp; reels</em></h1><p>Wedding highlights, pre-wedding stories and the reels in between.</p></div></section>
<section class="wrap"><div class="fgrid">
  {"".join(film_card(f, t, g) for f, t, g in FILMS)}
</div>
<h2 class="sec-sub" id="reels">The <em>reels</em></h2>
<div class="rgrid">{"".join(reel_card(f, t) for f, t in REELS)}</div></section>
<section class="gal-cta"><div class="wrap"><h2>Want a film like <em>this?</em></h2><div class="hero__cta">{wa("Check my date")}<a class="pill" href="gallery.html">See the photographs</a></div></div></section>
''' + foot() + FM + TAIL
open("films.html", "w").write(fl)

# ---- 404
nf = head("Page not found | UniqueCreation", "Page not found.", "404") + f'''
<section class="pagehead" style="min-height:80svh"><div class="wrap"><h1>Lost <em>frame</em></h1><p>That page wandered off. Let&#8217;s get you back to the pictures.</p><p style="margin-top:28px"><a class="pill pill--cobalt" href="index.html">Back home</a></p></div></section>
''' + foot() + TAIL
open("404.html", "w").write(nf)
print("built")
