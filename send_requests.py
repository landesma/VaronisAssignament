import requests

endpoint = "http://0.0.0.0:8000"
auth_response = requests.get(endpoint + "/login", params={"username": "lior", "password": "Panda"}).json()
payload = [
    {
        "name": "device",
        "strVal": "iPhone",
        "metadata": "not interesting"
    },
    {
        "name": "isAuthorized",
        "boolVal": "false",
        "lastSeen": "not interesting"
    }
]
normalize_response = requests.post(endpoint + "/normalize", json=payload,
                                   headers={"Authorization": "Bearer " + auth_response["token"]}).json()

print(normalize_response)
