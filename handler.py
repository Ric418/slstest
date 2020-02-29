import json


def hello(event, context):
    if not event['body']:
        name = "worlds"
    else:
        body = event['body']
        if type(body) is not dict:
            body = json.loads(body)
        name = body['name']

    return {
        "statusCode": 200,
        "body": "Hello, " + name
    }
    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
