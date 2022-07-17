import json
import boto3
import ast

# Lambda function to receive SQS messages and use that information to update a DynamoDB table.

client = boto3.client('sqs')

dbclient = boto3.resource("dynamodb")
table = dbclient.Table("PictureData")

def lambda_handler(event, context):

    # Receive SQS Message, extract relavent data
    res = event["Records"][0]["body"]
    resdict = ast.literal_eval(res)
    
    priKey = resdict["priKey"]
    keylocation = resdict["keylocation"]
    
    print("Prikey = ", priKey)
    print("keylocation = ", keylocation)
  
    # Update database
    Primary_Column_Name = "PictureName"
    
    response = table.put_item(
        Item={
            Primary_Column_Name: priKey,
            "TestValue1": "7/16/22 TEST",
            "OrigionalName": keylocation,
            "ThumbnailName": priKey,
            })
    print(response)  