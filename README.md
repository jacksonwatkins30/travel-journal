# Field Notes

Jackson's travel journal: https://jacksonwatkins30.github.io/travel-journal

## Adding or updating a trip
Edit `data/trips.json`. Each trip:
- `title`, `place`, `when` (the date text shown), `blurb`
- `start` / `end` (`YYYY-MM-DD`) once dates are booked; they drive "Been there" vs "Coming up" and the countdown. Use `sort` (a rough date) for trips without exact dates, or `done: true` for past trips without dates.
- optional: `state` (two-letter, for the states counter), `nights`, `miles`, `runs`, `highlights` (list), `photos`
- photos: drop images in `photos/` and list them, e.g. `"photos": [{"src": "photos/tahoe-1.jpg", "caption": "First chair"}]`

Bucket list: `data/bucket.json`. Check-offs are saved in your browser.
