import os
import sys
import datetime
import time
import boto3

print(sys.path)
print(os.getcwd())
# Used aws cli through cmd to upload table information on Dynamo DB on the aws
# 1 I had to upload the aws cli to my cmd using "pip install awscli"
# 2 I installed boto3 to my cmd using "pip install boto3"
# 3 I went into my aws account, created a user with access with IAM and created a table through DynamoDB
# 4 I configured the aws cli in my cmd to the specific aws user with access key ID and the secret key: "aws configure"
# 5 I ran the code on the windows cmd.
# commands for DynamoDB are at: https://docs.aws.amazon.com/cli/latest/reference/dynamodb/index.html
db = boto3.resource('dynamodb')
table = db.Table('employees')

# appends data to table in DynamoDB
# table.put_item(
#     Item={
#         'emp_id': '2',
#         'name': "John",
#         'Age': '24',
#     }
# )

# Getting Data on AWS DynamoDB Python Boto 3
# response = table.get_item(
#     Key={
#         "emp_id": '2'
#
#     }
# )
#
# print(response['Item'])

# Populating DynamoDB using classes and uploading them with Boto3


class MyDB(object):
    def __init__(self, Table_Name ='employees'):
        self.Table_Name = Table_Name
        self.db = boto3.resource('dynamodb')
        self.table = self.db.Table(Table_Name)
        self.client = boto3.client('dynamodb')

    def get(self, emp_id='1'):
        response = table.get_item(
            Key={
                "emp_id": emp_id

            }
        )
        return response

    def put(self, emp_id='', name='', Age=''):
        self.table.put_item(
            Item={
                'emp_id': emp_id,
                'name': name,
                'Age': Age,
            }
        )

    def delete(self, emp_id=''):
        self.table.delete_item(
            Key={
                'emp_id': emp_id
            }
        )
    def describe_table(self):
        response = self.client.describe_table(
            TableName='employees'
        )
        return response


# creates an object from the class MyDB() and prints the details in JSON to the console
obj = MyDB()
print(obj.describe_table())


# Injects data into the table on DynamoDB
resp = obj.put(emp_id='1', Age='25', name='John Hancock')
resp