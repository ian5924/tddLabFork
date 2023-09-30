"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
from unittest import TestCase


# we need to import the unit under test - counter
from src.counter import app 

# we need to import the file that contains the status codes
from src import status 

class CounterTest(TestCase):
    """Counter tests"""

    def test_create_a_counter(self):
     """It should create a counter"""
     client = app.test_client()
     result = client.post('/counters/foo')
     self.assertEqual(result.status_code, status.HTTP_201_CREATED)
    
    def test_duplicate_a_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_update_a_counter(self):
        client = app.test_client()
        result = self.client.post('/counters/counter1')
        print("RESULT:___||||||", result.data)

        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(b'{"counter1":0}\n', result.data)
       
        updateResult = self.client.put('/counters/counter1')

        #self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(updateResult.status_code, status.HTTP_200_OK)
        self.assertEqual(b'{"counter1":1}\n', updateResult.data)
        self.assertNotEqual(updateResult.data, result.data)
    
    def test_read_a_counter(self):
        client = app.test_client()
        result = self.client.post('/counters/counter_to_be_read')
        
        #client = app.test_client()
        getResult = self.client.get('/counters/counter_to_be_read')

        #testResultData = b'{"counter1":1}\n'
        #testResultStatus = "HTTP_409_OK"
        self.assertEqual(getResult.status_code, status.HTTP_200_OK)
        self.assertEqual(b'{"counter_to_be_read":0}\n', getResult.data)
       

    def setUp(self):
        self.client = app.test_client()
