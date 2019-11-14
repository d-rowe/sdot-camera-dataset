import json
import urllib.request

INPUT = "name_ids.json"
OUTPUT = "../seattle_traffic_cams.json"

# Load data from josn
with open(INPUT, "r") as read_file:
    camera_data = json.load(read_file)

# Set data
url_patterns = camera_data['url']
img_pattern = url_patterns['img']
stream_pattern = url_patterns['stream']
locations = camera_data['locations']


def test_url(url: str) -> bool:
    try:
        code = urllib.request.urlopen(url).getcode()
        return code == 200
    except:
        return False


def create_entry(location: list) -> str:
    name, indentifier = location
    img = img_pattern.replace('<LOCATION>', indentifier)
    stream = stream_pattern.replace('<LOCATION>', indentifier)
    direction = indentifier.rpartition('_')[2]
    return {"name": name, "identifier": indentifier, "direction": direction, "img": img, "stream": stream}


render = []
for location in locations:
    entry = create_entry(location)
    name = entry['name']
    print(f"Checking {name} for broken links...")
    img_up = test_url(entry["img"])
    stream_up = test_url(entry["stream"])
    if (img_up and stream_up):
        render.append(entry)
    else:
        print(f"{name} has a broken link")

with open(OUTPUT, 'w') as outfile:
    json.dump(render, outfile, indent=4, separators=(',', ': '))

successful = len(render)
unsuccessful = len(locations) - successful

if unsuccessful == 0:
    print(f"All {successful} entries successfully created")
else:
    print(f"Successfully rendered {successful} entries")
    print(f"{unsuccessful} entries ignored due to broken links")
