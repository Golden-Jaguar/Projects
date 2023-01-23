from twilio.rest import Client

# This function uses twilio sms service to trigger a message when an event happens
# This code was uploaded to aws-lambda with twilio's dependencies gathered in a zip file before uploading
# to capture twilio's dependencies go to cmd and cd into the same directory as the execution file
# then type in cmd 'pip3 install twilio -t .' in order to load it in a specific directory.
def send (event=None, context=None):
    #define your body
    my_body='EC2 Instance Stopped Working'
    #define client
    client = Client('AC08753d6fed6fb24c85d11c11eb01511a', '223db7684f91bb20047a58ed2b6af853')
    message = client.messages \
    .create(
         body='EC2 Instance Stopped Working',
         from_='+12059735986',
         status_callback='http://postb.in/1234abcd',
         to='+14702088645'
     )
    return 'sent message'

send()

# Once this zip file is uploaded to the lambda app on aws, we then create an event-rule on Amazon Event Bridge
# This rule is set to trigger when an EC2 instance changes state, which will intern trigger the lambda function.
