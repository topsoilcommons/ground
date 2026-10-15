# Ground in many places

**Wave 1, October 15, 2026.** Ground began as one board: New Rochelle and nearby Westchester, in listings.json. This file records the first wave of new places, built the same day to the same standard, so the pattern proves it travels.

## The standard

A listing joins a board only after a check on the provider's own published page, fetched the day the board was built. The offer, the place, and the times must all be on that page. Aggregator sites, search snippets, and memory do not count. Where a provider page omits an address, a time, or a price term, the listing says so plainly instead of borrowing the detail from anywhere else. Every listing was verified on October 15, 2026 and expires November 14, 2026. Past that date a listing is stale until someone checks it again, by the same door described in README.md.

Each place file in places/ holds its listings and its check log in the same shapes as listings.json and checks.json, plus a drops array: the candidates that were checked and did not make the board, each with its reason. places/index.json lists every place with its counts.

## The places

| Place | Listings | Food | Shelter | Health | Hygiene | Charging | Dropped |
|---|---|---|---|---|---|---|---|
| Yonkers, NY | 7 | 3 | 2 | 2 | 0 | 0 | 7 |
| Mount Vernon, NY | 8 | 5 | 0 | 3 | 0 | 0 | 10 |
| Bronx, NY | 9 | 2 | 2 | 3 | 2 | 0 | 7 |
| Harlem, NY | 7 | 4 | 1 | 2 | 0 | 0 | 11 |
| Jersey City, NJ | 7 | 2 | 2 | 2 | 1 | 0 | 8 |
| Newark, NJ | 7 | 3 | 3 | 1 | 0 | 0 | 7 |
| Philadelphia, PA | 10 | 4 | 3 | 1 | 2 | 0 | 6 |
| Boston, MA | 8 | 4 | 2 | 1 | 1 | 0 | 8 |
| Chicago, IL | 8 | 2 | 1 | 2 | 3 | 0 | 7 |
| Houston, TX | 8 | 3 | 3 | 1 | 1 | 0 | 7 |
| Los Angeles, CA | 8 | 2 | 2 | 2 | 2 | 0 | 5 |
| London, UK | 8 | 3 | 0 | 1 | 3 | 1 | 5 |

**Wave total: 95 verified listings and 88 recorded drops across 12 places.** With the seed board, Ground now holds 103 verified listings in 13 places.

## The honest negatives

- **Charging is nearly empty.** Only one charging listing verified in the whole wave, at the 999 Club Gateway in London. In the other eleven places, no provider's own page states a free public phone charging offer. Library and day centre pages describe WiFi, computers, and device lending, not charging. The sections stand empty rather than filled with unchecked claims, the same rule the seed board held.
- **Shelter verified nowhere in Mount Vernon or London.** In Mount Vernon the shelter offers found are referral based or enrolled programs, not public walk-in offers. In London the large shelter providers' own pages do not state a walk-in shelter with an address and times, and the Glass Door winter night shelters state on their own page that they are closed until late 2026. Day centres with food, showers, and laundry did verify in London, and they are on the board.
- **Hygiene stands empty as its own category in Yonkers, Mount Vernon, Harlem, and Newark,** though showers appear inside several shelter and drop-in listings in Yonkers, the Bronx, and Harlem. No standalone hygiene offer could be verified on a provider's own page in those four places.
- **Harlem was held to its own map.** Harlem is treated as Manhattan above 110th Street. Strong offers below that line, and a drop-in centre whose provider now lists it in Midtown, were dropped as out of area rather than stretched to fit.
- **Three listings first rested on a softer check; all three are now directly rechecked.** The Downtown Women's Center and Union Rescue Mission pages in Los Angeles and The Connection at St Martin's page in London hit a fetch rate limit during the wave build; those listings were first confirmed from the provider's own page content returned by search on October 15, 2026. Later the same day each page was fetched directly and every detail was confirmed again: the meal times, the guest intake hours, the drop in hours, the addresses, and the offers all match the listings as published, and the Downtown Women's Center health clinic listing, which stands on the same page, was confirmed in the same fetch. The direct rechecks are recorded in each place file's check log. No detail changed.
- **88 drops are part of the record.** Closed providers, hours that live only in PDFs or aggregator listings, offers with no address, addresses with no hours. Each drop is in its place file with its reason, so the next checker does not redo the dead ends.

## What is next

Each place improves by the Loop, like the seed board: measure, name the weakest fundamental, one verified change at a time. The weakest points after this wave are plain: charging almost everywhere, and shelter in Mount Vernon and London. Anyone can pick up any of them by the verify a listing door in README.md.
