
from flask import Flask, jsonify
from datastore.InMemoryEventStore import InMemoryEventStore

app = Flask(__name__)

data_store = InMemoryEventStore()

event_types = ['purchase', 'deposit', 'education', 'life_event', 'hours_worked', 'education']

@app.route('/')
def index():
    return "Event Manager API \n"


@app.route('/event/api/events', methods=['GET'])
def get_event():
    return jsonify({'events': data_store.get_events()})

@app.route('/event/api/events/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    return jsonify({'events': data_store.get_event_by_id(event_id)})

#@app.route('/event/api/event/', methods=['PUT'])
#def put_event():
#    return jsonify({'events': data_store.get_events()})

@app.route('/event/api/types', methods=['GET'])
def get_types():
    return jsonify({'event_types': event_types})


if __name__ == '__main__':
    app.run(debug=True)
