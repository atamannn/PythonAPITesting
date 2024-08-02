import json
from Helpers.HttpClient import HttpClient


http_client = HttpClient("hockey1.p.rapidapi.com")
response = http_client.Get("/v1/nhl/teams")

class Teams:
    meta: str

teams = json.loads(response)

teams2 = Teams()
teams2.meta = teams["meta"]["version"]

print(teams2.meta)

b = 1