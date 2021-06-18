import os
from dotenv import load_dotenv
import requests

load_dotenv()

COCKTAIL_API = os.getenv("COCKTAIL_API")

liquor = input("Please select a liquor type: ")
print(f"SELECTED LIQUOR: '{liquor}'")

request_url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={liquor}"

response = requests.get(request_url)
print(type(response))
print(response.text)