from flask import Flask, Request, Response
import flask_restful, reqparse

app = Flask(__name__)
api = flask_restful.Api(app)

questions = []


@app.route('/', endpoint='root')
def home():
    # install( level='DEBUG' )
    # host = 'localhost'
    # cls.ApiUrl = "http://localhost:5000"
    return '##### Stackoverflow-lite API #####'


class getQuestions(flask_restful.Resource):
    def get_question(self, methods=["GET"]):
        parser = reqparse.RequestParser()
        parser.add_argument("question_title")
        args = parser.parse_args()
        for question in questions:
            if(args["question_title"] == question["question_title"]):
                return question, 200
        return "No Questions found", 404
api.add_resource(getQuestions, "/questions", endpoint='getQuestions')

class postQuestion(flask_restful.Resource):
    def post(self, methods=["POST"]):
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
            if(args["question_title"] == question["question_title"]):
                return "Question with Title {} already exists".format(args["question_title"]), 400
        questions.append(question)
        return question, 201
api.add_resource(postQuestion, "/questions", endpoint='postQuestions')


class putQuestion(flask_restful.Resource):
    def put_question(self, methods=["PUT"]):
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
api.add_resource(putQuestion, "/questions/<question>", endpoint='putQuestion')


# class putAnswer(flask_restful.Resource):
#     def put_answer(self, methods=["PUT"]):
#             parser = reqparse.RequestParser()
#             parser.add_argument("question_title")
#             parser.add_argument("answers")
#             args = parser.parse_args()

#             for question in questions:
#                 if(args["question_title"] == question["question_title"]):
                   
#                     for answer in question.answers:
#                         answer["answer_id"] = args["answer_id"]
#                         answer["asn_desc"] = args["asn_desc"]
                  
#                     return question, 200

#             answer = {
#                 "answer_id": args["answer_id"],
#                 "asn_desc": args["asn_desc"]
#             }
#             question["answer"].append(question)
#             return question, 201
# api.add_resource(putAnswer, "/questions/<question>/<answer>", endpoint='putAnswer')

class deleteQuestion(flask_restful.Resource):
    def delete(self, methods=["DELETE"]):
            parser = reqparse.RequestParser()
            parser.add_argument("question_title")
            args = parser.parse_args()
            global questions
            questions = [
                question for question in questions if question["question_title"] != args["question_title"]]
            return "{} is deleted.".format(args["question_title"]), 200
api.add_resource(deleteQuestion, "/questions", endpoint='deleteQuestion')

if __name__ == '__main__':
        app.run(debug=True)
        