"""Apply a 'Map update' issue to data/visited.json. Reads the issue body from ISSUE_BODY."""
import json, os, re, sys
from pathlib import Path

VALID = {"AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"}
body = os.environ.get("ISSUE_BODY", "")
m = re.search(r"^visited:\s*(.+)$", body, re.M)
if not m:
    sys.exit("No 'visited:' line found in the issue.")
codes = sorted({c for c in re.findall(r"\b[A-Z]{2}\b", m.group(1)) if c in VALID})
if len(codes) < 1:
    sys.exit("No valid state codes found.")
p = Path("data/visited.json")
data = json.loads(p.read_text())
before = set(data.get("visited", []))
data["visited"] = codes
p.write_text(json.dumps(data, indent=2) + "\n")
added, removed = sorted(set(codes) - before), sorted(before - set(codes))
out = os.environ.get("GITHUB_OUTPUT")
summary = f"added {', '.join(added) or 'none'}; removed {', '.join(removed) or 'none'}; {len([c for c in codes if c != 'DC'])} states total"
print(summary)
if out:
    with open(out, "a") as f:
        f.write(f"summary={summary}\n")
