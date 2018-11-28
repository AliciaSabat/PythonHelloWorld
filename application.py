import os.path
import os
import flask

app = flask.Flask(__name__)
@app.route('/name')


def name():
    hiname = flask.request.args.get('name')
    #instance = load()
    return flask.jsonify("Hello " , hiname,  "!" )

