# Cloud-Platform-Development
The purpose of this coursework was to develop and test a cloud-based solution to a given problem 
using appropriate cloud services and technology. I had to implement an image recognition
solution using AWS Rekognition. 

# Specification
The application should be implemented using Python and the Boto3 Amazon Web Services (AWS)
SDK. I also required to setup IAM roles and policies for implementing the solution. The following 
steps had to be implemented:

1. The file 'S3_functions' contains the console program which can upload and download images
   from S3

2. The upload of an image to S3 must send a message to the SQS queue

3. A message in the SQS queue must trigger the Lambda function.

4. Lambda function: 

    4.1 The function on receiving the message must parse it to extract
        the relevant information such as image name etc.

    4.2 The image details must be sent using an appropriate call to the
        AWS Rekognition service to obtain image labels.

    4.3 The information returned from Rekognition must be processed to
        extract image label data but only a maximum of five labels per
        image should be used.

    4.4 DynamoDB database should have a single table with only a
        single partition (primary) key as image name. Only the first five
        labels received from Rekognition service should to be stored in
        the table.
