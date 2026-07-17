# StateLoop brand assets

Publicly hosted StateLoop brand assets and email signatures.

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
   [`logos/STATELOOP_email_gmail.png`](logos/STATELOOP_email_gmail.png).
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

## Signature assets

The email signature uses the stable public asset URL:

`https://stateloop.github.io/brand-assets/logos/STATELOOP_email_light.png`

`STATELOOP_email_light.png` is a cropped and optimized 360-by-44-pixel version
of `STATELOOP_clean_light.png`. It is prepared at twice the signature's
180-by-22-pixel display size for sharp high-density rendering with a small
payload.

`STATELOOP_email_gmail.png` is an optimized 180-by-22-pixel upload asset. Using
Gmail's image insertion flow lets Gmail host and deliver the logo instead of
depending on an external image proxy.

## Team portraits

The square profile pictures used in the latest company deck:

- [`people/jorrit-boumann.jpg`](people/jorrit-boumann.jpg)
- [`people/andrea-villa.jpg`](people/andrea-villa.jpg)
- [`people/putra-manggala.jpg`](people/putra-manggala.jpg)
- [`people/taewoon-kim.jpg`](people/taewoon-kim.jpg)
