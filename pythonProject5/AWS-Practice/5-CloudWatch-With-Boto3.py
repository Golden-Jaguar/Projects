import boto3
import json
import random
from datetime import datetime
AWS_REGION = 'us-east-2'
client = boto3.client('logs', region_name=AWS_REGION)


# # This Code Lists the log groups in the cloudwatch app
# # loggroupnameprefix can be used to filter desired log-groups
# AWS_REGION = "us-east-2"
#
# client = boto3.client('logs', region_name=AWS_REGION)
#
# retention_period_in_days = 5
#
# response = client.describe_log_groups(
#
#     logGroupNamePrefix='/aws/lambda/H'
# )
#
# print(json.dumps(response, indent=4))
#
# for each_line in response['logGroups']:
#     print(each_line["logGroupName"])



# How to update Amazon CloudWatch Log Group using Boto3
response = client.describe_log_groups(logGroupNamePrefix='/aws/lambda/')

print(json.dumps(response['logGroups'][0], indent=4))
# Here we are updating the tags on the specified group
response = client.tag_log_group(
    logGroupName='/aws/lambda/HelloWorld',
    tags={
        'Frequency': '100 Seconds',

    }
)
# Here we are changing the retentionInDays on the specified group
response = client.put_retention_policy(
    logGroupName='/aws/lambda/HelloWorld',
    retentionInDays=7
)

response = client.describe_log_groups(logGroupNamePrefix='/aws/lambda/')

print(json.dumps(response['logGroups'][0], indent=4))



# This code shows how to send logs to Amazon CloudWatch using Boto3

# # Create a log group using Boto3
# retention_period_in_days = 5
# response = client.create_log_group(
#     logGroupName='CRMBackendLogs',
#     tags={
#         'Type': 'Back end',
#         'Frequency': '30 seconds',
#         'Environment': 'Production',
#         'RetentionPeriod': str(retention_period_in_days)
#     }
# )

# # Step 1: Create Log Stream
# client.create_log_stream(
#     logGroupName='CRMBackendLogs',
#     logStreamName='ApplicationLogs'
# )

# Step 2: Put Log Events
messages = 'Syntax Error'
curr_dt = datetime.now()
timestamp = int(round(curr_dt.timestamp() * 1000))
response = client.put_log_events(
    logGroupName='CRMBackendLogs',
    logStreamName='ApplicationLogs',
    logEvents=[
        {
            'timestamp': timestamp,
            'message': 'Syntax Error'
        }
    ]
)
print(response)