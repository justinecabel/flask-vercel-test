from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/author')
def author():
    return 'Hello Justine'

if __name__ == '__main__':
    app.run(debug=True)
