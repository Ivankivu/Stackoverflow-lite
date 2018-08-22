from flask import Flask, jsonify, json, url_for, Response
import flask_restful
from flask_restful import Api, Resource, reqparse, request


app = Flask(__name__)
api = flask_restful.Api(app)

questions = []


@app.route('/', endpoint='root')
def home():
    return 'Stackoverflow-lite API'


@app.route('/questions', methods=['POST'], endpoint='post_question')
def posts():

    parser = reqparse.RequestParser()
    parser.add_argument("question_title")
    parser.add_argument("question_id",type=int)
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
    return question, 201


@app.route('/questions', methods=['GET'])
def get_questions():
        if questions == []:
            return "No questions posted", 400
        else:
            return questions, 201


@app.route('/questions/<question_id>', methods=['GET'])
def get_one_questions():
         for question in questions:
            if(["question_id"] == question["question_id"]):
                return question, 201
            else:
                return "Question not found", 400
            
@app.route('/questions/<question_id>', endpoint='question')
def single_posts(question_id):
        parser = reqparse.RequestParser()
        parser.add_argument("question_title")
        args = parser.parse_args()

        for question in questions:
            if(args["question_title"] == question["question_title"]):
                return "Question with Title {} already exists".format(args["question_title"]), 400

        return question, 201

        #api.add_resource(Questions, "/", endpoint='all_questions')
    
# def post(self):
#     questions = request.get_json()
#     return jsonify({'questions': questions}),




# class Question(flask_restful.Resource):
#     def get_question(self, methods=["GET"]):
#         parser = reqparse.RequestParser()
#         parser.add_argument("question_title")
#         args = parser.parse_args()
#         for question in questions:
#             if(args["question_title"] == question["question_title"]):
#                 return question, 200
#         return "No Questions found", 404

#     def post(self, methods=["POST"]):
#         parser = reqparse.RequestParser()
#         parser.add_argument("question_title")
#         parser.add_argument("question_id")
#         parser.add_argument("description")
#         parser.add_argument("answers")
#         args = parser.parse_args()
#         question = {
#                         "question_title": args["question_title"],
#                         "question_id": args["question_id"],
#                         "description": args["description"],
#                         "answers": args["answers"]
#                     }
#         for question in questions:
#             if(args["question_title"] == question["question_title"]):
#                 return "Question with Title {} already exists".format(args["question_title"]), 400

#         questions.append(question)
#         return question, 201

#     def put_question(self, methods=["PUT"]):
#             parser = reqparse.RequestParser()
#             parser.add_argument("question_title")
#             parser.add_argument("question_id")
#             parser.add_argument("description")
#             parser.add_argument("answer")
#             args = parser.parse_args()

#             for question in questions:
#                 if(args["question_title"] == question["question_title"]):
#                     question["question_id"] == args["question_id"]
#                     question["description"] == args["description"]
#                     return question, 200

#             question = {
#                 "question_title": args["question_title"],
#                 "question_id": args["question_id"],
#                 "description": args["description"]
#             }
#             question["answer"].append(question)
#             return question, 201

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

#     def delete(self, methods=["DELETE"]):
#             parser = reqparse.RequestParser()
#             parser.add_argument("question_title")
#             args = parser.parse_args()
#             global questions
#             questions = [
#                 question for question in questions if question["question_title"] != args["question_title"]]
#             return "{} is deleted.".format(args["question_title"]), 200


# api.add_resource(Question, "/questions", endpoint='multi_questions')
# api.add_resource(Question, "/questions/<int:question_id>/<int:answer_id>", endpoint='answer')
# api.add_resource(Question, "/questions/<int:question_id>", endpoint='one_question')
# api.add_resource(Questions, "/", endpoint = 'all_questions')


if __name__ == '__main__':
        app.run(debug=True)
