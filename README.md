# Ground

**Layer 0 of the Ascent: the body.** Food, shelter, health, safety.

The need, in the words of the map: a material floor. Reliable food, a safe place to sleep, a body that is cared for, a life not lived in fear. The full map is [The Ascent](https://github.com/auroracommons/auroracommons/blob/main/NEEDS.md) on the Aurora Commons profile.

## What Ground is

A small board of local help in New Rochelle and nearby Westchester, checked by hand. Each listing is a Proof: what is offered, who offers it, where, when, the provider's own page as the source, the name of the person who checked it, the date they checked it, and the date to check again.

A listing joins the board only after a check on the provider's own published page. Aggregator sites, search snippets, and memory do not count. Every listing expires 30 days after its check. Past that date the board shows the listing as stale, in the open, until someone checks it again.

## Live demo

https://auroracommons.github.io/ground/ (link placeholder until the repository and Pages are enabled)

The page is one static HTML file. It reads listings.json and renders plain cards grouped by category: food, shelter, health, hygiene, and charging. No build step. No external services. No tracking.

## Proof

State as of October 15, 2026, the day this seed board was built.

- **Listings on the board: 8.** Food 3, shelter 4, health 1.
- **Verified today: 8 of 8.** Every listing was checked on October 15, 2026 against the provider's own page, and every listing expires November 14, 2026.
- **Dropped during verification: 4.** A Yonkers shelter listed as permanently closed on its own listing; a county kitchen and pantry whose hours appear only in a county PDF and not on the provider's own page; a health center found only in aggregator data; a public library listed elsewhere as a phone charging site, where the library's own pages describe free WiFi and device lending but no charging. None of them are on the board.
- **Source for each category.** Food: HOPE Community Services (hopecommunityservices.org) and the United Community Center of Westchester (uccenter.org). Shelter: WestCOP (westcop.org), Lifting Up Westchester (liftingupwestchester.org), and United Way of Westchester and Putnam (uwwp.org) for the Hudson Valley 211 helpline. Health: Open Door Care Network (opendoormedical.org).
- **Hygiene and charging are empty, on purpose.** No listing in those categories could be verified on a provider's own page today, so the sections stand empty on the board rather than filled with unchecked claims.
- **The expiry rule.** Verified date plus 30 days is the expiry. The page compares today's date to each expiry and marks a passed listing stale. It never hides one silently.
- **The check log.** checks.json in this repository is the public log of every check: listing, verifier, date, result. The seed checks are credited to the Ground maintainers.
- **How this board improves.** It runs the Loop: measured fundamentals, the weakest one named, one verified change at a time. [BASELINE.md](BASELINE.md) holds the numbers and the open log of cycles.

## Verify a listing

This is the participation door, and it takes minutes.

1. Pick any listing on the board, or one marked stale.
2. Open the provider page the listing links to.
3. Check that the offer, the place, and the times still match.
4. Open a pull request: add your check to checks.json (listing id, your name, stage name, or handle, today's date, and what you found), and update the listing in listings.json with the new verified date and a new expiry 30 days later.
5. When the pull request lands, the listing carries your name and your date. Your minutes are visible on the board itself: they are what keeps a listing alive.

A steady stage name is a full identity for credit here, the same as a legal name. Anonymous checks are recorded as anonymous. If you find that a listing is wrong, say so in the pull request or an issue: a wrong listing is fixed or removed in the open, and the check that caught it is logged too.

## Contribute

Ways in are in [COLLABORATE.md](COLLABORATE.md) and [CONTRIBUTING.md](CONTRIBUTING.md). The wider table is the [Open Table](https://github.com/auroracommons/auroracommons/blob/main/OPEN_TABLE.md) on the profile: one rule, be fair to others, and credit in the public ledger for verified work.

## License

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 Ground contributors.

## Built on the shoulders of giants

The providers on this board, who do the real work every week. The Proof format from Aurora Commons (THE_PROOF.md on the profile). Plain static HTML and JSON, viewable anywhere, forkable by anyone.
