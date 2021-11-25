import csv
import json

data = open("core_data.csv")

data_reader = csv.reader(data)
file_object = open('train.txt', 'a')
for con in data_reader:
    file_object.write(con[1]+" "+con[2]+" ")
file_object.close()
