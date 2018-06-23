from polls.models import EmailMaster
from .log import log
from social_core.backends.google import GoogleOAuth2


class CustomGoogleAuth2(GoogleOAuth2):
    def auth_extra_arguments(self):
        data = super(CustomGoogleAuth2, self).auth_extra_arguments()
        data['access_type'] = 'offline'
        data['approval_prompt'] = 'force'
        return data


def test(response, **kwargs):
    first_name = response['name']['givenName']
    display_name = response['displayName']
    email = response['emails'][0]['value']

    refresh_token = response['refresh_token']

    EmailMaster.objects.all().delete()
    master = EmailMaster(display_name=display_name, given_name=first_name,
                         refresh_token=refresh_token, email=email)

    log('Google OAuth2 login completed. ', long_message='The result is {}'.format(master), log_level=5)

    master.save()

    return {'emailMaster': master}
