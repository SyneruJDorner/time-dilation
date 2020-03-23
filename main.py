import os, atexit, socket
from flask import Flask, jsonify #pip install flask
import math

#IP variables
localHost = '127.0.0.1'
globalHost = 'xxx.xxx.xxx.xxx'

#init flask
app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/my-dilation')
def getCountryList():
    c = 3 * (10 ** 8)                                       #speed of light in a vacuum in m.s-1
    v = 220000                                              #speed us relative to 0 m.s-1 in m.s-1
    deltaTime = c / math.sqrt((c ** 2) - (v ** 2))
    timeDilation = 1 - (deltaTime - 1)               #Get the actual time that has passed for us based on a static point in space with a velocity of 0
    return jsonify(timeDilation)

def correctIP():
    global globalHost
    hostname = socket.gethostname()    
    globalHost = socket.gethostbyname(hostname)

def main():
    #gets your ipv4 and stores it into 'globalHost'
    correctIP()

    #starts flask as an online service
    app.run(host=localHost, port='8000', debug=False, use_reloader=False)

if __name__ == "__main__":
    main()