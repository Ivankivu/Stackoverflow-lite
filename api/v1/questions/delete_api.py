from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

questions = [
    {
        "question_title": "What is a computer",
        "question_id": 42,
        "description": "lorem lorem lorem",
        "answer": [

            # {
            #     "answer_id": "What is a computer",  users['answers'].append(3)
            #     "asn_desc": "kjsadnsafdkjdsfkdsfn"
            # }
        ]
    },
    {

        "question_title": "What is a computer",
        "question_id": 15,
        "description": "lorem lorem lorem lorem lorem lorem",
        "answer": []
    },
    {

        "question_title": "What is a computer",
        "question_id": 32,
        "description": "lorem lorem lorem loremlorem lorem loremlorem lorem",
        "answer": []
    }
]


class Questions(Resource):
     def get(self):
        return jsonify({'questions': questions})


api.add_resource(Questions, "/")


class Question(Resource):



        def delete(self, method=["DELETE"]):
            parser = reqparse.RequestParser()
            parser.add_argument("question_title")
            args = parser.parse_args()
            global questions
            questions = [
                question for question in questions if question["question_title"] != args["question_title"]]
            return "{} is deleted.".format(args["question_title"]), 200


api.add_resource(Question, "/")


if __name__ == '__main__':
        app.run(debug=True)
