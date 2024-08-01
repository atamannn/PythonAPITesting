import http.client

class HttpClient:
    url = ""
    def __init__(self, url):
        self.url = url
    
    def Get(self, path):
        headers = {
        'x-rapidapi-key': "72181f6b35msh7952d7f58c76fd8p16d1c1jsnb93bb1a6feb7",
        'x-rapidapi-host': "hockey1.p.rapidapi.com"
        }
        conn = http.client.HTTPSConnection(self.url)

        conn.request("GET", path, headers=headers)

        res = conn.getresponse()
        return res.read().decode("utf-8")
    
    def Test(a, b):
        return b+1