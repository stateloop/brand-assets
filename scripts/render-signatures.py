#!/usr/bin/env python3
"""Generate the email signatures from the design system's colours.

    uv run --with playwright python scripts/render-signatures.py [--check]

Email cannot use CSS custom properties: Gmail, Outlook and Apple Mail all want
literal values in inline styles. So a signature cannot REFERENCE a token -- it
has to carry the resolved number. That is exactly how a palette drifts, and it
had: the four signatures were built from hand-picked greys (#0a0a0a, #1a1a1a,
#404040, #525252, #737373) that sit 5 to 35 away in RGB from anything in the
design system, invented rather than derived.

This script closes that gap the only way email allows: it resolves the tokens
from the vendored stylesheet in a real browser -- including the translucent
ones, which are color-mix() and cannot be read off a stylesheet as text -- and
writes the literals into the template. Change a token, re-run, commit.

--check re-resolves and compares without writing, so CI can fail when the
signatures no longer match the design system rather than discovering it in
someone's outbox.

Two things about the colour that are deliberate:

  Every colour is composited over WHITE, not over --color-bg. The site's ground
  is #f2f2f3 drafting paper; an email client's is white, and compositing a
  translucent token over the wrong ground is how you ship text that measures
  fine locally and fails in the client.

  --text-muted and --text-subtle are color-mix(..., transparent). Reading them
  through a canvas discards the alpha and reports them as near-black at 16:1.
  They are resolved here by painting them ON white and reading the result back.
"""
import argparse
import asyncio
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DS = ROOT.parent / "design-system" / "css"

# Role -> the design-system token that role takes its colour from. The signature
# has three levels of ink plus links and a divider; the old greys had six, two
# of which differed by 16/255 and read identically.
ROLES = {
    "ink": "var(--color-text)",        # name, and the table's inherited colour
    "muted": "var(--text-muted)",      # job title, contact block
    "subtle": "var(--text-subtle)",    # location
    "link": "var(--color-link)",       # stateloop.ai
    "divider": "var(--color-neutral-300)",  # the rule and the middot separator
}

PEOPLE = [
    ("andrea-villa", "Andrea Villa", "Technical Staff &amp; Co-founder", "andrea@stateloop.ai"),
    ("jorrit-boumann", "Jorrit Boumann", "CEO &amp; Co-founder", "jorrit@stateloop.ai"),
    ("putra-manggala", "Putra Manggala", "Technical Staff &amp; Co-founder", "putra@stateloop.ai"),
    ("taewoon-kim", "Taewoon Kim", "Technical Staff &amp; Co-founder", "taewoon@stateloop.ai"),
]

# The folder already says "email", so the filename says what the PIXELS are,
# matching logos/on-solid/. The old name was STATELOOP_email_light.png, which
# read as "for the light theme" when the ground is baked in -- the same misread
# that made STATELOOP_clean_light.png ship an invisible logo. It is used in
# dark clients too, because an <img> does not follow the client's theme.
LOGO = "https://stateloop.github.io/brand-assets/logos/email/STATELOOP_on_white@2x.png"
SANS = ("-apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Helvetica, "
        "Arial, sans-serif")
MONO = "&quot;SF Mono&quot;, Menlo, Monaco, Consolas, monospace"


async def resolve() -> dict[str, str]:
    """Resolve each token to a hex literal, composited over white."""
    from playwright.async_api import async_playwright

    probe = "".join(
        f'<span id="{k}" style="color:{v}">x</span>' for k, v in ROLES.items()
    )
    html = (f'<style>{(DS / "tokens.css").read_text()}\n'
            f'{(DS / "semantic.css").read_text()}</style>'
            f'<body style="background:#fff">{probe}</body>')

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await (await browser.new_context(color_scheme="light")).new_page()
        await page.set_content(html)
        out = await page.evaluate("""() => {
            const res = {};
            for (const el of document.querySelectorAll('span')) {
                // Paint ON white, then read back: a translucent token composited
                // against the ground it will actually sit on. Reading the
                // computed colour instead keeps the alpha and lies about it.
                const cv = document.createElement('canvas');
                cv.width = cv.height = 1;
                const x = cv.getContext('2d');
                x.fillStyle = '#ffffff'; x.fillRect(0, 0, 1, 1);
                x.fillStyle = getComputedStyle(el).color; x.fillRect(0, 0, 1, 1);
                const [r, g, b] = x.getImageData(0, 0, 1, 1).data;
                res[el.id] = '#' + [r, g, b].map(v => v.toString(16).padStart(2, '0')).join('');
            }
            return res;
        }""")
        await browser.close()
    return out


# The page exists to be copied INTO Gmail, and the obvious way to copy it is
# the way that loses the logo: a plain-text copy serialises <img> to its alt
# text, so you paste the word "Stateloop" where the wordmark should be. The
# button writes text/html to the clipboard explicitly, so there is nothing to
# get wrong. Everything it needs is inline -- the page must keep working with
# no build step -- and the toolbar sits OUTSIDE the copied region, so a
# select-all still copies only the signature.
TOOLBAR = """  <div id="bar" style="font: 500 13px -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; color: #5c5d5e; margin: 0 0 20px; user-select: none;">
    <button id="copy" style="font: inherit; color: #1d1f20; background: #fff; border: 1px solid #d4d4d7; border-radius: 4px; padding: 7px 13px; cursor: pointer;">Copy signature</button>
    <span id="msg" style="margin-left: 10px; color: #707272;">then paste into Gmail → Settings → Signature</span>
  </div>
"""

