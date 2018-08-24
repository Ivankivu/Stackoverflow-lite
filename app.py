from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

questions = []


@app.route('/', methods=['GET'])
def home():
        return '## Stackoverflow-lite API ##'


@app.route('/questions', methods=['GET'])
def get_question():
        parser = reqparse.RequestParser()
        parser.add_argument("question_title")
        args = parser.parse_args()
        for question in questions:
            if(args["question_title"] == question["question_title"]):
                return question, 200
        return "No Questions found", 404


@app.route('/questions', methods=['POST'])
def post():
        parser = reqparse.RequestParser()
        parser.add_argument("question_title")
        parser.add_argument("question_id")
        parser.add_argument("description")
        parser.add_argument("answers")
        args = parser.parse_args()
        question = {
                        "question_title": args["question_title"],
                        "question_id": args["question_id"],
                        "description": args["description"],
                        "answers": args["answers"]
                    }
        for question in questions:
            if(args["question_title"] == question.post["question_title"]):
                return "Question with Title {} already exists".format
                (args["question_title"]), 400
        questions.append(question)
        return question, 201


@app.route('/questions/<str>', methods=['PUT'])
def put_question():
            parser = reqparse.RequestParser()
            parser.add_argument("question_title")
            parser.add_argument("question_id")
            parser.add_argument("description")
            parser.add_argument("answer")
            args = parser.parse_args()
            for question in questions:
                if(args["question_title"] == question["question_title"]):
                    question["question_id"] == args["question_id"]
                    question["description"] == args["description"]
                    return question, 200
            question = {
                "question_title": args["question_title"],
                "question_id": args["question_id"],
                "description": args["description"]
            }
            question["answer"].append(question)
            return question, 201


@app.route('/questions/<question_title>/answers', methods=['PUT'])
def put_answer():
            parser = reqparse.RequestParser()
            parser.add_argument("question_title")
            parser.add_argument("answers")
            args = parser.parse_args()
            for question in questions:
                if(args["question_title"] == question["question_title"]):
                    for answer in question.answers:
                        answer["answer_id"] = args["answer_id"]
                        answer["asn_desc"] = args["asn_desc"]
                    return question, 200
            answer = {
                "answer_id": args["answer_id"],
                "asn_desc": args["asn_desc"]
            }
            question["answer"].append(question)
            return question, 201


@app.route('/questions/<question_title>', methods=['DELETE'])
def delete():
            parser = reqparse.RequestParser()
            parser.add_argument("question_title")
            args = parser.parse_args()
            global questions
            questions = [
                question for question in questions if
                question["question_title"] != args["question_title"]]
            return "{} is deleted.".format(args["question_title"]), 200


if __name__ == '__main__':
    app.run(debug=True)
