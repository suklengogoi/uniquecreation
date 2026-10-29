"""Behind-the-lens section (used by build.py). Edit BTS list to change videos/results."""

BTS = [
    ("bts1", "Fashion shoot", "fashion", ["fashion-07", "fashion-03", "fashion-10"], "Fashion &amp; Portraits",
     "Studio lights, styling and direction on set. What you take home: edited frames ready for print and Instagram.", "BTS vs output"),
    ("bts2", "Newborn shoot", "family", ["family-18", "family-20", "family-22"], "Maternity &amp; Newborn",
     "Gentle light, props and a lot of patience around a sleeping baby. What you take home: soft, timeless first portraits.", "Setup to final frame"),
]


def bts_section(ICO, btn):
    cases = ""
    for n, (vid, name, alb, imgs, atitle, desc, tag) in enumerate(BTS):
        res = "".join(f'<img src="assets/img/{f}-t.webp" alt="{atitle} by UniqueCreation" loading="lazy">' for f in imgs)
        cases += f"""
  <article class="case{' case--r' if n % 2 else ''}">
    <div class="case__no"><span class="lbl">Case 0{n+1}</span><i></i><span class="lbl lbl--soft">{name} &middot; {tag}</span></div>
    <div class="case__g">
      <div class="vf rv" role="button" tabindex="0" data-play="assets/video/{vid}.mp4" data-title="Behind the lens: {name}" data-poster="assets/video/{vid}.jpg" data-cursor="Sound" aria-label="Play behind the scenes video: {name}">
        <video data-src="assets/video/{vid}.mp4" poster="assets/video/{vid}.jpg" muted loop playsinline preload="none" data-auto></video>
        <span class="vf__sh"></span>
        <span class="vf__c vf__c--tl"></span><span class="vf__c vf__c--tr"></span><span class="vf__c vf__c--bl"></span><span class="vf__c vf__c--br"></span>
        <span class="vf__rec"><i></i>REC</span><span class="vf__bat"><i></i></span>
        <span class="vf__focus"></span>
        <span class="vf__tc">00:00:00:00</span><span class="vf__mode">BTS &middot; {name}</span>
        <span class="vf__snd">{ICO("play")}Watch with sound</span>
      </div>
      <div class="case__ar" aria-hidden="true"><svg viewBox="0 0 160 60"><path d="M4 40C40 6 96 6 150 30"/><path d="M138 18l13 12-17 6"/></svg><em>becomes</em></div>
      <div class="case__res rv" style="--d:.15s">
        <span class="lbl lbl--soft">(The result)</span>
        <div class="res">{res}</div>
        <h3>{atitle}</h3><p>{desc}</p>
        {btn("See the full set", f"gallery.html?a={alb}", "ulink", False, "")}
      </div>
    </div>
  </article>"""
    tick = "".join('<span>Behind the scenes</span><b></b><span>Rec</span><b></b>' for _ in range(4))
    return f"""<section class="bts" id="bts">
  <div class="bts__tick" aria-hidden="true"><div>{tick}</div><div>{tick}</div></div>
  <div class="wrap">
  <div class="bts__h">
    <div><span class="lbl lbl--soft">(Behind the lens)</span><h2 class="h-xl" data-words>See how the <em>magic</em> is made</h2></div>
    <div><p class="rv">Every shoot is planned, lit and directed. Here is what a session looks like on the day, and what you take home after. Tap a video for sound.</p>
    <ul class="bts__inc rv"><li>Light set-up on location</li><li>Posing &amp; direction</li><li>Edited final photographs</li><li>Reels &amp; highlight films</li></ul></div>
  </div>{cases}
  </div>
</section>
"""
