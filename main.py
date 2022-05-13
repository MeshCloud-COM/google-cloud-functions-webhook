import os
import json
import base64
import requests

FEISHU_WEBHOOK_URL = os.getenv("FEISHU_WEBHOOK_URL")


def feishu_alert_http(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    request_json = request.get_json()
    if request.args and 'message' in request.args:
        message = request.args.get('message')
    elif request_json and 'message' in request_json:
        message = request_json['message']
    elif request_json and 'incident' in request_json:
        message = json.dumps(request_json['incident'])
    else:
        message = f'no message'

    payload_message = {
        "msg_type": "text",
        "content": {
            "text": "标题：{0} \n消息：{1}".format("GCP 告警", message)}
    }

    res = requests.request("POST", FEISHU_WEBHOOK_URL, json=payload_message)

    return f'ok'


def feishu_alert_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """

    msg = base64.b64decode(event['data']).decode('utf-8')

    payload_message = {
        "msg_type": "text",
        "content": {
            "text": "标题：{0} \n消息：{1}".format("GCP pub sub 告警", msg)}
    }

    res = requests.request("POST", FEISHU_WEBHOOK_URL, json=payload_message)

    return f'ok'
