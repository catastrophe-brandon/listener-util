from flask import Flask, request
app = Flask(__name__)


def print_request_headers(request):
    print("Request Headers:")
    print("BEGIN")
    print(request.headers)
    print("END")


def print_request_body(request):
    print("Request Data:")
    print("BEGIN")
    print(request.get_data(as_text=True))
    print("END")


@app.route('/api/policies/v1.0/policies')
def policies():
    print_request_headers(request)
    print_request_body(request)
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=8080)
