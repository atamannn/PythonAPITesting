import requests
from Entities.Teams import Teams
class HttpClient:

    BASE_URL = "https://hockey1.p.rapidapi.com/v1/nhl/"

    headers = {
        'x-rapidapi-key': "72181f6b35msh7952d7f58c76fd8p16d1c1jsnb93bb1a6feb7",
        'x-rapidapi-host': "hockey1.p.rapidapi.com"
    }
    def GetTeams(self):
        url = "teams"
        response = requests.get(HttpClient.BASE_URL + url, headers=HttpClient.headers)
        teams = Teams.from_json(response.text)
        return teams