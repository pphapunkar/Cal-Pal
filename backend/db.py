from flask import abort
from google.cloud import firestore
import json
import datetime

EVENTS = firestore.Client().collection('Events')

def get_events():
    print('Retrieving events from firestore')
    docs = EVENTS.get()
    ret = []
    for doc in docs:
        d = doc.to_dict()
        d['id'] = doc.id
        ret.append(d)
    return ret


def add_Event(data, ID):
    print('adding a new event' + ID + ' to firestore')
    data['date_added'] = datetime.datetime.now()
    #data['likes'] = 0
    EVENTS.document(ID).set(data)
    return ID


def _ensure_Events(ID):
    try:
        return EVENTS.document(ID).get()
    except:
        print('failed attempt to access Events' + ID)
        abort(404)


def Test_events(ID):
    print(ID)
    print('adding a new event' + ID + ' to firestore')
    doc_ref = EVENTS.document(ID)
    print(ID)
    doc_ref.set({
        u'dateTime': u'2019-08-23 22:00:36.886000+00:00',
        u'eventDescription': u'Join us for the Happy Hour',
        u'eventN_name': u'Yay'
    })
    print ("success")
    return ID
