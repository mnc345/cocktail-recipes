from app.cocktail_recipes import fetch_cocktails

def test_get_vodka():
    drinks = fetch_cocktails("vodka")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_whiskey():
    drinks = fetch_cocktails("whiskey")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_whisky():
    drinks = fetch_cocktails("whisky")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_beer():
    drinks = fetch_cocktails("beer")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_port():
    drinks = fetch_cocktails("port")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_vermouth():
    drinks = fetch_cocktails("vermouth")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_everclear():
    drinks = fetch_cocktails("everclear")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_absinthe():
    drinks = fetch_cocktails("absinthe")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_cider():
    drinks = fetch_cocktails("cider")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_brandy():
    drinks = fetch_cocktails("brandy")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_aperol():
    drinks = fetch_cocktails("aperol")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_wine():
    drinks = fetch_cocktails("wine")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_gin():
    drinks = fetch_cocktails("gin")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_rum():
    drinks = fetch_cocktails("rum")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")

def test_get_tequila():
    drinks = fetch_cocktails("tequila")
    if drinks == "":
        print("TEST FAILED!")
    else:
        print("TEST PASSED")
