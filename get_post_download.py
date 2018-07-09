import sys
import os
from urllib import request, parse

# GET-------------------------------------------------------------------------------------------------------------------

my_url = 'https://github.com/spike23'
page = request.urlopen(my_url)
my_text = page.readlines()
for line in my_text:
    print(line)

# POST------------------------------------------------------------------------------------------------------------------

my_page = 'https://www.google.com/search?'

find = {
    'q': 'Metallica'
}

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 
                           'Chrome/67.0.3396.87 Safari/537.36'
}

try:
    my_data = parse.urlencode(find)
    my_page += my_data
    print(my_page)
    my_request = request.Request(my_page, headers=my_headers)
    response = request.urlopen(my_request)
    content = response.readlines()
    for line in content:
        print(line)
except Exception:
    print(sys.exc_info()[1])


# DOWNLOAD--------------------------------------------------------------------------------------------------------------

my_picture = 'https://dp.informator.ua/wp-content/uploads/2018/07/DSC_6176.jpg'
picture_name = os.path.split(my_picture)[1]
file_path = 'C:\\Users\\admin\\Downloads\\{0}'.format(picture_name)

try:
    request.urlretrieve(my_picture, file_path)
except Exception:
    print(sys.exc_info()[1])
