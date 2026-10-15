# Contributing to Ground

Contributions are welcome, and the main door takes minutes: verify a listing. The house rule is the evidence rule: a listing ships with the check that proves it, not just the edit.

## The main door: verify a listing

1. Pick a listing in listings.json, or one the board marks stale.
2. Open the provider page in its source field.
3. Check the offer, where, and when against that page.
4. In one pull request: add your check to checks.json (listing id, your name, stage name, or handle, today's date, what you found), and update the listing's verified and expires dates (expiry is 30 days after the check).
5. When it lands, the board shows your name and your date on the listing.

Credit is by name, stage name, or anonymously, as you choose. A steady stage name is a full identity for credit here.

## Other good first tasks (sized in hours)

- **Report a wrong listing (under an hour).** Open an issue with what is wrong and the provider page that shows it. A documented error is a contribution.
- **Find a hygiene or charging listing (1 to 2 hours).** Both sections are empty because nothing passed verification yet. Find a provider whose own page states the offer, place, and times, and propose the listing with the page linked.
- **Check the board on a phone (under an hour).** Open the demo on a small screen and file anything that is hard to read or tap.

## Ground rules

- Provider pages only. No aggregator data, no search snippets, no memory.
- Never invent a time, an address, or a phone number. If the provider page omits a field, the listing omits it too and says so.
- Listings state facts. No claims about quality or outcomes, and no medical claims anywhere.

## Pull requests

Keep them small and single purpose. State the evidence in the PR description: the page you checked and what it said. Contributors are named in release notes, by name, stage name, or anonymously, as they choose.
