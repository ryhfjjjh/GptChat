import requests
from bs4 import BeautifulSoup

url = "https://massaget.kz/madeniet/til/67389/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text()
with open("dataset/texts/massaget1.txt", "w", encoding="utf-8") as f:
    f.write(text)
