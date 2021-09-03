# 1. Version of requests
# https://www.codegrepper.com/code-examples/python/print+version+of+requests+python
# by Bored Coder
# 2. Resquests to a url page
# https://stackoverflow.com/a/15869929
# By Alex K

import requests

print('Requests version:', requests.__version__, '\n')

google = requests.get("https://www.google.com/")

print(google.text, '\n')

git = requests.get("https://raw.githubusercontent.com/kingfxj/404Lab1/master/1.py")

f = open('1.py', 'w')
f.write(git.text)
f.close()

print('Source code:\n' + git.text)
