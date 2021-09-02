import requests

print('Requests version:', requests.__version__, '\n')

google = requests.get("https://www.google.com/")

print(google.text)