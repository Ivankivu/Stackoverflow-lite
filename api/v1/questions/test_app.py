

import unittest
import app 
from app import questions
from flask import Flask, request
import json
import sys
from flask import Request, Response
from pipenv.vendor import urllib3

class TestAPI(unittest.TestCase):
    
    def test_home(self):
         self.BaseUrl = 'http://localhost:5000'
  
    def test_posts(self):
        PostUrl = (self.BaseUrl+"?q=question,questions"+"&"+"APPID=")
        print (PostUrl)
        response = urllib3.urlopen(PostUrl)
        html=response.read()
        print(html)
        self.assertTrue("question" in html)
    
    def test_post_question(self):
        pass
    
    def test_put_question(self):
        #self.assertDictEqual("/questions", True)
        pass
    
    def test_delete_question(self):
        pass
    
    
    
