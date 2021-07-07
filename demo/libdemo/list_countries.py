import requests

URL = "https://restcountries.eu/rest/v2/all"

resp = requests.get(URL)
if resp.status_code != 200:
    print(f"Sorry! Could not get details!")
    exit(1)

countries = resp.json()

for country in sorted(countries, key=lambda c: c['region']):
    print(f"{country['name']:50} {country['region']}")
