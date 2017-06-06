from datetime import date
import datetime
from flask import Flask, jsonify, abort
from flask.globals import request
from flask.helpers import make_response
import time
from datastore.InMemoryEventStore import InMemoryEventStore

app = Flask(__name__)

data_store = InMemoryEventStore()
current_id = 0

event_types = ['purchase', 'deposit', 'education', 'life_event', 'hours_worked', 'education']

@app.route('/')
def index():
    return "Event Manager API \n"


@app.route('/event/api/events', methods=['GET'])
def get_event():
    return jsonify({'events': data_store.get_events()})

@app.route('/event/api/events/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    event = data_store.get_event_by_id(event_id)
    if not event:
        abort(404)
    return jsonify({'events': data_store.get_event_by_id(event_id)})


@app.route('/event/api/types', methods=['GET'])
def get_types():
    return jsonify({'event_types': event_types})


def validate_event(event):

    if event['id'] == None:
        event['id'] = generate_id()
    elif data_store.id_exists(event['id']):
        raise ValueError('ID already exists')

    if event['date'] == None:
        event['date'] = date.today()

    if event['type'] == None:
        event['type'] = 'unknown'

    if event['title'] == None:
        raise ValueError('Event provided without title')


@app.route('/event/api/events', methods=['POST'])
def create_event():
    if not request.json or not 'title' in request.json:
        abort(400)
    event = {
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'type': request.json.get('type', "unknown"),
        'date': request.json.get('date', time.strftime("%d/%m/%Y")),
        'id': request.json.get('id', generate_id())
    }
    data_store.put_event(event)
    return jsonify({'event': event}), 201




def generate_id():
    #TODO Use UUID Generation
    global current_id
    current_id +=1
    return current_id


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
