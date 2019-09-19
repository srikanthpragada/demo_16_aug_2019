import requests
import sys

code = input("Enter currency code :")
resp = requests.get("https://restcountries.eu/rest/v2/all")

for country in resp.json():
    cl = country['currencies']
    for c in cl:
        if c['code'] == code:
            print(country['name'])
            break

