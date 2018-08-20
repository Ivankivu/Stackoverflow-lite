from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

questions = []


class Questions(Resource):
     def get(self):
        return jsonify({'questions': questions})


api.add_resource(Questions, "/")


class Question(Resource):

        def get(self, method=["GET"]):
            parser = reqparse.RequestParser()
            parser.add_argument("question_title")
            args = parser.parse_args()
            for question in questions:
                if(args["question_title"] == question["question_title"]):
                    return question, 200
            return "User not found", 404

        def post(self, method=["POST"]):
            parser = reqparse.RequestParser()
            parser.add_argument("question_title")
            parser.add_argument("question_id")
            parser.add_argument("description")
            parser.add_argument("answers")
            args = parser.parse_args()

            for question in questions:
                if(args["question_title"] == question["question_title"]):
                    return "Question with Title {} already exists".format(args["question_title"]), 400

            question = {
                "question_title": args["question_title"],
                "question_id": args["question_id"],
                "description": args["description"],
                "answers": args["answers"]
            }
            questions.append(question)
            return question, 201

        def put_question(self, method=["PUT"]):
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

        # def put_answer(self, method=["PUT"]):
        #     parser = reqparse.RequestParser()
        #     parser.add_argument("question_title")
        #     parser.add_argument("answers")
        #     args = parser.parse_args()

        #     for question in questions:
        #         if(args["question_title"] == question["question_title"]):
                   
        #             for answer in question.answers:
        #                 answer["answer_id"] = args["answer_id"]
        #                 answer["asn_desc"] = args["asn_desc"]
                  
        #             return question, 200

        #     answer = {
        #         "answer_id": args["answer_id"],
        #         "asn_desc": args["asn_desc"]
        #     }
        #     question["answer"].append(question)
        #     return question, 201

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
