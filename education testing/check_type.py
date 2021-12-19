import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"par1": "value1"})
print(response.text)
print(response.status_code)

responce_2 = requests.post("https://playground.learnqa.ru/api/get_500")
print(responce_2.status_code)
print(responce_2.text)

ressponce_3 = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
#first_resp = response.history[0]
#sec_resp = response
#print(ressponce_3.text)
print(ressponce_3.status_code)
#print(first_resp.url)
#print(sec_resp.url)