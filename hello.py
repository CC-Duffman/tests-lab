from flask import Flask
from flask import make_response
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!\n"


@app.route('/<page_name>')
def other_page(page_name):
    response = make_response('ERROR: The page named %s does not exist.'
                             % page_name, 404)
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
