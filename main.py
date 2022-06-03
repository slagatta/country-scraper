from bs4 import BeautifulSoup
import requests
import json

response = requests.get("https://www.worldometers.info/geography/alphabetical-list-of-countries/")
country_site = response.text
soup = BeautifulSoup(country_site, "html.parser")

country_list = []
table = soup.find("table")

for row in table.tbody.find_all("tr")[1:]:
    # Find all data for each column
    columns = row.find_all("td")
    new_item = {
        "Country": columns[1].getText(),
    }
    country_list.append(new_item)

with open("country_list.json", "w") as f:
    json.dump(country_list, f)