SCRIPT = """  <script>
    (function () {
      var btn = document.getElementById('copy');
      var msg = document.getElementById('msg');
      var sig = document.getElementById('signature');
      function say(t) { msg.textContent = t; }
      btn.addEventListener('click', async function () {
        var html = sig.innerHTML;
        try {
          // text/html is the whole point: a text/plain copy turns the logo
          // into the word "Stateloop".
          await navigator.clipboard.write([new ClipboardItem({
            'text/html': new Blob([html], { type: 'text/html' }),
            'text/plain': new Blob([sig.innerText], { type: 'text/plain' })
          })]);
          say('Copied. Paste into Gmail → Settings → Signature.');
        } catch (e) {
          // Older browsers, or a denied permission: select the signature so
          // the user's own copy still carries the markup.
          var r = document.createRange();
          r.selectNodeContents(sig);
          var s = getSelection(); s.removeAllRanges(); s.addRange(r);
          say('Selected — press Ctrl+C (Cmd+C), then paste with Ctrl+V.');
        }
      });
    })();
  </script>
"""


def render(c: dict[str, str], name: str, title: str, email: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name} — Stateloop email signature</title>
</head>
<body>
{TOOLBAR}  <div id="signature">
  <table cellpadding="0" cellspacing="0" border="0" style="font-family: {SANS}; color: {c['ink']}; font-size: 13px; line-height: 1.5;">
    <tbody>
      <tr>
        <td style="margin: 0; padding: 0 20px 0 0; border-right: 1px solid {c['divider']}; vertical-align: middle;">
          <img src="{LOGO}" alt="Stateloop" width="178" height="22" style="display: block; border: 0;">
        </td>
        <td style="margin: 0; padding: 0 0 0 20px; vertical-align: middle;">
          <div style="font-size: 14px; font-weight: 600; color: {c['ink']}; line-height: 1.3;">{name}</div>
          <div style="font-family: {MONO}; font-size: 11px; color: {c['muted']}; margin-top: 3px; letter-spacing: 0.3px;">{title}</div>
          <div style="font-size: 12px; color: {c['muted']}; margin-top: 10px; line-height: 1.7;">
            <a href="mailto:{email}" target="_blank" style="color: {c['muted']}; text-decoration: none;">{email}</a><br>
            <a href="https://stateloop.ai/" target="_blank" style="color: {c['link']}; text-decoration: none;">stateloop.ai</a><span style="color: {c['divider']};">&nbsp;·&nbsp;</span><span style="color: {c['subtle']};">Amsterdam, NL</span>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
  </div>
{SCRIPT}</body>
</html>
"""


LOCK = ROOT / "signatures" / "tokens.lock.json"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true",
                    help="fail if the committed signatures do not match tokens.lock.json")
    args = ap.parse_args()

    # --check reads the LOCKFILE, not the design system. brand-assets is public
    # and design-system is private, so CI here cannot resolve the tokens without
    # being handed a token for a private repo. Splitting it keeps the useful
    # half free: CI proves nobody hand-edited a signature, and the lockfile is
    # refreshed by whoever changes the palette, who has both repos checked out.
    #
    # Residual gap, stated rather than papered over: nothing here notices a
    # palette change until someone re-runs this script. The lockfile records
    # which design-system version it was resolved from so the staleness is at
    # least visible in a diff.
    if args.check:
        if not LOCK.exists():
            print("x signatures/tokens.lock.json missing — run without --check first")
            return 1
        colours = json.loads(LOCK.read_text())["colours"]
    else:
        colours = asyncio.run(resolve())
    stale = []
    for slug, name, title, email in PEOPLE:
        path = ROOT / "signatures" / f"{slug}.html"
        want = render(colours, name, title, email)
        if args.check:
            if not path.exists() or path.read_text() != want:
                stale.append(path.name)
        else:
            path.write_text(want)

    if args.check:
        if stale:
            print("x signatures do not match tokens.lock.json: " + ", ".join(stale))
            print("  regenerate: uv run --with playwright python scripts/render-signatures.py")
            return 1
        print("+ signatures match tokens.lock.json.")
        return 0

    version = "unknown"
    pkg = DS.parent / "package.json"
    if pkg.exists():
        version = json.loads(pkg.read_text()).get("version", "unknown")
    LOCK.write_text(json.dumps(
        {"resolvedFrom": f"@stateloop/design-system {version}",
         "roles": ROLES, "colours": colours}, indent=2) + "\n")

    print(f"+ wrote {len(PEOPLE)} signatures from the design system {version}:")
    for role, token in ROLES.items():
        print(f"    {role:8} {token:28} {colours[role]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
