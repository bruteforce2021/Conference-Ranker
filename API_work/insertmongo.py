import json
from typing import Text
from pymongo import MongoClient
import pymongo
from textblob import TextBlob


myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["testDB"]

test = db["Test"]


with open('data (3).json') as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    test.insert_many(file_data)
else:
    test.insert_one(file_data)


# db.Test.find({$text: {$search: "Conference on Embedded system "}},{score: {$meta: "textScore"}, conf_title: 1, conf_acronym: 1 }).sort({score:{$meta:"textScore"}}).pretty()


# while True:

#     query = input("enter the query you want to search >>  ")

#     query_blob = TextBlob(query)
#     correct_query = query_blob.correct()

#     print("Correct Format: "+str(correct_query))

#     res = test.find(
#         {
#             "$text":
#             {
#                 "$search": query
#             }
#         },
#         {
#             "score": {"$meta": "textScore"}
#         }).sort(
#             [
#                 (
#                     'score', {
#                         "$meta": "textScore"
#                     }
#                 )
#             ]
#     )

    # print(res.count_documents())
    # conf_list = []
    # for i in res:
    #     # doc = {
    #     #     "id": i['conf_core_id'],
    #     #     "title": i['conf_title'],
    #     #     "score": i["score"]
    #     # }
    #     conf_list.append({"id": i['conf_core_id'],
    #                       "title": i['conf_title'], "rank": i['conf_rank'], "acronym": i['conf_acronym']})
    #     # print("{\n\tid: "+i['conf_core_id']+",\n\ttitle: " +
    #     #       i['conf_title']+",\n\tscore: "+str(i["score"])+"\n},\n")
    # result = {
    #     "status": 200,
    #     "data": conf_list
    # }
    # print(result)
