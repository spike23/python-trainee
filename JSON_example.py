import json
import os


file_path = 'C:\\Users\\admin\\Downloads\\'
filename = 'test_file.txt'
my_file = os.path.join(file_path, filename)


guitar_1 = {
    'brand': 'Gibson',
    'strings': 6,
    'endorsement': ['Metallica', 'Guns`n`Roses', 'ZZ Top']
}

guitar_2 = {
    'brand': 'Fender',
    'strings': 6,
    'endorsement': ['Rainbow', 'Aria', 'Iron Maiden', 'Twisted Sisters']
}

guitar_list = []
guitar_list.append(guitar_1)
guitar_list.append(guitar_2)

# save
with open(my_file, 'w') as f:
    json.dump(guitar_list, f, sort_keys=True, indent=4)

# load
with open(my_file, 'r') as f:
    my_data = json.load(f)
for guitar in my_data:
    print("Brand name is: " + str(guitar['brand']))
    print("Strinq quantity is: " + str(guitar['strings']))
    print("Endorsement band is: " + str(guitar['endorsement'][0]))
    print("Endorsement band is: " + str(guitar['endorsement'][1]))
    print("Endorsement band is: " + str(guitar['endorsement'][2]))
    if len((guitar['endorsement'])) >= 4:
        print("Endorsement band is: " + str(guitar['endorsement'][3]))
