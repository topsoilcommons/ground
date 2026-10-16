# Ground baseline: the fundamentals, measured

## The Loop

The Loop. Ground improves by one measured cycle at a time. (1) Measure the fundamentals and write the numbers down with dates. (2) Name the weakest fundamental. (3) Make the smallest change that moves it. (4) Verify the change by re-measuring. (5) Record the cycle in the open, in this file, newest first. Then repeat. One cycle, one weakness, one verified change. Nothing counts until it is re-measured. A cycle that finds nothing it can honestly change records that too.

## Fundamentals, measured October 16, 2026

- **Verified listings: 156.** Food 59, shelter 39, health 34, hygiene 21, charging 3. Counted from listings.json on October 16, 2026.
- **Places covered: 19.** New Rochelle and nearby Westchester, Yonkers, Mount Vernon, the Bronx, Harlem, Jersey City, Newark, Philadelphia, Boston, Chicago, Houston, Los Angeles, London, Stamford, Bridgeport, Hartford, New Haven, Paterson, and Hempstead.
- **Listings with a place, times, and a provider source: 156 of 156 (100 percent each).** Every listing carries its where, its when, and the provider's own page in its source field.
- **Verification freshness: 0 listings past expiry.** 103 listings checked October 15, 2026, expiring November 14, 2026. 53 listings checked October 16, 2026, expiring November 15, 2026. The oldest check is 1 day old.
- **Checks logged: 161 entries** across checks.json and the check logs inside the place files, counted October 16, 2026.
- **Page weight: 125.2 KB.** index.html 25,982 bytes plus listings.json 99,194 bytes (125,176 bytes in all; KB counted at 1,000 bytes). The weight grew because the take away file now holds all 156 listings.
- **Taps from page open to a call or directions action: not re-measured this cycle.** Last measured October 15, 2026: 1.
- **Languages offered: 1.** English.

## The weakest fundamental

Charging: 3 of 156 listings (1.9 percent), in 3 of 19 places (London, Hartford, and Harlem). Hygiene, empty at the baseline, now stands at 21 after the two waves, so the empty category Cycle 1 attacked is closed. Charging is the category the waves could not fill: PLACES.md records that in 17 places no provider's own page states a free public charging offer. Cycle 3 added a warming space in Harlem from the city warming centers page, which counts in this category on this board, but no new phone charging offer verified. It stays named as the weakest, and each new place wave carries charging as an explicit check.

## Cycles

### Cycle 3, October 16, 2026: one warming space verified in Harlem, charging moves from 2 to 3

Baseline re-measured first: 155 listings, charging 2, in 2 of 19 places, 0 past expiry. The hunt ran on providers' own pages only. Candidates tried:

- **NYC 311 warming centers page, City of New York** (portal.311.nyc.gov). Verified. The page lists warming spaces with addresses and hours. NYC Health + Hospitals/Harlem, 506 Lenox Avenue, New York, NY, is listed as a warming space open 24/7. The page also says warming centers may be activated during periods of extreme cold, and the listing on the board says so in its own words. Added as a charging listing (this board counts warming and cooling space in that category), checked by Groundskeeper on October 16, 2026, expiring November 15, 2026, with the check logged in checks.json and in the Harlem place file.
- **LinkNYC** (link.nyc). Its own home page states device charging in a power only USB port, free, and that Links stand in all five boroughs. Its Find a Link page is a map with no specific address or hours in the page text, so no single listing could be written from the provider's own page. Does not count.
- **New Rochelle Public Library and the New York Public Library.** Their own pages describe free WiFi, computers, and device lending or digital help. No charging offer is stated. The same failure as Cycle 1.
- **Brooklyn Public Library.** Its own press page describes a mobile charging station at an interim Brooklyn Heights location, published in 2016 for a temporary site. Out of date, and Brooklyn is not one of the 19 places. Does not count.
- **Public libraries in Boston, Hartford, New Haven, Stamford, Philadelphia, Chicago, Houston, and Los Angeles.** The pages opened describe WiFi, computers, and device lending. No free public charging offer with a place and times is stated.
- **Westchester County cooling centers list.** The standing list sits in a county PDF, the pattern this board excludes, and its entries say to call for hours during a heat advisory. Does not count.

Result, re-measured after the change: 156 listings, charging 3 of 156 (1.9 percent), in 3 of 19 places. Harlem stands at 8 listings. Freshness holds at 0 listings past expiry: 103 expire November 14, 2026 and 53 expire November 15, 2026. tools/build_listings.py --check passes at 156 listings, and tools/build_counts.py now writes 156 and charging 3 on the home page. The cycle took about 6 minutes. Charging stays the weakest fundamental: one warming space moved it, and phone charging itself is still verified in only 2 places.

### Cycle 2, October 16, 2026: the board outgrew its own record, and the record is corrected

The fundamentals above were re-measured from listings.json and checks.json. The baseline on this page still described the 8 listing seed board, and the counts section of the home page, generated by tools/build_counts.py, stated that every listing was checked on October 15, 2026 and due a fresh check on November 14, 2026. That was wrong for the 52 wave 2 listings, checked October 16 and due November 15. The smallest change that moves the weakest point, a published claim a visitor acts on: the generator now spans all places, first check to last check and the last recheck date, and the page it writes says so. Verified by running the generator twice: the second run wrote the same page as the first, and the new sentence was read against the data (155 listings, 19 places, checks on October 15 and 16, last recheck November 15, 2026). The stale baseline numbers on this page are replaced by the measured block above. Charging did not move this cycle and stays the named weakest fundamental.

### Cycle 1, October 15, 2026: honest negative on hygiene and charging

Attacked the weakest fundamental. No listing was added, because no candidate could be verified on the provider's own page today. Candidates tried, each checked against the provider's own published page only:

- **The Sharing Community, Yonkers** (showers at its day program, per older third party accounts). The organization's own domain, thesharingcommunity.org, now serves an unrelated casino site. The provider publishes nothing there to check an offer against. Cannot verify.
- **Lifting Up Westchester.** Its own shelters page offers shelter, food, and case management to shelter residents. No shower or hygiene offer open to the public is published there.
- **HOPE Community Services.** Its own page lists food, housing, and distributions of clothes and supplies. No shower, laundry, or hygiene service with a place and times is published there.
- **WestCOP.** Its own pages describe the Oasis shelter and early childhood health services. No public shower or laundry offer is published there.
- **Laundry Love.** No Westchester host appears in the program's own channels. The nearest published host found is Port Washington, in Nassau County, in a 2022 host flyer: outside this board's area, and out of date.
- **Hugh A. Doyle Senior Center, New Rochelle, as cooling space** (the charging category also covers warming and cooling space). The City's own mentions are archived news items from 2011 and 2022, issued per heat event. The current standing list sits in a Westchester County PDF, the pattern this board already excludes. No standing offer with hours stands on the provider's own current page. Cannot verify.
- **Library phone charging** (New Rochelle Public Library and other county libraries). Library pages describe free WiFi and device lending. No charging offer is stated. The same failure as the seed build.
- **Mobile shower programs ShowerUp and Project Outpour.** Their own sites place their work in other states, not Westchester.

Result: hygiene stays 0, charging stays 0. The number did not move, and the board stays honest. The weakest fundamental stays named. Next cycle starts by asking Lifting Up Westchester and HOPE directly whether a public hygiene offer exists that their pages do not state.

### Cycle 0, October 15, 2026: baseline measured

The fundamentals above are the first numbers on record for this board.
