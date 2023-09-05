import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.eventhubs.com/stats/sf4/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
sf4_tiers = soup.find(id="tiers1")

head = sf4_tiers.find("tr", class_="headerRow")
# get column headers
col_headers = [x.text for x in head.find_all("th", class_="tdgradient")]

body = sf4_tiers.find("tbody")
rows = body.find_all("tr")
# get row data
char_data = []
for row in rows:
    data = row.find_all("td")
    data = [dp.text for dp in data]
    char_data.append(data)

df = pd.DataFrame(char_data, columns=col_headers)
df.to_csv('sf4-char-usage.csv', index=False)

