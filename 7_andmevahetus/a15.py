from urllib.request import urlopen

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

vastus = urlopen(url)
try:
    baidid = vastus.read()
finally:
    vastus.close()

tekst = baidid.decode("utf-8")

read = tekst.splitlines()

ridu = len(read)
sonu = len(tekst.split())
tahemarke = len(tekst)

tuhje_ridu = 0
for rida in read:
    if rida.strip() == "":
        tuhje_ridu += 1

print("Veebiteksti statistika")
print("----------------------")
print(f"Ridu: {ridu}")
print(f"Sõnu: {sonu}")
print(f"Tähemärke: {tahemarke}")
print(f"Tühje ridu: {tuhje_ridu}")