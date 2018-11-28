import os.path
import flask

app = flask.Flask(__name__)
@app.route('/name')


def name():
    hiname = flask.request.args.get('name')
    return flask.jsonify("Hello " , hiname,  "!" )

