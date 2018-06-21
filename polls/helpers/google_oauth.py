from polls.models import EmailMaster


def test(backend, response, **kwargs):
    access_token = response['access_token']
    first_name = response['name']['givenName']
    display_name = response['displayName']
    email = response['emails'][0]['value']

    refresh = backend.refresh_token_params(token=access_token)
    refresh_token = refresh['refresh_token']

    EmailMaster.objects.all().delete()
    master = EmailMaster(display_name=display_name, given_name=first_name,
                         refresh_token=refresh_token, email=email)

    master.save()

    return {'emailMaster': master}
