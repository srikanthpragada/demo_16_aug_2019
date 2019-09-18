import requests
import sys

resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get details of countries!")
    sys.exit(0)

countries = resp.json()
countries = filter(lambda c: c['area'] is not None, countries)

for c in sorted(countries,key=lambda c: c['area'], reverse=True)[:10]:
    print(f"{c['name']:50} {int(c['area']):10d}")