

import unittest
import app 
from app import questions
from flask import Flask
import json
import sys

class TestAPI(unittest.TestCase):
        
    def test_home(self):
        response = self.app.get("/")
        self.assertEquals(response.code, 200)
        
  
    def test_posts(self):

        self.assertDictEqual("question", True)
    
    def test_post_question(self):
        pass
    
    def test_put_question(self):
        pass
    
    def test_delete_question(self):
        pass
    
    
    
