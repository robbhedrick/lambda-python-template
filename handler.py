import boto3
import json
import sys, os, io
import logging
import requests
import time
from urllib.parse import unquote

from commands import SlashCommand

logger = logging.getLogger()
logger.setLevel(logging.INFO)



def lambda_handler(event, context):
    logger.info("--- Handler Event ---")
    logger.info(event)
    logger.info("--- Handler Context ---")
    logger.info(context)

    role = event['stageVariables'].get('role', '').lower()
    logger.info("--- Current role is {r} ---".format(r=role.upper()))

    ts_now = int(time.time())
    body_response = {"timestamp":ts_now}

    incoming_http_body = event.get("body", None)
    incoming_http_method = event.get('httpMethod', None)
    
    outgoing_http_response = {
        "statusCode": 200,
        "headers": {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        "body": ""}

    # SNS Integration
    #try:
    #    sns = event['Records'][0]['Sns']
    #    #if "Slicebot" in sns['Subject']:
    #    sns_message = json.loads(sns['Message'])
    #except Exception as e:
    #    sns_message = {}
    #    pass
    
    if not role:
        outgoing_http_response['statusCode'] = 500
        outgoing_http_response['body'] = json.dumps(
            {
                "error": True,
                "message": "Missing role from API."
            }
        )
        return outgoing_http_response
    
    if incoming_http_method == "POST":

        if incoming_http_body:

            try:
                payload = json.loads(incoming_http_body)
            except Exception as e:
                payload = dict(pair.split('=') for pair in incoming_http_body.split('&'))
                logger.error("Error trying load body as JSON")
                logger.error(str(e))
                pass

            logger.info("--- Incoming Payload ---")
            logger.info(payload)

    outgoing_http_response["body"] = json.dumps(body_response)
    return outgoing_http_response
