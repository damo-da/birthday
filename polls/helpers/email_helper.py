from __future__ import print_function
import httplib2
import oauth2client
from oauth2client import client, tools
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery
from mysite import settings
from polls.models import EmailMaster
from .log import log

__all__ = ['send_email']


def get_credentials():
    emailPerson = EmailMaster.objects.first()
    credentials = oauth2client.client.GoogleCredentials('', settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
                                                        settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
                                                        emailPerson.refresh_token, '',
                                                        'https://accounts.google.com/o/oauth2/token', '')

    return credentials


def SendMessageInternal(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
        return "Error"


def CreateMessageHtml(sender, to, subject, msgHtml):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    # msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(msgHtml, 'html', _charset='utf-8'))
    return {'raw': base64.urlsafe_b64encode(msg.as_string())}


def send_email(sender, to, subject, msgHtml):
    message = 'Sending email from {} to {}...'.format(sender, to)
    log(message, log_level=2)

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())

    service = discovery.build('gmail', 'v1', http=http)

    message1 = CreateMessageHtml(sender, to, subject, msgHtml)

    result = SendMessageInternal(service, "me", message1)

    log('result: {}'.format(result), log_level=2)

    return message
