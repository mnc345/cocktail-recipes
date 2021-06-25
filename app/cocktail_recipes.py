import os
from dotenv import load_dotenv

from requests.models import encode_multipart_formdata
import requests
import random
import webbrowser
import json

load_dotenv()


valid_selections = ["whiskey", "whisky", "beer", "port", "vermouth", "everclear", "absinthe", "cider", "brandy", "aperol", "wine", "gin", "vodka", "rum", "tequila"]


liquor = input("Please select a liquor type: ").lower()
    
if liquor not in valid_selections:
    print("OOPS! Invalid liquor type. Please try again.")
    exit()
else:
    print(f"Selected liquor: '{liquor}'")
    print("\n")
        
    
    request_url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={liquor}"
    response = requests.get(request_url)
    liquor_data = json.loads(response.text)

    drinks = liquor_data["drinks"]

    while True:
        random_drink = random.choice(drinks)
        print("Cocktail choice:",random_drink["strDrink"])

        user_choice = input("Do you want this type of cocktail? If so, type 'yes' If no, type any key: ").lower()
        if  user_choice == "yes":
            break
            
            print("\n")
    
    drink_id = random_drink["idDrink"]

    request_url_id = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}"
    id_response = requests.get(request_url_id)
    id_data = json.loads(id_response.text)
    

drink = id_data["drinks"][0]

for index in range(1, 15):
    key = "strIngredient"+str(index)
    ingredient = drink[key]
    key = "strMeasure"+str(index)
    measurement = drink[key]
    if (ingredient is not None):
        if measurement is not None:
            print(measurement, ingredient)
        else:
            print(ingredient)
        

        #url = i["strDrinkThumb"]
        #webbrowser.open(url)


liquor

##Email the choice to user 

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
print("SendGrid Code",SENDGRID_API_KEY)

client = SendGridAPIClient("SENDGRID_API_KEY") #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

subject = "Your Cocktail Recipe is HERE!!"

USER_NAME = os.getenv("USER_NAME", default="Cocktail Lover")

cocktail_choice = random_drink["strDrink"]
drink = id_data["drinks"][0]
instructions = drink["strInstructions"]
ingredient_one = drink["strIngredient1"]
measurement_one = drink["strMeasure1"]
ingredient_2 = drink["strIngredient2"]
measurement_2 = drink["strMeasure2"]
ingredient_3 = drink["strIngredient3"]
measurement_3 = drink["strMeasure3"]
ingredient_4 = drink["strIngredient4"]
measurement_4 = drink["strMeasure4"]
ingredient_5 = drink["strIngredient5"]
measurement_5 = drink["strMeasure5"]
ingredient_6 = drink["strIngredient6"]
measurement_6 = drink["strMeasure6"]
ingredient_7 = drink["strIngredient7"]
measurement_7 = drink["strMeasure7"]
ingredient_8 = drink["strIngredient8"]
measurement_8 = drink["strMeasure8"]
ingredient_9 = drink["strIngredient9"]
measurement_9 = drink["strMeasure9"]
ingredient_10 = drink["strIngredient10"]
measurement_10 = drink["strMeasure10"]
ingredient_11 = drink["strIngredient11"]
measurement_11 = drink["strMeasure11"]
ingredient_12 = drink["strIngredient12"]
measurement_12 = drink["strMeasure12"]
ingredient_13 = drink["strIngredient13"]
measurement_13 = drink["strMeasure13"]
ingredient_14 = drink["strIngredient14"]
measurement_14 = drink["strMeasure14"]
ingredient_15 = drink["strIngredient15"]
measurement_15 = drink["strMeasure15"]
#this is where the template is not working 
html_content = f"Hello {USER_NAME}, You chose a cocktail with {liquor}!!, The name of your cocktail is {cocktail_choice}!!"
html_content += f"instructions:{instructions}"
html_content += f"{request_url}"
html_content += f"These are the ingredients you need:"
html_content += f"{ingredient_one}, {measurement_one},\n,{ingredient_2}, {measurement_2}, \n, {ingredient_3}, {measurement_3},\n, {ingredient_4}, {measurement_4},\n,{ingredient_5}, {measurement_5}, \n, {ingredient_6}, {measurement_6}, \n , {ingredient_7}, {measurement_7}, \n ,{ingredient_8}, {measurement_8}, \n ,{ingredient_9}, {measurement_9}, \n ,{ingredient_10}, {measurement_10}, \n ,{ingredient_11}, {measurement_11}, \n ,{ingredient_12}, {measurement_12}, \n, {ingredient_12}, {measurement_12}, \n, {ingredient_13}, {measurement_13}, \n, {ingredient_14}, {measurement_14}, \n, {ingredient_15}, {measurement_15}, \n"

print("HTML:", html_content)
message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

try:
    response = client.send(message)

    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    print(response.body)
    print(response.headers)

except Exception as err:
   print(type(err))
   print(err) 



print("HTML:", html_content)
message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

try:
    response = client.send(message)

    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    print(response.body)
    print(response.headers)

except Exception as err:
   print(type(err))
   print(err) 
