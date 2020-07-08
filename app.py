from flask import Flask, request
app = Flask(__name__)


@app.route('/api/policies/v1.0/policies')
def hello():
    print(request.headers)
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=8080)
