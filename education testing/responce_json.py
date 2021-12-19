from json.decoder import JSONDecodeError
import requests

payloat = {"name": "Vsevolod"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payloat)
print(response.text)
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")