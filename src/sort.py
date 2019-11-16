import json
FILE_NAME = "name_ids.json"

with open(FILE_NAME, "r") as read_file:
    camera_data = json.load(read_file)

locations = camera_data['locations']

camera_data['count'] = len(locations)
camera_data["locations"] = sorted(locations)


with open(FILE_NAME, 'w') as outfile:
    json.dump(camera_data, outfile, indent=2, separators=(',', ': '))
