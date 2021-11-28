import csv
import json
import io
from urllib.request import urlopen

data = open("core_data.csv")

data_reader = csv.reader(data)

conf_list = []

with open("data.json") as f:
    conf_list = json.load(f)

url = "http://portal.core.edu.au/conf-ranks/"

# count=100

for con in data_reader:
    # print(con[4])
    print(url+str(con[0])+"/json")

    if con[0] == "" or con[4] == "" or len(con[4]) > 2:
        continue
    response = urlopen(url+str(con[0])+"/json")
    data_json = json.loads(response.read())
    # print()

    tagarray = []
    s = str()
    for element in con[1]:
        if((element >= 'A' and element <= 'Z') or (element >= 'a' and element <= 'z')):
            s = s+element
        else:
            if(len(s) > 2):
                tagarray.append(s)
            s = ""

    if(len(s) > 2):
        tagarray.append(s)

    tagarray.append(data_json['acronym'])

    conf_list.append({
        'conf_core_id': con[0],
        'conf_title': con[1],
        'conf_acronym': con[2],
        'conf_source': con[3],
        'conf_url': data_json['url'],
        'conf_rank': con[4],
        'conf_tags': tagarray
    })

    with open("data.json", 'w') as json_file:
        json.dump(conf_list, json_file,
                  indent=4,
                  separators=(',', ': '))

data.close()
