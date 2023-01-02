import os
import unittest
import json
from flask import Flask
from app import app

tdata = None
with open("app/static/adress.json", "r+") as f:
   tdata=json.load(f)
   f.close()


class TestCase(unittest.TestCase):


    def setUp(self):
        app.config.from_object('config')
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        pass



    def test_view_correct_record(self):
       response = self.app.get('/view?id=2',follow_redirects=True)
       print('Testing To see if a record can be viewved')
       print('expected Request : 200')
       print('request recieved: ' ,response.status_code)
       print('Sucessfuly Viewed')
       self.assertEqual(response.status_code, 200)

    def test_view_incorrect_record(self):
       response = self.app.get('/view?id=500')
       print('Testing To see if an invalid record can be viewed')
       print('expected Request : 404')
       print('request recieved: ' ,response.status_code)
       print('Hence test concludes that a random record cannot be viewed')
       self.assertEqual(response.status_code, 404)


    def test_create_user_page(self):
       response = self.app.get('/create_user',follow_redirects=True)
       response2 = self.app.post('/create_user',data ={"email": "aktest", "fname": "test",  "lname": "er","pno": "123456"},follow_redirects=True)
       print('Testing To see if the record form can be seen')
       print('expected Request : 200')
       print('request recieved: ' ,response.status_code)
       print('Hence test concludes that the homepage can be viewed')
       print('\n') 
       print('Testing To see if a record can be created on sucess it should return to homepage')
       print('expected Request : /')
       print('request recieved: ' ,response.request.path)
       print('Hence test concludes that the homepage can be viewed')        
       self.assertEqual(response.status_code, 200)
       self.assertEqual(response2.request.path, '/')

    def test_correct_edit(self):
       response = self.app.get('/edit/2',follow_redirects=True)
       self.assertEqual(response.status_code, 200)
    
    def test_incorrect_edit(self):
       response = self.app.get('/edit/500')

       print('Testing To see if the Record can be accessed for editing')
       print('expected Request : 404')
       print('request recieved: ' ,response.status_code)
       print('Error as The record cannot be accessed')
       self.assertEqual(response.status_code, 404)

    def test_addtaskroute(self):
       response = self.app.get('/',follow_redirects=True)
       print('Testing To see if Homepage can be viewed')
       print('expected Request : 200')
       print('request recieved: ' ,response.status_code)
       print('Hence test concludes that the homepage can be viewed')
       self.assertEqual(response.status_code, 200)
   

    def tearDown(self):
        with open("app/static/adress.json", "w") as outfile:
            json.dump(tdata, outfile, indent=4,  separators=(',',': '))
            outfile.close()
        pass
if __name__ == '__main__':
    unittest.main()