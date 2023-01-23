import boto3
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import datetime


# Good way to create bucket
# How to name the bucket
# FirstName MiddleName LastName Date
#example: alexwolfgangklotz12082022


# What Files are Available in the current directory
# print(os.listdir())


# Renames the file name.
#os.rename("simplepic.jpg", "shotpic.jpg")


#Specifies what resource you want to use with Boto3
s3 = boto3.resource('s3')


# Print out bucket names in current user profile
# for bucket in s3.buckets.all():
    # print(bucket.name)


# getting the date and time
d = datetime.datetime.now()
# print(d)

# formatting date and time to only include the month, day, and year
current_time = "{}{}{}".format(d.month, d.day, d.year)
# print(current_time)

# Create a client object using the class s3
client = boto3.client('s3')


# this is used to create the s3 bucket
# response = client.create_bucket(
#     ACL='private',
#     Bucket='alexwolfgangklotz{}'.format(current_time),
#     CreateBucketConfiguration={
#         'LocationConstraint': 'us-east-2'
#     }
# )


# This code turns the picture data into binary so the code can be uploaded in that form.
# with open('pic2.PNG', 'rb') as f:
#     data = f.read()
#
# # Upload Files to S3 Bucket using this code
# response = client.put_object(
#     ACL='private',
#     Body=data,
#     Bucket='alexwolfgangklotz{}'.format(current_time),
#     Key='pic2.PNG',
# )
# print(response)

# This code shows how to delete a file on the s3 bucket
# response = client.delete_object(
#     Bucket='alexwolfgangklotz{}'.format(current_time),
#     Key='shotpic.jpg'
# )
# print(response)


# This code shows how to list objects in a bucket
# response = client.list_objects(
#     Bucket='alexwolfgangklotz{}'.format(current_time),
# )
# for x in response.get("Contents", None):
#     print(x.get('Key', None))


# This code will list buckets
response = client.list_buckets()
for x in response.get("Buckets", None):
    print(x.get('Name', None))
    