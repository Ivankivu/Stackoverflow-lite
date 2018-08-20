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



class Question(Resource):

        def post(self, method=["POST"]):
            parser = reqparse.RequestParser()
            parser.add_argument("question_title")
            parser.add_argument("question_id")
            parser.add_argument("description")
            args = parser.parse_args()

            for question in questions:
                if(args["question_title"] == question["question_title"]):
                    return "Question with Title {} already exists".format(args["question_title"]), 400

            question = {
                "question_title": args["question_title"],
                "question_id": args["question_id"],
                "description": args["description"]
            }
            questions.append(question)
           ##  return jsonify({'question': question}),
            return question, 201

     

api.add_resource(Question, "/question")


if __name__ == '__main__':
        app.run(debug=True)
