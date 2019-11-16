import json
FILE_NAME = "name_ids.json"


while True:
    with open(FILE_NAME, "r") as read_file:
        camera_data = json.load(read_file)

    locations = camera_data['locations']

    name = input('Name: ')

    name_taken = False
    for location in locations:
        if name in location:
            name_taken = True
            print('That name has already been entered, try a new one')

    if name_taken == False:
        identifier = input('Identifier: ')
        identifier_taken = False
        for location in locations:
            if identifier in location:
                identifier_taken = True
                print('That identifier has already been entered')

    if not name_taken and not identifier_taken:

        locations.append([name, identifier])
        camera_data["locations"] = locations
        print(locations)

        with open(FILE_NAME, 'w') as outfile:
            json.dump(camera_data, outfile, indent=2, separators=(',', ': '))
        print('Saved')
