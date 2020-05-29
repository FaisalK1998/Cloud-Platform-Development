import boto3
s3 = boto3.client('s3')
import os
import logging
from botocore.exceptions import ClientError
from tkinter import filedialog
from tkinter import *

### FUNCTIONS ###

def display_title_bar():

    # Clears the terminal before displaying the title bar
    os.system('cls')

    print("\t************************************")
    print("\t       *** S3 Functions ***         ")
    print("\t************************************")


def get_user_choice():
    """
    Lets the user know what they can do
    """
    print("\n[1] Upload a File to S3")
    print("[2] Download a file from S3")
    print("[3] List all files from S3 bucket")
    print("[4] List all buckets from S3")
    print("[5] Quit")

    return input("What would you like to do? ")


def upload_file(file_name, bucket, object_name):
    """
    Function to upload a file to an S3 bucket
    """
    
    # Upload file
    try:
        response = s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False

    return True


def download_file(file_name, file_location):
    """
    Function to download a given file from an S3 bucket
    """

    try:
        s3_resource = boto3.resource('s3')
        s3_resource.Bucket('cpd-coursework2020').download_file(file_name, file_location)
    except ClientError as e:
        logging.error(e)
        return False
    
    return True

def list_files():
    """
    Function to list files in a given S3 bucket
    """

    s3_resource = boto3.resource('s3')

    for bucket in s3_resource.buckets.all():
        print(bucket.name)
        print("---")
        for item in bucket.objects.all():
            print("\t%s" % item.key)


def list_buckets():
    """
    Function to list all buckets in S3
    """

    response = s3.list_buckets()

    print('Existing buckets: ')
    for bucket in response['Buckets']:
        print(f'    {bucket["Name"]}')


### CONSOLE ###

# Setting what each choice does
choice = ''
display_title_bar()
while choice != '5':

    choice = get_user_choice()

    #Respond to the user's choice
    display_title_bar()
    if choice == '1':
        print("\nSelect a file to upload\n")

        #Tkinter is used to grab the file to upload to S3 via a pop up file dialog
        root = Tk()
        root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("jpeg files","*.jpg"), ("png files","*.png")))
        print(root.filename)

        if root.filename == '':
            print("Error!! Please select a file to upload")
            root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("jpeg files","*.jpg"), ("png files","*.png")))
            print(root.filename)

        #object_name set to the input by the user
        object_name = input("Enter a file name: ")
        while object_name == "":
            print("Error!! Please enter a file name")
            object_name = input("\nEnter a file name: ")
        
        if object_name != "" and object_name.endswith(".jpg") or object_name.endswith("png"):
            print("Successfully uploaded file: " + object_name + " to S3 bucket")
            upload_file(root.filename, 'cpd-coursework2020', object_name)
        else:
            print("Please enter a file type!! (.jpg or .png)")
            object_name = input("\nEnter a file name: ")
    
    elif choice == '2':
        list_files()
        file_name = input("\nEnter a file to download: ")

        while file_name == "":
            print("\nError!! Please enter a file name to download\n")
            file_name = input("Enter a file to download: ")
        
        if file_name != "" and file_name.endswith(".jpg") or file_name.endswith("png"):
            print("Successfully downloaded file: " + file_name + "\nCheck your desktop")
            download_file(file_name, '/Users/faisa/Desktop/'+ file_name)
        else:
            print("Please enter a file type!! (.jpg or .png)")
            file_name = input("\nEnter a file to download: ")
    
    elif choice == '3':
        print("\nAll files listed below\n")
        list_files()
    
    elif choice == '4':
        print("\nAll buckets listed below\n")
        list_buckets()

    elif choice == '5':
        print("\nGoodbye\n")
    
    else:
        print("\nPlease enter a valid choice.\n")
