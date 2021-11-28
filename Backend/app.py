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
