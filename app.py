from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

# 404 handler
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'There is no record: ' + request.url,
    }
    res = jsonify(message)
    res.status_code = 404
    return res
# end 404 handler


# 403 handler
@app.errorhandler(403)
def forbidden(error=None):
    message = {
        'status': 403,
        'message': 'Forbidden',
    }
    res = jsonify(message)
    res.status_code = 403
    return res
# end 403 handler

# 500 handler
@app.errorhandler(500)
def internal_server_error(error=None):

    message = {
        'status': 'fail',
        'message': 'Failed to process request',
    }
    res = jsonify(message)
    res.status_code = 500
    return res
# end 500 handler

# CORS section
@app.after_request
def after_request_func(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
# end CORS section



# Add API endpoints here
from routes import register

@app.route('/')
def homePage():
    try:
        res = "<h1 style='position: fixed; top: 50%;  left: 50%; transform: translate(-50%, -50%);font-family:Montserrat;'><img src='https://www.pattarai.in/images/pattarai_portrait.svg'/>Stretch API</h1>"
        return res

    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run()




