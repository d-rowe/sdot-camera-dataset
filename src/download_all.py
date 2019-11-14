import requests
import shutil
import json
from datetime import datetime
import os


try:
    os.makedirs('../images')
except:
    pass

INPUT = "../seattle_traffic_cams.json"

datestr = datetime.now().strftime("%m.%d.%y_%H.%M")

# Load data from json
with open(INPUT, "r") as read_file:
    entries = json.load(read_file)

for entry in entries:
    identifier = entry['identifier']
    name = entry['name']
    img_url = entry['img']
    file_name = f"{datestr}_{identifier}.jpg"

    print(f"Downloading latest image from {name}...")

    # Open the url image, set stream to True, this will return the stream content.
    resp = requests.get(img_url, stream=True)

    # Open a local file with wb ( write binary ) permission.
    local_file = open(f"../images/{file_name}", 'wb')

    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True

    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)

    # Remove the image url response object.
    del resp

print("Finished!")
