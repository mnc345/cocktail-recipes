
from app.cocktail_recipes import fetch_data
def test_fetch_data():
    results = fetch_data("whiskey")
    assert isinstance(results, list)
    drink = results[0]
    assert "idDrink" in list(drink.keys())