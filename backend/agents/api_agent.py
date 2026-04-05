import requests

def call_api(prompt: str):
    try:
        res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = res.json()
        return f"Bitcoin Price: {data['bpi']['USD']['rate']}"
    except Exception as e:
        return f"API Error: {str(e)}"
