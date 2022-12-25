from flask import Flask, request
from flask_log_request_id import RequestID, current_request_id
import json
import yaml
import time
from kubernetes import client, config, watch
from resty import create_job_object, create_job, delete_job

app = Flask(__name__)
RequestID(app)
config.load_incluster_config()

description =   """
                <!DOCTYPE html>
                <head>
                <title>Welcome to Resty API</title>
                </head>
                <body>  
                    <h3>A sample API request: curl -X POST http://localhost:8080/api?value=26</h3>
                </body>
                """			

@app.route('/', methods=['GET'])
def hello_world():
	return description

@app.route('/api', methods=['POST'])
def square():
    if not all(k in request.args for k in (["value"])):
        error_message =     f"\
                            Required paremeters : 'value'<br>\
                            Supplied paremeters : {[k for k in request.args]}\
                            "
        return error_message
    else:
        value = int(request.args['value'])
        value = request.args.get('value', type=int)
        random_id = current_request_id()[:6]
        create_job(client.BatchV1Api(), create_job_object(value, random_id))
        return json.dumps({"Initiated cron job with ID" : value})

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
