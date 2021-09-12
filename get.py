import json
import boto3

def get(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('quotes')   
    response = table.scan()
    #quotes_raw = response[""]
    quotes = []
    for x in range(0, len(response["Items"])):
        quotes.append(response["Items"][x]["text"])
    
    return quotes #response["Items"]
    

    
    
    
def lambda_handler(event, context):
   # post()
    return get()
    