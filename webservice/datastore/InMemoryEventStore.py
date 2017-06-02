from datetime import datetime

class InMemoryEventStore():

    def __init__(self):
        self.events = []

    def get_events(self):
        return self.events

    def put_event(self, event):
        self.events.append(event)

    def get_event_by_id(self, id):
        for event in self.events:
            if event['id'] == id:
                return event


    def get_events_by_date_range(self,start_date,end_date):
        eventList = []
        for event in self.events:
            current_event_date = datetime.strptime(event['date'], '%m/%d/%y')
            if current_event_date >= start_date and current_event_date <= end_date:
                eventList.append(event)

        return eventList




