# UniqueCreation — Uddip Phukan (prototype)

Static site: plain HTML, CSS and JavaScript. No build tools needed to host it.
Upload the folder to GitHub Pages (or any host) and open `index.html`.

## Pages
- `index.html` — home (3D photo ring hero, genre list with hover previews, reels, landscape section, films, about, contact)
- `gallery.html` — all photographs with category filters and lightbox (`gallery.html?a=couples` opens one category)
- `films.html` — wedding films and reels with a video player
- `404.html`

## Editing content
- `js/data.js` — albums, films, reels, phone numbers and Instagram links.
- Photos: `assets/img/` (`name.webp` full size, `name-t.webp` thumbnail). Videos: `assets/video/`.
- Contact: phones 8486339975 / 7002078910, WhatsApp button uses 8486339975. Change in `build.py` (`PH1`, `PH2`) and run `python3 build.py`.

## Before going public
Some photographs in the prototype came from other photographers' or collaborators' Instagram accounts (tagged posts). Confirm every image and film belongs to Uddip, or replace it with his own files.
Photos are resized copies of Instagram files, so they are not print quality. Replace with originals when he sends them.

Fonts: Instrument Serif and DM Sans (SIL Open Font License, files in `assets/fonts`).
