# a working AWS lambda function that copies objects from one bucket to another. Needs a lot of work. First ever funtional Lambda function I have ever made. 


import json
import boto3

s3 = boto3.resource("s3")

s3Bucket = s3.Bucket("newtestbucket25324dhfghgfhd8gds0")
destinationBucket = s3.Bucket("thumbnailimages49f2ng34b0wmw2mv")

def lambda_handler(event, context):
    
    listOfPhotos = []

    for thing in s3Bucket.objects.all():
        print(thing.key)
        print(type(thing))
        # if str(thing).endswith(".jpg" or ".png" or ".raw"):
        # print("Success!")
        listOfPhotos.append(thing.key)

    print(listOfPhotos)
    
    i = 0
    while i <= (len(listOfPhotos) - 1):
        destFile1 = "/tmp/testingtestingtesting" + str(i) + ".jpg"
        s3.meta.client.download_file("newtestbucket25324dhfghgfhd8gds0", str(listOfPhotos[i]), destFile1)
        print(destFile1)
        
    
        object = s3.Object(destinationBucket.name, destFile1)

        result = object.put(Body=open(destFile1, 'rb'))
        
        
        res = result.get('ResponseMetadata')
        
        if res.get('HTTPStatusCode') == 200:
            print('File Uploaded Successfully')
        else:
            print('File Not Uploaded')
        i=i+1    
        
        
        
        
        
        
        
        
        
        """
        object1 = s3.Object(destinationBucket, destFile1)
        result = object.put(Body= listOfPhotos[i])
        #s3.meta.client.put_object(Bucket= destinationBucket, Key= destFile1)
        #print(f"downloaded {listOfPhotos[i]} to destinationBucket")
        i = i + 1
    
    """
    
    
    
    
    
    
    
    
    '''
    bucket_list = []
    for bucket in s3.buckets.all():
        print(bucket.name)
        bucket_list.append(bucket.name)
    
    
    return(bucket_list)
'''





'''

s3Bucket = "newtestbucket25324dhfghgfhd8gds0"

# Download object from S3 and save it to a file
def download(s3Object, destFile):
    s3.meta.client.download_file("newtestbucket25324dhfghgfhd8gds0", s3Object, destFile)
    print(f"downloaded {s3Object} to {destFile}")


# Image resize
def imageResize(picture, thumbNailName):
    image1 = Image.open(picture)
    width, height = image1.size
    newSize = (200, 200)
    image2 = image1.resize(newSize)
    image2.save(thumbNailName)
    
'''