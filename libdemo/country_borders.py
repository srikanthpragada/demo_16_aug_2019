import requests
import sys

code = input("Enter country code :")
resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()
# build dict of code and name
codes = {}
for c in countries:
    codes[c['alpha3Code']] = c['name']

for country in countries:
    if country['alpha3Code'] == code:
        if len(country['borders']) > 0:
            for b in country['borders']:
                print(codes[b])
        else:
            print("No borders found!")

        break
else:
    print("Sorry! Country code not found!")
