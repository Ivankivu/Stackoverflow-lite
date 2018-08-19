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

            {
                "answer_id": "What is a computer",  #users['answers'].append(3)
                "desc": "kjsadnsafdkjdsfkdsfn"
            }
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


api.add_resource(Questions, "/questions")


class Question(Resource):

        def get(self, method=["GET"]):
            parser = reqparse.RequestParser()
            parser.add_argument("question_id")
            args = parser.parse_args()
            for question in questions:
                if(args["question_id"] == question["question_id"]):
                    #return question, 200
                    return jsonify({'question': question})
            return "User not found", 404

api.add_resource(Question, "/questions/<int:id>", endpoint = "question")


if __name__ == '__main__':
        app.run(debug=True)
