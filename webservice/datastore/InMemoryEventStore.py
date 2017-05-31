

template = [
        {
            'id': 1,
            'title': u'Bought groceries',
            'type': u'purchase',
            'description': u'went to the store',
            'date': '10/11/17',
            'time': '13:34'
        },
        {
            'id': 2,
            'title': u'Learned Python',
            'type': u'education',
            'description': u'found a good Python tutorial on the web',
            'date': '10/11/17',
            'time': '12:12'
        }
]

class InMemoryEventStore():

    def __init__(self):
        self.events = template

    def get_events(self):
        return self.events

    def put_event(self, event):
        self.events.append(event)

    def get_event_by_id(self, id):
        for event in self.events:
            if event['id'] == id:
                return event



