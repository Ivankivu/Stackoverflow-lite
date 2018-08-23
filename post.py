from flask import Flask

class postQuestion(flask_restful.Resource):
    def post(self, methods=["POST"]):
        request_data  = request.get_json()
    if (valid_question(request_data)):
        question = {
                        "question_title": request_data["question_title"],
                        "question_id": request_data["question_id"],
                        "description": request_data["description"],
                        "answers": request_data["answers"]
        }
        questions.append(question)
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "questions/" + str(request_data['question_title'])
        return response
    else:
        bad_object = {
        "error": "Invalid book object",
        "help_string":
        "Request format should be {'question': 'What is science',"
        "'question_id': '2','question_id': 1212 }"
        }
        response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
        return response
api.add_resource(postQuestion, "/questions", endpoint='postQuestions')