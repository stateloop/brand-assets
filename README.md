# Stateloop brand assets

Publicly hosted Stateloop brand assets and email signatures.

## Install your Gmail signature

Open your page and press **Copy signature**, then paste into Gmail →
Settings → Signature with a normal paste (Ctrl+V / Cmd+V).

Do NOT copy the page by hand and paste without formatting. A plain-text copy
serialises the logo to its `alt` text, so you end up with the word "Stateloop"
where the wordmark should be — which is exactly what happened before the button
existed. The button writes `text/html` to the clipboard, so there is nothing to
get wrong; the toolbar itself is outside the copied region.

Use the rendered signature for your name:

- [Jorrit Boumann](https://stateloop.github.io/brand-assets/signatures/jorrit-boumann.html)
- [Andrea Villa](https://stateloop.github.io/brand-assets/signatures/andrea-villa.html)
- [Putra Manggala](https://stateloop.github.io/brand-assets/signatures/putra-manggala.html)
- [Taewoon Kim](https://stateloop.github.io/brand-assets/signatures/taewoon-kim.html)

Then:

1. Select the entire rendered signature and copy it.
2. Open Gmail's **Settings → See all settings → General → Signature**.
3. Create or select your signature and paste the copied content.
4. Click the pasted logo and remove only the image.
5. Put the cursor back in the empty logo area on the left of the divider.
6. Click Gmail's **Insert image** button and upload
   [`logos/email/STATELOOP_on_white@1x.png`](logos/email/STATELOOP_on_white@1x.png).
7. Select this signature under **Signature defaults** for new emails and,
   if wanted, replies and forwards.
8. Scroll to the bottom of Gmail settings and click **Save Changes**.
9. Send a test email to a different address.

Do not leave the logo copied directly from the rendered web page. In that
case Gmail sends the external website URL, which can fail when Gmail's image
proxy loads it. Uploading the image through Gmail changes it to a
Google-hosted `googleusercontent.com/mail-sig` URL.

### Recipient image privacy

Some recipients or email clients block all remote images until they choose
**Display images from this sender**. This is controlled by the recipient and
cannot be overridden by an HTML signature. The Gmail-uploaded logo is the
most reliable image-based option available through Gmail's web interface.

If a signature must render without any recipient approval, it must be
image-free. A true inline `cid:` image requires a different email client or
custom MIME email generation; Gmail's web signature editor does not support
it.

## Logos

Files are grouped by the surface they go on, because that is the only question
someone picking one actually has. The previous flat layout named files on three
different axes at once -- `clean_light` by theme, `transparent` by alpha
channel, `email_light` by destination -- and none of them told you where the
file belonged. Worse, `clean_light`/`clean_dark` were opaque plates whose names
read as "for the light theme"; that misread shipped an invisible logo once.

    logos/
      wordmark/   transparent, trimmed to the ink. Use these anywhere you
                  control the background with CSS. Padding is the caller's job.
                    STATELOOP_wordmark_ink.png     dark letters -> light surfaces
                    STATELOOP_wordmark_paper.png   light letters -> dark surfaces
      on-solid/   the wordmark on a baked-in background, for surfaces you do
                  NOT control -- third-party listings and the like. Both are
                  1808x592 plates, so neither drops into a square app-icon or
                  avatar slot; see rule 4.
                    STATELOOP_on_white.png
                    STATELOOP_on_navy.png
      email/      pre-sized for one destination; see the signature section.
                    STATELOOP_on_white@2x.png   hotlinked by the signatures
                    STATELOOP_on_white@1x.png   for Gmail's own uploader

The wordmark is the name set as type: STATEL, the infinity mark standing in for
the two O's, then P. A symbol substituting for a letter is still a wordmark.

### Dimensions

There is one master and everything else is derived from it, downstream repos
included: stateloop/design-system regenerates `STATELOOP_letters_mask.png`,
`STATELOOP_mark.png` and `STATELOOP_mark_solo.png` from
`wordmark/STATELOOP_wordmark_ink.png` with its `scripts/derive-logo-assets.py`,
so re-exporting the master means re-running that too. Rules, in order:

1. **One aspect ratio for the whole set.** The master is
   `wordmark/STATELOOP_wordmark_ink.png`, 1426x176, aspect **8.102**. Every
   export of the wordmark derives its width from its height at that ratio. The
   `on-solid/` plates are the exception: they are compositions on their own
   1808x592 canvas, aspect 3.054. This was not being
   done: the old email assets were 360x44 and 180x22, aspect 8.182, about 1%
   wider than the master. Small, but it means they were cropped by eye rather
   than exported, and eye-cropping compounds.
2. **Size a raster by its destination, times its density.** The signature
   displays at 22px tall, so the retina asset is 44px tall and the width falls
   out of the ratio: 356x44. Not a round number, and it should not be -- a
   round number here means the ratio was broken to get it.
3. **Never bake padding into a raster.** Clear space is the caller's margin,
   not baked pixels. The file this repo used to publish as
   `STATELOOP_transparent.png` was the 1426x176 wordmark floating in a 1808x592
   canvas with lopsided margins (226 left against 156 right, putting the
   wordmark 35px right of centre). That file is gone; use `wordmark/` and set
   your own space. The same off-centre canvas still ships under `on-solid/`,
   where the baked background is the point.
4. **A square asset is composed, not squeezed.** An avatar or app icon is a
   different composition, not the 8:1 wordmark scaled down. There is no square
   asset here yet; make one deliberately when it is needed.
5. **A theme pair differs only in ink colour.** Same canvas, same margins, same
   geometry -- otherwise the logo jumps when the theme flips. This one is not
   yet a pair: `_ink` carries 231 alpha values over 17,824 anti-aliased pixels
   while `_paper` is a hard 0/255 cut, and their alpha differs by up to 243
   across those same 17,824 pixels. Two renderings of the same artwork, not one
   geometry in two inks -- which is why stateloop/design-system masks `_ink`
   rather than swapping these two.

The gap worth naming: **there is no SVG master.** Every file here is a raster,
so nothing scales past 1426px cleanly and every theme variant is a separate
file. An SVG with the letters on `currentColor` and the mark on the brand azure
would replace both wordmark files with one that themes itself. The only SVG
in this repo's history is `logos/STATELOOP_logotype_on_dark.svg`, on the
unmerged `feat/figma-home-assets` branch: seven white letterform paths from
Figma, with no infinity mark, so it is no master either.

## Signature assets

The email signature uses the stable public asset URL:

`https://stateloop.github.io/brand-assets/logos/email/STATELOOP_on_white@2x.png`

`STATELOOP_on_white@2x.png` is 356x44: twice the signature's 178x22 display
size, for sharp high-density rendering at a small payload, derived from the
wordmark master at its exact aspect.

A copy also stays at the OLD path and under the OLD name,
`logos/STATELOOP_email_light.png`, because four installed Gmail signatures
hardcode that URL. Gmail stores the HTML you pasted rather than following the
repository, so moving the file alone would put a broken-image box in every mail
those signatures send. It is the same file, deliberately at two paths -- not a
second image under a second name, which is the thing this layout exists to
prevent. A symlink would not work: this site uses the legacy Pages pipeline,
where symlinks fail the BUILD outright and would take the whole site down.

The email files are named for what the PIXELS are, like logos/on-solid/ --
the folder already says they are for email. They were STATELOOP_email_light
and _gmail, and "light" read as "for the light theme" when the white ground
is baked in. It is used in DARK clients too: an <img> does not follow the
client's theme the way text does, so the plate is what keeps the wordmark
legible there.

Delete the compatibility copy once all four signatures have been reinstalled
from the rendered pages. Until then, an un-reinstalled signature renders the
new 356x44 image at its hardcoded 180x22, a 1% horizontal stretch that
disappears on reinstall.

`STATELOOP_on_white@1x.png` is the same image at 178x22 for upload. Using
Gmail's image insertion flow lets Gmail host and deliver the logo instead of
depending on an external image proxy.

## Signature colours come from the design system

The four signatures are generated, not hand-edited:

    uv run --with playwright python scripts/render-signatures.py

Email cannot use CSS custom properties -- Gmail, Outlook and Apple Mail all
want literal values in inline styles -- so a signature cannot reference a token
and has to carry the resolved number. That is exactly how a palette drifts, and
it had: these files were built from hand-picked greys (#0a0a0a, #1a1a1a,
#404040, #525252, #737373) sitting 5 to 35 away in RGB from anything in the
design system. Six levels of ink, two of which differed by 16/255 and read
identically.

The script resolves the tokens from design-system/css in a real browser and
writes the literals in, plus `signatures/tokens.lock.json` recording what it
resolved and from which version. Change a token, re-run, commit.

`--check` compares the signatures against that lockfile -- it does NOT resolve
the tokens, and needs no browser. That split is deliberate: this repository is
public and design-system is private, so CI here cannot read the palette without
being handed credentials for a private repo. The free half is still the useful
one, and it runs on every push: nobody can hand-edit a signature back to an
invented colour.

The gap that leaves, stated rather than papered over: nothing notices a palette
change until someone re-runs the generator. The lockfile names the version it
was resolved from, so at least the staleness shows up in a diff.

Every colour is composited over WHITE, not over `--color-bg`. The site's ground
is #f2f2f3 drafting paper and a mail client's is white; compositing a
translucent token over the wrong ground ships text that measures fine locally
and fails in the client.

| role | token | value | on white |
|---|---|---|---|
| name, body | `--color-text` | `#1d1f20` | 16.55:1 |
| title, contact | `--text-muted` | `#5c5d5e` | 6.60:1 |
| location | `--text-subtle` | `#707272` | 4.84:1 |
| link | `--color-link` | `#00619e` | 6.56:1 |
| rule, separator | `--color-neutral-300` | `#d4d4d7` | decorative |

Known and accepted: the logo is the `on-solid` asset, so in a dark-mode mail
client it shows as a white plate. An opaque image cannot follow the client's
theme the way text does, `prefers-color-scheme` is unreliable across mail
clients, and a mid-tone wordmark would look washed on both grounds. A brand
plate on dark reads as deliberate; a half-working swap does not.

## Team portraits

The square profile pictures used in the latest company deck:

- [`people/jorrit-boumann.jpg`](people/jorrit-boumann.jpg)
- [`people/andrea-villa.jpg`](people/andrea-villa.jpg)
- [`people/putra-manggala.jpg`](people/putra-manggala.jpg)
- [`people/taewoon-kim.jpg`](people/taewoon-kim.jpg)
