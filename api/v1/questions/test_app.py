

import unittest
import app 
from app import questions
from flask import Flask, Request, Response
from flask_restful import reqparse
import json
import sys
from urllib.request import urlopen

class TestAPI(unittest.TestCase):
    
    def test_home(self):
         self.BaseUrl = 'http://localhost:5000'
         
  
    def test_posts(self):
        PostUrl = ("http://localhost:5000/questions")
        print (PostUrl)
        for question in questions:
            self.assertTrue(args["question_title"] == question["question_title"])
            return question, 201
          
              #  return "Question with Title {} already exists".format(args["question_title"]), 400 
    #    
    
    def test_post_question(self):
        PostUrl = ("http://localhost:5000/questions/<str>")
        for question in questions:
            self.assertTrue(args["question_title"] == question["question_title"])
            return question, 201
    
    def test_put_question(self):
        #self.assertDictEqual("/questions", True)
        PostUrl = ("http://localhost:5000/questions/<str>")
    
    def test_delete_question(self):
        PostUrl = ("http://localhost:5000/questions/<str>")
    
    
    
