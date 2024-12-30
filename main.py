# import json
# from datetime import datetime
# import uuid
# from flask import Flask, request

# import os
# from google.cloud import tasks_v2

# app = Flask(__name__)

# # Set environment variables
# DATETIME = os.environ.get('GET_DATETIME')
# UUID = os.environ.get('GET_UUID')
# PROJECT_ID = os.environ.get('PROJECT_ID')  # Your GCP project ID
# LOCATION = os.environ.get('LOCATION')  # Your Cloud Tasks location (e.g., 'us-central1')
# QUEUE_ID = os.environ.get('QUEUE_ID')  # Your Cloud Tasks queue ID

# client = tasks_v2.CloudTasksClient()
# parent = client.queue_path(PROJECT_ID, LOCATION, QUEUE_ID)


# @app.route('/', methods=['POST'])
# def handle_request():
#     try:
#         print(request)
#         api_event = request.path  # Get the path from the request

#         if api_event == DATETIME:
#             message = datetime.strftime(datetime.now(), "%m-%d-%Y, %I:%M:%S %p (UTC)")
#         elif api_event == UUID:
#             message = str(uuid.uuid4())
#         else:
#             return f"Error: '{api_event}' does not exist.", 400

#         print(message)

#         # Create a Cloud Task
#         task = {
#             "http_request": {  # Specify the type of request as 'http_request'
#                 "http_method": tasks_v2.HttpMethod.POST,
#                 "url": "YOUR_WORKER_URL",  # Replace with the URL of your worker service
#                 "headers": {"Content-type": "application/json"},
#                 "body": json.dumps(message).encode()
#             }
#         }

#         response = client.create_task(request={"parent": parent, "task": task})
#         print(f"Created task {response.name}")

#         return json.dumps(message)

#     except Exception as e:
#         print(e)
#         return str(e), 500

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
