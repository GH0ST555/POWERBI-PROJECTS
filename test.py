import os
import unittest
from flask import Flask
from app import app


def add(x,y):
    return x + y

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config')
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        pass



    def test_view_correct_record(self):
       response = self.app.get('/view?id=2',follow_redirects=True)
       self.assertEqual(response.status_code, 200)

    def test_view_incorrect_record(self):
       response = self.app.get('/view?id=500')
       self.assertEqual(response.status_code, 404)


    def test_create_user_page(self):
       response = self.app.get('/create_user',follow_redirects=True)
       self.assertEqual(response.status_code, 200)

    def test_correct_edit(self):
       response = self.app.get('/edit/2',follow_redirects=True)
       self.assertEqual(response.status_code, 200)
    
    def test_incorrect_edit(self):
       response = self.app.get('/edit/500')
       self.assertEqual(response.status_code, 404)

    def test_addtaskroute(self):
       response = self.app.get('/',follow_redirects=True)
       self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass
        # db.session.remove()
        # db.drop_all()   

if __name__ == '__main__':
    unittest.main()