import json
from PIL import Image
from PIL.ExifTags import TAGS

def lambda_handler(event, context):
    
    print(event)

'''
    imagename = 
    
    image = Image.open(imagename)

    
    exifdata = image.getexif()


    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")

getmetadata("/home/gula/Desktop/Test Photos/660H0155_CR2_embedded.jpg")'''