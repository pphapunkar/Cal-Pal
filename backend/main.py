import db
import flask
import json
import datetime

app = flask.Flask(__name__)


@app.route('/test', methods=['GET'])
def Test_events():
    print('testing')
    db.Test_events("12345")


@app.route('/Events', methods=['GET'])
def read_events():
    print('backend service responding to request for events')
    # string is default to prevent error when jsonifying python datetime
    return json.dumps(db.get_events(), indent=4, sort_keys=True, default=str), 200


@app.route('/Events/add/<id>', methods=['GET'])
def create_event(id):
    print('backend service adding new happening')
    data = flask.request.form.to_dict(flat=True)
    doc = db.add_Event(data, id)
    return flask.jsonify({'ID': doc}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)