"""Writes a JSON file with show information to be used by other scripts"""

import json

sample_data = {
    "show": "Gentleman's Guide to Love and Murder",
    "units": ["Platform", "Wagon", "Portal 1", "Portal 2"]
}

json_object = json.dumps(sample_data, indent=4)

with open("data.json", "w", encoding="UTF-8") as outfile:
    outfile.write(json_object)
