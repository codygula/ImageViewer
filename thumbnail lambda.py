import json
import boto3
import uuid
import time
# from PIL import Image


##### This function is now able to copy an item from a source bucket, update the database, and put the object in another bucket. It is still not able to 
# resize images or extract metadata for the database. This will require getting PIL imported into lambda.

s3 = boto3.resource("s3")
client = boto3.resource("dynamodb")

s3Bucket = s3.Bucket("newtestbucket25324dhfghgfhd8gds0")
destinationBucket = s3.Bucket("thumbnailimages49f2ng34b0wmw2mv")

table = client.Table("PictureData")  

def lambda_handler(event, context):
    
    bucketlocation = event['Records'][0]['s3']['bucket']['name']
    # Get name of item that triggered labmda
    keylocation = event['Records'][0]['s3']['object']['key']
   
    bucketName = s3Bucket.name
   
    priKey = "picture" + str(time.time()) + "_" + str(uuid.uuid4()) 
    
    thumbfile = "/tmp/" + priKey + ".jpg"
    
    # The JSON test file has been fixed. I Put real bucket name and real object name into test file. This fixed the 404 error.
   
    # Copy into /tmp/ 
    response = s3.meta.client.download_file(bucketName, keylocation, thumbfile)
    
    
    # Update database
    Primary_Column_Name = "PictureName"
    
    response = table.put_item(
        Item={
            Primary_Column_Name: priKey,
            "binaryTestValue": False,
            "TestValue1": "TestingTesting",
            "OrigionalName": keylocation,
            "OrigionalS3Name": bucketlocation,
            "ThumbnailName": keylocation,
            
        })
    
     # copy into /tmp/, update database, resize, copy into destinationbucket
     
    # TODO resize images. This requires some effort to get PIL or another library imported into lambda.
    '''
    im = Image.open(thumbfile)
    width, height = im.size
    print(width, height)
    '''
     
    object = s3.Object(destinationBucket.name, thumbfile)

    result = object.put(Body=open(thumbfile, 'rb'))
        
    res = result.get('ResponseMetadata')
        
    if res.get('HTTPStatusCode') == 200:
        print('File Uploaded Successfully')
    else:
        print('File Not Uploaded')
   
