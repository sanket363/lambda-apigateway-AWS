import json
from api import base_url
import requests


def lambda_handler(event, context):
        
        res = requests.get(url=base_url+'todos/1')
        return {
            'statusCode': res.status_code,
            'body': res.json()
        }

