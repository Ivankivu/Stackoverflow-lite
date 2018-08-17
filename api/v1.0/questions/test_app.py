from flask import Flask, jsonify, request, json, Response, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

questions = [
    {
        "question_title": "What is a computer",
        "question_id": 42,
        "description": "lorem lorem lorem",
        "answers": [

            {
                "answer_id": "What is a computer",
                "asn_desc": "kjsadnsafdkjdsfkdsfn"
            },
            {
                "answer_id": "What is a computer",
                "asn_desc": "kjsadnsafdkjdsfkdsfn"
            }
        ]
    }

]

#get all questions
@app.route('/questions')
def get_questions():
    return jsonify({'questions': questions})


#api.add_resource(Questions, "/")class Question(Resource):


#get questions/question_title
@app.route('question/<int:question_id')
def get_a_question(question_id):
    question = {}
    for question in questions:
        if item["question_id"] == question_id:
            question = {
                "question_title": item["question_title"],
                "question_body": item["question_body"],
                "answer": item["answer"]
            }
    return jsonify(question)
            # parser = reqparse.RequestParser()
            # parser.add_argument("question_title")
            # args = parser.parse_args()
            # for question in questions:
            #     if(args["question_title"] == question["question_title"]):
            #         return question, 200
            # return "User not found", 404

#POST /questions
@app.route('/questions', method=["POST"])
def add_a_question():
    request_data = request.get_json()
    if (valid_question(request_data)):
        question = {
            "question_id": request_data[1],
            "question_title": request_data["question_title"],
            "question_body": request_data["question_body"] #"answer": item["answer"]
        }
        questions.append(question)
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "questions/" + str(request_data['question_id'])
        return response
    else:
        bad_object = {
            "error": "Invalid question object",
            "help_string":
                "Request format should be {'question_title': 'What is science?',"
                "'question_body': 'kndksfkjdshfkjsdhfdhkjd','question_id': 123 }"
        }
        response = Response(json.dumps(bad_object),
                            status=400, mimetype="appliation/json")
        return response


            # parser = reqparse.RequestParser()
            # parser.add_argument("question_title")
            # parser.add_argument("question_id")
            # parser.add_argument("description")
            # args = parser.parse_args()

            # for question in questions:
            #     if(args["question_title"] == question["question_title"]):
            #         return "Question with Title {} already exists".format(args["question_title"]), 400

            # question = {
            #     "question_title": args["question_title"],
            #     "question_id": args["question_id"],
            #     "description": args["description"]
            # }
            # questions.append(question)
            # return question, 201


#PATCH /questions/question_id
@app.route('/questions/<int:question_id')
def update_question(question_id):
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
