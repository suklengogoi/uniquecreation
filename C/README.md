# UniqueCreation — Uddip Phukan · Design C (cinematic noir)

Static site: plain HTML, CSS and JavaScript. No build step needed to host it.
Upload the folder to GitHub Pages (or any host) and open `index.html`.

## Pages
- `index.html` — iris intro, black & white hero montage with a colour "lens" that follows the cursor,
  ivory studio statement with photos inside the text, stacking chapter cards, draggable infinite photo wall,
  landscape grid that zooms to full screen, "Now showing" film cinema, Behind the lens (round BTS videos),
  reels, contact with WhatsApp form
- `gallery.html` — the collection with chapter filters and lightbox (`gallery.html?a=bihu` opens one chapter)
- `films.html` — all films, behind the lens and reels
- `404.html`

## Editing
- `js/data.js` — albums, films, reels, phone numbers, Instagram links.
- Text, sections and photo picks: edit `build.py`, then run `python3 build.py` to rebuild the HTML.
- Photos in `assets/img/` (`name.webp` full, `name-t.webp` thumbnail). Videos in `assets/video/`.

## Before going public
Some photos came from other photographers' or collaborators' Instagram posts. Confirm every image and film is Uddip's own,
or replace it. Photos are resized Instagram copies; swap in originals when he sends them.

Fonts: Cormorant Garamond and Manrope (SIL Open Font License, in `assets/fonts`).
