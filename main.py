import requests

from Entities.Teams import Teams
from Helpers.HttpClient import HttpClient
BASE_URL = "https://hockey1.p.rapidapi.com/v1/nhl/teams"
http_client = HttpClient("hockey1.p.rapidapi.com")

headers = {
            'x-rapidapi-key': "72181f6b35msh7952d7f58c76fd8p16d1c1jsnb93bb1a6feb7",
            'x-rapidapi-host': "hockey1.p.rapidapi.com"
          }
response = requests.get(BASE_URL, headers=headers)
teams = Teams.from_json(response.text)

def test_teams_meta():
    assert teams.meta.version == "v1.0"

    b = 1