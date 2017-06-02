import unittest
import pprint
from datetime import datetime

from webservice.datastore.InMemoryEventStore import InMemoryEventStore

class TestInMemoryEventStore(unittest.TestCase):

    data_store = InMemoryEventStore()
    pp = pprint.PrettyPrinter(indent=4)

    def setUp(self):
        self.create_test_events()


    def tearDown(self):
        pass

    def test_get_event_by_id(self):
        print("Testing Get Event by ID...")
        event = self.data_store.get_event_by_id(2349)
        self.assertEqual(event['id'] , 2349)
        self.assertEqual(event['title'], 'Wrote a bad')
        self.assertEqual(event['type'], 'education')
        self.assertEqual(event['description'],'This is the best way to make sure your code is working')
        self.assertEqual(event['date'], '1/1/01')
        self.assertEqual(event['time'], '12:34')

    def test_put_event(self):
        print("Testing the PUT function")
        test_event = {
            'id': 5555,
            'title': u'Wrote a Unit Test',
            'type': u'education',
            'description': u'This is the best way to make sure your code is working',
            'date': '1/1/02',
            'time': '12:34'
        }
        self.data_store.put_event(test_event)
        event = self.data_store.get_event_by_id(5555)
        self.assertEqual(event['id'] , 5555)
        self.assertEqual(event['title'], 'Wrote a Unit Test')
        self.assertEqual(event['type'], 'education')
        self.assertEqual(event['description'],'This is the best way to make sure your code is working')
        self.assertEqual(event['date'], '1/1/02')
        self.assertEqual(event['time'], '12:34')

    def test_get_events_by_date_range(self):
        print('Testing get events by date range')
        start_date = datetime.strptime('1/1/01', '%m/%d/%y')
        end_date = datetime.strptime('5/5/02', '%m/%d/%y')
        results = self.data_store.get_events_by_date_range(start_date,end_date)
        self.assertEqual(2, len(results))



    def create_test_events(self):
        self.data_store = InMemoryEventStore()
        test_event_1 = {
            'id': 2349,
            'title': u'Wrote a bad',
            'type': u'education',
            'description': u'This is the best way to make sure your code is working',
            'date': '1/1/01',
            'time': '12:34'
        }
        test_event_2 = {
            'id': 2315,
            'title': u'Wrote a Unit Test',
            'type': u'education',
            'description': u'This is the best way to make sure your code is working',
            'date': '2/2/02',
            'time': '12:34'
        }
        test_event_3 = {
            'id': 23453,
            'title': u'Failed',
            'type': u'education',
            'description': u'This is the best way to make sure your code is working',
            'date': '3/3/03',
            'time': '12:34'
        }
        test_event_4 = {
            'id': 22345,
            'title': u'Wrote a Unit Test',
            'type': u'education',
            'description': u'This is the best way to make sure your code is working',
            'date': '4/4/04',
            'time': '12:34'
        }

        self.data_store.put_event(test_event_1)
        self.data_store.put_event(test_event_2)
        self.data_store.put_event(test_event_3)
        self.data_store.put_event(test_event_4)


if __name__ == '__main__':
    unittest.main()
