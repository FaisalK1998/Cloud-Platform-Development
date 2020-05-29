from __future__ import print_function

import boto3
from decimal import Decimal
import json
import os

def getLabels():
    
    #Get the resource client
    client = boto3.client('rekognition')
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Change bucket and photo to your S3 Bucket and image.
    bucket='cpd-coursework2020' 
    photo='animal1.png'                
    
    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
            MaxLabels=5) 
    
    print('Detected labels for ' + photo) 
    print(response)
    
    print('*****************************')
    
    # pk = bucket + '-' + photo
    # ddbTable = os.environ['DynamoDBTableName']
    # ddb = dynamodb.Table(ddbTable)
    
    for label in response['Labels']:
        print ("Label: " + label['Name'])
        print ("Confidence: " + str(label['Confidence']))
        print ("----------")
        # ddbResponse = ddb.put_item(Item={
        #     'pk': pk,
        #     'Label' : label['Name'],
        #     'LabelConfidence' : Decimal(str(label['Confidence']))
        # })
        

# --------------- Main handler ------------------

def lambda_handler(event, context):
    
    for record in event['Records']:
       payload=record["body"]
       print(str(payload))
    getLabels()


