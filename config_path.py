import os
import json

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
creds_path = os.path.join(str(BASE_PATH), "config", "credentials.json")

with open(creds_path, "r") as file:
    creds = json.load(file)

PASSWORD = creds["password"]
USERNAME = creds["username"]
