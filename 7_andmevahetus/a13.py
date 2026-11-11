from urllib.request import urlopen

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

vastus = urlopen(url)
try:
    baidid = vastus.read()
finally:
    vastus.close()

tekst = baidid.decode("utf-8")

print(tekst)