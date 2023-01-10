import requests

print(requests.__version__)
result = requests.get("http://www.google.com")
print(result.status_code)