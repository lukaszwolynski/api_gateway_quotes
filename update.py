import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('quotes')   
    response = table.put_item(Item={
        'text': str(event['text']),
   })
    return "Added your quote!"