import requests

URL = "https://europe-west1-gibz-informatik.cloudfunctions.net/send_2fa_sms"


def request_token(recipient, length=8, flash=True):
    """
    """
    header = {
        "Authorization": b64encode("19_20.M183.jrost".encode("utf-8")),
        "Content-Type": "application/json",
    }

    body = {"recipient": recipient, "length": length, "flash": flash}

    result = requests.post(URL, headers=header, json=body)
