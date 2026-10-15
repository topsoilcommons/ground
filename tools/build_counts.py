#!/usr/bin/env python3
"""Build the counts section of the Ground home page from the data files.

The counts come from the same files the board itself reads: listings.json
for the seed board and places/index.json for the other boards. Nothing in
the section is typed by hand. Run this after a board changes, and commit
the page it writes.

Run: python3 tools/build_counts.py
"""

import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BEGIN = "<!-- counts:begin -->"
END = "<!-- counts:end -->"


def fmt_date(value):
    parsed = date.fromisoformat(value)
    return parsed.strftime("%B %-d, %Y")


def main():
    seed = json.loads((ROOT / "listings.json").read_text(encoding="utf-8"))
    places_data = json.loads(
        (ROOT / "places" / "index.json").read_text(encoding="utf-8"))

    rows = []
    categories = Counter()
    seed_count = len(seed["listings"])
    categories.update(l["category"] for l in seed["listings"])
    rows.append(("New Rochelle and nearby Westchester", seed_count,
                 seed["verified_on"], seed["listings"][0]["expires"]))
    for place in places_data["places"]:
        categories.update(place["categories"])
        rows.append((place["place"], place["listings"],
                     place["verified_on"], place["expires"]))
    total = sum(r[1] for r in rows)

    verified = rows[0][2]
    expires = rows[0][3]
    start = date.fromisoformat(verified)
    end = date.fromisoformat(expires)
    today = date.today()
    span = (end - start).days
    elapsed = min(max((today - start).days, 0), span)
    fraction = (elapsed / span) if span else 0

    place_rows = "\n".join(
        "<tr><td>%s</td><td>%d</td><td>%s</td><td>%s</td></tr>"
        % (name, count, fmt_date(v), fmt_date(e))
        for name, count, v, e in rows)
    cat_rows = "\n".join(
        "<tr><td>%s</td><td>%d</td></tr>" % (name.capitalize(), count)
        for name, count in sorted(categories.items(),
                                  key=lambda kv: (-kv[1], kv[0])))
    section = """%s
<section aria-labelledby="counts-h">
  <h2 id="counts-h">Ground in numbers</h2>
  <p class="sub">%d listings stand checked across %d places, counted from listings.json and places/index.json in this repository on %s. Every listing was checked on %s and is due a fresh check on %s.</p>
  <table class="counts-table">
    <thead><tr><th scope="col">Place</th><th scope="col">Listings</th><th scope="col">Checked</th><th scope="col">Check again</th></tr></thead>
    <tbody>
%s
    </tbody>
  </table>
  <table class="counts-table">
    <thead><tr><th scope="col">Kind of help</th><th scope="col">Listings</th></tr></thead>
    <tbody>
%s
    </tbody>
  </table>
  <p class="sub">How fresh the board is, as one band:</p>
  <div class="freshband" role="img" aria-label="Freshness band: %d of %d days passed between the check date and the recheck date."><i style="--scale:%.4f"></i></div>
  <p class="sub">Key: the band runs from the check date, %s, to the recheck date, %s. The filled part is the share of that span that has passed by today, %s. One unit is one day of the %d day span.</p>
</section>
%s""" % (BEGIN, total, len(rows), fmt_date(verified), fmt_date(verified),
         fmt_date(expires), place_rows, cat_rows, elapsed, span,
         fmt_date(verified), fmt_date(expires), fmt_date(today.isoformat()),
         span, END)

    path = ROOT / "index.html"
    page = path.read_text(encoding="utf-8")
    if BEGIN in page and END in page:
        before, rest = page.split(BEGIN, 1)
        _, after = rest.split(END, 1)
        page = before + section + after
    else:
        anchor = '<section>\n  <h2>One listing, as a full Proof</h2>'
        if anchor not in page:
            print("build_counts: insertion anchor not found",
                  file=sys.stderr)
            sys.exit(1)
        page = page.replace(anchor, section + "\n\n" + anchor, 1)
    path.write_text(page, encoding="utf-8")
    print("build_counts: %d listings across %d places" % (total, len(rows)))


if __name__ == "__main__":
    main()
