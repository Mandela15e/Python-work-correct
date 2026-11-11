from urllib.request import urlopen

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

vastus = urlopen(url)
try:
    baidid = vastus.read()
finally:
    vastus.close()

tekst = baidid.decode("utf-8")

read = tekst.splitlines()

for number, rida in enumerate(read[:10], start=1):
    print(f"{number}: {rida}")
    