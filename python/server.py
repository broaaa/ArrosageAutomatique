from app import core
import logging
from flask import Flask,request,jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'application/json'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

logging.basicConfig(filename='./log/arrosage.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

@app.route('/api/v1.0/arrosage/herbe', methods=['POST'])
def herbe():
    if request.json["action"] == "on":
        json = core.main("on","herbe",request.json['temps'])
        return jsonify(json)
    elif request.json["action"] == "off":
        return { 'message' : core.stop_gpio()}
    else:
        return jsonify({'message':'Unknown action'})

@app.route('/api/v1.0/arrosage/potager', methods=['POST'])   
def potager():
    if request.json["action"] == "on":
        json = core.main("on","potager",request.json['temps'])
        return jsonify(json)
    elif request.json["action"] == "off":
        json = core.stop_gpio()
        return jsonify({ 'message' : json})
    else:
        return jsonify({'message':'Unknown action'})

@app.route('/api/v1.0/arrosage/status', methods=['GET'])
def status():
    status = jsonify(core.getStatus())
    print(status)
    return status #, status=200, content_type='application/json')
    #return 

@app.route('/api/v1.0/arrosage/stop', methods=['POST'])
def stop():
    core.stop_gpio()
    return jsonify(core.getStatus())

if __name__ == '__main__':
    core.initGpio()
    app.run(debug=True,host='0.0.0.0', port=5000)
