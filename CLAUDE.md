# Field Notes

Jackson's travel journal: https://jacksonwatkins30.github.io/travel-journal

## Adding or updating a trip
Edit `data/trips.json`. Each trip:
- `title`, `place`, `when` (the date text shown), `blurb`
- `start` / `end` (`YYYY-MM-DD`) once dates are booked; they drive "Been there" vs "Coming up" and the countdown. Use `sort` (a rough date) for trips without exact dates, or `done: true` for past trips without dates.
- `states`: two-letter codes the trip touched, e.g. `["TX"]` (highlights them on the map for that year)
- `year`: only needed when a trip has no `start`/`sort` date; it decides which year button the trip shows under
- optional: `nights`, `miles`, `runs`, `highlights` (list), `photos`
- photos: drop images in `photos/` and list them, e.g. `"photos": [{"src": "photos/tahoe-1.jpg", "caption": "First chair"}]`

## States map
`states.html` is a separate page with a 3D map (three.js from jsDelivr, falls back to a flat SVG map without WebGL). The home page shows only the States Visited card, which links to it.
`data/visited.json` → `visited` is the list of states lit up for everyone (DC lights up but doesn't count toward 50). The map is read-only on the site; Jackson asks Claude to add or remove states, which means editing `visited`. Shapes: `data/us-states.json`, US Census Bureau boundaries via us-atlas (ISC).

## Cities
`data/cities.json`: `{name, st, lat, lon}` per city; the states page projects lat/lon onto the map (Albers USA, same as the state shapes) and drops a pin. Add a city by appending a line.

Bucket list: `data/bucket.json`. Check-offs are saved in your browser.
