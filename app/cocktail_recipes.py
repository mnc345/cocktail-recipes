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
    measurment = drink[key]
    if (ingredient is not None):
        if measurment is not None:
            print(measurment, ingredient)
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

client = SendGridAPIClient("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") #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

subject = "Your Cocktail Recipe is HERE!!"

USER_NAME = os.getenv("USER_NAME", default="Cocktail Lover")
cocktail_choice = random_drink["strDrink"]
drink = id_data["drinks"][0]
instructions = drink["strInstructions"]
ingrediant_one = drink["strIngredient1"]
measurement_one= drink["strMeasure1"]
ingrediant_2 = drink["strIngredient2"]
measurement_2= drink["strMeasure2"]
ingrediant_3 = drink["strIngredient3"]
measurement_3= drink["strMeasure3"]
ingrediant_4 = drink["strIngredient4"]
measurement_4= drink["strMeasure4"]
ingrediant_5 = drink["strIngredient5"]
measurement_5= drink["strMeasure5"]
ingrediant_6 = drink["strIngredient6"]
measurement_6= drink["strMeasure6"]
ingrediant_7 = drink["strIngredient7"]
measurement_7= drink["strMeasure7"]
ingrediant_8 = drink["strIngredient8"]
measurement_8= drink["strMeasure8"]
ingrediant_9 = drink["strIngredient9"]
measurement_9= drink["strMeasure9"]
ingrediant_10 = drink["strIngredient10"]
measurement_10= drink["strMeasure10"]
ingrediant_11 = drink["strIngredient11"]
measurement_11= drink["strMeasure11"]
ingrediant_12 = drink["strIngredient12"]
measurement_12= drink["strMeasure12"]
ingrediant_13 = drink["strIngredient13"]
measurement_13= drink["strMeasure13"]
ingrediant_14 = drink["strIngredient14"]
measurement_14= drink["strMeasure14"]
ingrediant_15 = drink["strIngredient15"]
measurement_15= drink["strMeasure15"]
#this is where the template is not working 
html_content = f"Hello {random}, you chose a cocktail with {liquor}!!, this is the name of your cocktail {cocktail_choice}!!,\n"
html_content += f"instructions:{instructions}"
html_content += f"{request_url}"
html_content += f"These are the ingrediants you need:"
html_content += f"{ingrediant_one}, {measurement_one},\n,{ingrediant_2}, {measurement_2}, \n, {ingrediant_3}, {measurement_3},\n, {ingrediant_4}, {measurement_4},\n,{ingrediant_5}, {measurement_5}, \n, {ingrediant_6}, {measurement_6}, \n , {ingrediant_7}, {measurement_7}, \n ,{ingrediant_8}, {measurement_8}, \n ,{ingrediant_9}, {measurement_9}, \n ,{ingrediant_10}, {measurement_10}, \n ,{ingrediant_11}, {measurement_11}, \n ,{ingrediant_12}, {measurement_12}, \n, {ingrediant_12}, {measurement_12}, \n, {ingrediant_13}, {measurement_13}, \n, {ingrediant_14}, {measurement_14}, \n, {ingrediant_15}, {measurement_15}, \n"

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


