import requests
import json

FEISHU_WEBHOOK_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxxxxxx"


def feishu_alert(request):
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
    headers = {
        'Content-Type': 'application/json'
    }

    res = requests.request("POST", FEISHU_WEBHOOK_URL, headers=headers, data=json.dumps(payload_message))

    return f'ok'
