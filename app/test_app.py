

import unittest
from app import questions
from venv import reqparse


class TestAPI(unittest.TestCase):
    def test_home(self):
        self.BaseUrl = 'http://localhost:5000'

    def test_posts(self):
        PostUrl = ("http://localhost:5000/questions")
        print(PostUrl)
        self.parser = reqparse.RequestParser()
        args = self.parser.parse_args()
        for question in questions:
            self.assertTrue(args["question_title"] ==
                            question["question_title"])
            return question, 201
#  return "Question with Title {} already exists"
# .format(args["question_title"]), 400

    def test_post_question(self):
        pass
        # PostUrl = ("http://localhost:5000/questions/<str>")
        # for question in questions:
        #     self.assertTrue(args["question_title"] ==
        # question["question_title"])
        #     return question, 201

    def test_put_question(self):
        pass
        # #self.assertDictEqual("/questions", True)
        # PostUrl = ("http://localhost:5000/questions/<str>")
        # for question in questions:
        #     self.assertTrue(args["question_title"] ==
        # question["question_title"])
        #     return question, 201

    def test_delete_question(self):
        pass
