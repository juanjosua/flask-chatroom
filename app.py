from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'installation successful'


if __name__ == '__main__':
    app.run()
