import flask
from flask import request, jsonify

from verify_email import verify_email

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>welcome to email verifier</p>"


@app.route('/data', methods=['GET'])
def get_query_string():
    return request.args['email']


@app.route('/verify-email', methods=['GET'])
def get_verify_email():
    email = request.args['email']
    res = verify_email(email)
    return jsonify({'email': email,
                    'results': res})


if __name__ == '__main__':
      app.run(port=4300)
