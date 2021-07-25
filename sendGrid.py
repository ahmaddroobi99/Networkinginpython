import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='layla.hamdan1999@gmail.com',
    to_emails='ahmad.droobi1999@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>hi this is my python programm sending this email with help of send Grid</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)