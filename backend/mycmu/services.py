
import requests
from django.core.exceptions import ValidationError
from decouple import config

GOOGLE_ID_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'
GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')
def google_validate_id_token(*, id_token: str) -> bool:
    # Reference: https://developers.google.com/identity/sign-in/web/backend-auth#verify-the-integrity-of-the-id-token
    response = requests.get(
        GOOGLE_ID_TOKEN_INFO_URL,
        params={'id_token': id_token}
    )

    if not response.ok:
        raise ValidationError('id_token is invalid.')

    audience = response.json()['aud'] 
    if audience != GOOGLE_CLIENT_ID:
        raise ValidationError('Invalid audience.')

    return True