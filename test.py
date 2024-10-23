import requests

tuman = input("viloyatni kiriting: ")
url = f"https://islomapi.uz/api/present/week?region={tuman}"

response = requests.get(url=url).json()
print(response)
