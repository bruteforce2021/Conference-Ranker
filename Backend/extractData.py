import csv
import json
import io
from urllib.request import urlopen

data = open("core_data.csv")

data_reader = csv.reader(data)

conf_list = []

with open("data.json") as f:
    conf_list = json.load(f)



# menu_reader = csv.reader(menu)
# menu_headings = next(menu_reader)
# print(menu_headings[0].split(" ")[0]+"\t"+menu_headings[1].split(" ")[0]+"\t"+menu_headings[2].split(" ")[0])
# items = []
# for item in menu_reader:
#     print(item[0]+"\t"+item[1]+"\t"+item[2])
#     main_menu[item[0]] = (item[1],item[2])
# menu.close()
