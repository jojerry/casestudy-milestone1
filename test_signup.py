import unittest
import json

from app import app
from database.db import db


class SignupTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()
    
    def test_SignupApi(self):
        # Given
        payload = json.dumps({
                    "username" : "meena123",
                     "password" : "meena123",
                     "address" : "102-saraswathi apt,bangalore",
                     "state" : "karnataka",
                    "country" : "India",
                    "emailAddress" : "jerry123@gmail.com",
                    "pan" : "AXH454545",
                    "contactNo" : 1234567891,
                    "DOB" : "18.10.1959",
                    "accountType" : "savings"  
                    })

        # When
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        
        self.assertEqual(200, response.status_code)

    def test_LoginApi(self):
        #given
        
        payload = json.dumps({
                    "username" : "jerry123",
                     "password" : "jerry123"
                    })
       # When
        response = self.app.post('/accounts/login', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(200, response.status_code)
    
    def test_LoginApi3(self):
        #given

        payload = json.dumps(
                {
                    "username" : "jerry123",
                     "password" : "jerry123",
                     "address" : "102-saraswathi apt",
                     "state" : "karnataka",
                    "country" : "India",
                    "emailAddress" : "jerry123@gmail.com",
                    "pan" : "AXH454545",
                    "contactNo" : 111111111,
                    "DOB" : "18.10.1959",
                    "accountType" : "savings"  
                    })


       # When
        response = self.app.put('/accounts/login/5fa914d0c5088d93fab6e5df', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(201, response.status_code)    
    def test_LoginApi4(self):
        #given

        payload = json.dumps(
                {
                    "username" : "jerry123",
                     "password" : "jerry123",
                     "address" : "102-saraswathi apt",
                     "state" : "karnataka",
                    "country" : "India",
                    "emailAddress" : "jerry123@gmail.com",
                    "pan" : "AXH454545",
                    "contactNo" : "anjkghkjg",
                    "DOB" : "18.10.1959",
                    "accountType" : "savings"  
                    })


       # When
        response = self.app.put('/accounts/login/5fa914d0c5088d93fab6e5df', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(500, response.status_code)    

    

    def test_LoanApi(self):
        #given

        payload2 = json.dumps({
                    
                    "username" : "jerry123",
                    "loan_type" : "Bike loan",
                    "loan_Amount": 200000,
                    "date": "17/12/1995",
                    "rate_of_interest" :1,
                    "duration_of_loan" : 12
                    
                            })
       # When
        response = self.app.post('/accounts/login/jerry123/loans', headers={"Content-Type": "application/json"}, data=payload2)

        # Then
        self.assertEqual(200, response.status_code)

    
    