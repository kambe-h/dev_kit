
import json
import boto3
import urllib.parse

dynamodb = boto3.resource('dynamodb')

def next_seq(table, tablename):
    response = table.update_item(
        Key={
            'tablename':tablename
        },
        UpdateExpression="set seq = seq + :val",
        ExpressionAttributeValues = {
            ':val': 1
        },
        ReturnValues = 'UPDATED_NEW'
    )
    return response['Attributes']['seq']

