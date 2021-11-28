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

for con in data_reader:#100 test
    # print(con[4])
    print(url+str(con[0])+"/json")

    if con[0] == "" or con[4]=="":
        continue
    response = urlopen(url+str(con[0])+"/json")
    data_json = json.loads(response.read())
    # print()


    

    conf_list.append({
        'conf_core_id': con[0],
        'conf_name': con[1],
        'conf_reference': con[2],
        'conf_source': con[3],
        'conf_url': data_json['url'],
        'conf_rank': con[4],
    })

    with open("data.json", 'w') as json_file:
        json.dump(conf_list, json_file,
                  indent=4,
                  separators=(',', ': '))

    # with open('data.json', 'r', encoding='utf-8') as f:
    #     cur_data = json.loads(f.read())
    #     cur_data.append(conf_data)
    # with open('data.json', 'a', encoding='utf-8') as f:
    #     json.dump(cur_data, f, indent=4)

data.close()

# menu_reader = csv.reader(menu)
# menu_headings = next(menu_reader)
# print(menu_headings[0].split(" ")[0]+"\t"+menu_headings[1].split(" ")[0]+"\t"+menu_headings[2].split(" ")[0])
# items = []
# for item in menu_reader:
#     print(item[0]+"\t"+item[1]+"\t"+item[2])
#     main_menu[item[0]] = (item[1],item[2])
# menu.close()
