import requests
from base64 import b64encode
from http import HTTPStatus

URL = "https://europe-west1-gibz-informatik.cloudfunctions.net/send_2fa_sms"


def send_token(recipient, length=6, flash=False):
    """
    """
    header = {
        "Authorization": b64encode("19_20.M183.jrost".encode("utf-8")),
        "Content-Type": "application/json",
    }

    body = {"recipient": recipient, "length": length, "flash": flash}

    result = requests.post(URL, headers=header, json=body)

    if result.status_code == HTTPStatus.OK:
        return result.json()["token"]
    return None
