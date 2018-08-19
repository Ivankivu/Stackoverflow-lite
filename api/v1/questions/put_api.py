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

        def put(self, method=["PUT"]):
            parser = reqparse.RequestParser()
            parser.add_argument("question_title")
            parser.add_argument("question_id")
            parser.add_argument("description")
            parser.add_argument("answer")
            args = parser.parse_args()

            for question in questions:
                if(args["question_title"] == question["question_title"]):
                    question["question_id"] = args["question_id"]
                    question["description"] = args["description"]
                    question["answer"] = args["answer"]
                    return question, 200

            question = {
                "question_title": args["question_title"],
                "question_id": args["question_id"],
                "occupation": args["occupation"]
            }
            question["answer"].append(question)
            return question, 201


api.add_resource(Question, "/")


if __name__ == '__main__':
        app.run(debug=True)
