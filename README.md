# Stateloop brand assets

Publicly hosted Stateloop brand assets and email signatures.

## Install your Gmail signature

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
   [`logos/email/STATELOOP_email_gmail.png`](logos/email/STATELOOP_email_gmail.png).
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
                  NOT control -- app icons, avatars, third-party listings.
                    STATELOOP_on_white.png
                    STATELOOP_on_navy.png
      email/      pre-sized for one destination; see the signature section.
                    STATELOOP_email_light.png
                    STATELOOP_email_gmail.png

The wordmark is the name set as type: STATEL, the infinity mark standing in for
the two O's, then P. A symbol substituting for a letter is still a wordmark.

### Dimensions

There is one master and everything else is derived from it. Rules, in order:

1. **One aspect ratio for the whole set.** The master is
   `wordmark/STATELOOP_wordmark_ink.png`, 1426x176, aspect **8.102**. Every
   export derives its width from its height at that ratio. This was not being
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
   wordmark 70px right of centre). It is gone; use `wordmark/` and set your own
   space.
4. **A square asset is composed, not squeezed.** An avatar or app icon is a
   different composition, not the 8:1 wordmark scaled down. There is no square
   asset here yet; make one deliberately when it is needed.
5. **A theme pair differs only in ink colour.** Same canvas, same margins, same
   geometry -- otherwise the logo jumps when the theme flips.

The gap worth naming: **there is no SVG master.** Every file here is a raster,
so nothing scales past 1426px cleanly and every theme variant is a separate
file. An SVG with the letters on `currentColor` and the mark on the brand azure
would replace both wordmark files with one that themes itself. The two SVGs
that used to exist were pre-rebrand and carried the retired teal `#0c7070`;
they were deleted rather than repaired.

## Signature assets

The email signature uses the stable public asset URL:

`https://stateloop.github.io/brand-assets/logos/email/STATELOOP_email_light.png`

`STATELOOP_email_light.png` is 356x44: twice the signature's 178x22 display
size, for sharp high-density rendering at a small payload, derived from the
wordmark master at its exact aspect.

A copy of `STATELOOP_email_light.png` also stays at the OLD path,
`logos/STATELOOP_email_light.png`, because four installed Gmail signatures
hardcode that URL. Gmail stores the HTML you pasted rather than following the
repository, so moving the file alone would put a broken-image box in every mail
those signatures send. It is the same file, deliberately at two paths -- not a
second image under a second name, which is the thing this layout exists to
prevent. A symlink would not work: this site uses the legacy Pages pipeline,
where symlinks fail the BUILD outright and would take the whole site down.

Delete the compatibility copy once all four signatures have been reinstalled
from the rendered pages. Until then, an un-reinstalled signature renders the
new 356x44 image at its hardcoded 180x22, a 1% horizontal stretch that
disappears on reinstall.

`STATELOOP_email_gmail.png` is the same image at 178x22 for upload. Using
Gmail's image insertion flow lets Gmail host and deliver the logo instead of
depending on an external image proxy.

## Team portraits

The square profile pictures used in the latest company deck:

- [`people/jorrit-boumann.jpg`](people/jorrit-boumann.jpg)
- [`people/andrea-villa.jpg`](people/andrea-villa.jpg)
- [`people/putra-manggala.jpg`](people/putra-manggala.jpg)
- [`people/taewoon-kim.jpg`](people/taewoon-kim.jpg)
