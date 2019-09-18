import requests
import sys

code = input("Enter country code :")
resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
if resp.status_code == 404:
    print("Sorry! Country code is not valid!")
    sys.exit(0)

if resp.status_code != 200:
    print("Sorry! Could not get details of country!")
    sys.exit(0)

details = resp.json()

print("Name       : ", details['name'])
print("Capital    : ", details['capital'])
print("Region     : ", details['region'])
