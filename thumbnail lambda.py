import json
import boto3
import uuid
import time
from PIL import Image


s3 = boto3.resource("s3")
client = boto3.client('sqs')

s3Bucket = s3.Bucket("newtestbucket25324dhfghgfhd8gds0")
destinationBucket = s3.Bucket("thumbnailimages49f2ng34b0wmw2mv")


def lambda_handler(event, context):
    
    
    bucketlocation = event['Records'][0]['s3']['bucket']['name']
    
    # Get name of item that triggered labmda
    keylocation = event['Records'][0]['s3']['object']['key']
    
    bucketName = s3Bucket.name
    priKey = "picture" + str(time.time()) + "_" + str(uuid.uuid4()) 
    thumbfile = "/tmp/" + priKey + ".jpg"
   
    # Copy into /tmp/ 
    response = s3.meta.client.download_file(bucketName, keylocation, thumbfile)
  
    # copy into /tmp/, resize, copy into destinationbucket
    
    # resize image
    im = Image.open(thumbfile)
    width, height = im.size
    print("Before Size: ", width, height)
    basewidth = 300
    wpercent = (basewidth/width)
    hsize = int(height*wpercent)
    im = im.resize((basewidth, hsize), Image.BOX)
    width, height = im.size
    print("After Size: ", width, height)
    im = im.save(thumbfile)
    
    # Write file to thumnail S3 bucket
    object = s3.Object(destinationBucket.name, priKey)  
    result = object.put(Body=open(thumbfile, 'rb'))
    res = result.get('ResponseMetadata')
        
    if res.get('HTTPStatusCode') == 200:
        print('File Uploaded Successfully')
    else:
        print('File Not Uploaded')
    
    
    # send message to SQS 
    response = client.send_message(
        QueueUrl='https://sqs.us-west-1.amazonaws.com/929749464795/newTestQueue0000-000-001',
        MessageBody=str({
            "priKey": priKey,
            "keylocation": keylocation
        }))
    print(response)