from app import app
from flask import render_template, request, redirect
from models.event_list import events, add_event
from models.event import Event

from flask.wrappers import Request


@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events/<index>')
def show(index):
    return render_template('show.html', event=events[int(index)])


@app.route('/events/new')
def new():
    return render_template('new.html', title="Add Event")

@app.route('/events', methods=['POST'])
def create():
    event_date = request.form['date']
    event_name = request.form['name_of_event']
    event_guests = request.form['number_of_guests']
    event_room = request.form['room_location']
    event_desc = request.form['description']
    new_event = Event(event_date, event_name, event_guests, event_room, event_desc)
    add_event(new_event)
    return redirect('/events')




