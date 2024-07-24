from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response("Hello World", 200)
    return response

@app.route('/repeat')
def getParameter():
    input = request.args.get("input", "Missing get parameter")
    val = (input,200)
    return val

@app.route('/health')
@app.route('/healthcheck')
def health():
    response = make_response("OK",200)
    return response

@app.route('/hang')
def hang():
    # loop 4ever
    var = False
    while True: # var == False:
        pass
        
if __name__ == '__main__':
    # By default flask is only accessible from localhost.
    # Set this to '0.0.0.0' to make it accessible from any IP address
    # on your network (not recommended for production use)
    app.run(host='0.0.0.0', port=5004, debug=True, threaded = False)
