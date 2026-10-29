# UniqueCreation — Uddip Phukan · Design B (editorial)

Static site: plain HTML, CSS and JavaScript. No build step needed to host it.
Upload the folder to GitHub Pages (or any host) and open `index.html`.

## Pages
- `index.html` — intro counter, arch photo frame that zooms to full screen on scroll, studio statement,
  horizontal-scroll categories, film contact sheet with magnifier loupe, film player,
  "Behind the lens" (BTS videos in camera viewfinders beside the final photos; edit src/bts.py), reel fan,
  parallax landscapes, how-it-works, contact with WhatsApp form
- `gallery.html` — portfolio with category tabs, justified rows and lightbox (`gallery.html?a=bihu` opens one category)
- `films.html` — film list with hover previews and a player, plus reels
- `404.html`

## Editing
- `js/data.js` — albums, films, reels, phone numbers, Instagram links.
- Text and section content: edit `build.py`, then run `python3 build.py` (rebuilds the HTML files).
- Photos in `assets/img/` (`name.webp` full, `name-t.webp` thumbnail). Videos in `assets/video/`.

## Before going public
Some photos came from other photographers' or collaborators' Instagram posts. Confirm every image and film is Uddip's own,
or replace it. Photos are resized Instagram copies; swap in originals when he sends them.

Fonts: Bodoni Moda and Manrope (SIL Open Font License, in `assets/fonts`).
