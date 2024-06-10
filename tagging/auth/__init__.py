from datetime import timedelta

from cachier import cachier
import requests

from .key import API_KEY, SECRET_KEY


@cachier(stale_after=timedelta(days=30))
def get_access_token() -> str:

    # !!! CORE SECRET !!!
    api_key = API_KEY
    secret_key = SECRET_KEY
    url = (
        "https://aip.baidubce.com/oauth/2.0/token"
        "?grant_type=client_credentials&"
        f"client_id={api_key}&client_secret={secret_key}"
    )

    payload = ""
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload, timeout=10)

    return response.json().get("access_token")
