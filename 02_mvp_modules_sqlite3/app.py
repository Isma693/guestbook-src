"""
A simple guestbook flask app.
"""
import flask
from index import Index
from sign import Sign

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/sign',
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='34.165.58.145', port=8000, debug=True)


# 34.165.58.145
