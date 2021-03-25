from models.event import *

event1 = Event('25.03.21','Comedy Club', "1000", 'Tunnel 1', ' Charlie Murphy on Rick James')

event2 = Event('19.04.22', 'Fight Club', "2",'Basement 3','Description cannot be talked about here')

events = [event1, event2]

def add_event(new_event):
    events.append(new_event)