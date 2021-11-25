from flask import Flask, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from textblob import TextBlob
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
mongo_client = MongoClient("mongodb://localhost:27017")

CORS(app)

# //database
db = mongo_client.testDB
# Test document storage
test = db['Test']


def queryDB(query):
    res = test.find(
        {
            "$text":
            {
                "$search": query
            }
        },
        {
            "score": {"$meta": "textScore"}
        }).sort(
        [
            (
                'score', {
                    "$meta": "textScore"
                }
            )
        ]
    )
    return res


class ResolveQuery(Resource):
    def post(self):

        # Collecting query data
        postedData = request.get_json()
        query = postedData['query']

        # querying database
        result = queryDB(query)

        # collecting similar words
        query_blob = TextBlob(query)
        correct_query = query_blob.correct()

        if result.count() == 0:
            conf_list = []
            retmap = {
                'status': 201,
                'suggest_word': str(correct_query),
                'data': conf_list
            }
            return retmap
        else:
            conf_list = []
            for conf in result:
                conf_list.append({"id": conf['conf_core_id'],
                                  "title": conf['conf_title'],
                                  "rank": conf['conf_rank'],
                                  "acronym": conf['conf_acronym'],
                                  'url': conf['conf_url'],
                                  'source': conf['conf_source']
                                  })

            retmap = {
                'status': 200,
                'suggest_word': str(correct_query),
                'data': conf_list
            }
            return retmap


class Print(Resource):
    def post(self):

        # //step 1: getting json data
        postedData = request.get_json()

        # //step 2: json data to variable
        name = postedData["name"]

        # process variable

        return {
            "Status": 200,
            "Message": "Yee it works "+name
        }


api.add_resource(Print, '/print')
api.add_resource(ResolveQuery, '/query')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
