from Helpers.HttpClient import HttpClient


http_client = HttpClient("hockey1.p.rapidapi.com")
response = http_client.Get("/v1/nhl/schedule?date=2024-01-25")


c = http_client.Test(1)

b = 1