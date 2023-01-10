import requests

print(requests.__version__)
result = requests.get("http://www.google.com")
# print(result.status_code)

raw = requests.get("https://raw.githubusercontent.com/marquezp/CMPUT-404-Lab1/main/lab1_script.py")
print(raw.text)