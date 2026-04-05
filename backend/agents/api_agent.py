import requests

def call_api(prompt):
    return requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
