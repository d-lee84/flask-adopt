import requests
from secrets import API_KEY, SECRET
from random import choice

TOKEN_URL = "https://api.petfinder.com/v2/oauth2/token"
PET_URL = "https://api.petfinder.com/v2/animals?limit=100"


def get_token_request():
    """ make api get request to get an Oauth token"""
    resp = requests.post(TOKEN_URL, data={"grant_type": "client_credentials",
                                          "client_id": API_KEY,
                                          "client_secret": SECRET})
    # breakpoint()
    # print(resp)
    token = resp.json()["access_token"]
    return token


def get_random_pet():
    """ send a get request to get 100 pets,
    randomly choose one and return its name, age and image URL"""
    token = get_token_request()
    resp = requests.get(PET_URL, headers={"Authorization": f"Bearer {token}"})
    pets = resp.json()["animals"]
    random_pet = choice(pets)
    #check if primary photos are empty, return '' if it is empty 
    photos = random_pet.get("photos")
    photo_url = photos[0]["small"] if photos else ""
    return {"age": random_pet["age"],
            "name": random_pet["name"],
            "photo_url": photo_url}
