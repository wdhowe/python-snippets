#!/usr/bin/env python3
"""
Using the requests module against a website to retrieve data
"""

import requests

# XKCD Current Comic JSON API
my_site = "https://xkcd.com/info.0.json"

# Retrieve using GET
print("Sending GET to: " + my_site)
response = requests.get(my_site)

# Extract the JSON object from the response
data = response.json()

# Show http status code on GET
print("Status code is: " + str(response.status_code))

# Show Certain fields from the JSON object
print("\n-- The Current XKCD Comic --")
print("Comic Title: " + data["title"])
print("Comic Text: " + data["alt"])
print("Comic Date: " + data["year"] + "-" + data["month"] + "-" + data["day"])
print("Comic Image URL: " + data["img"])
