from urllib import request

url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quotes():
    response = request.get(url)
    if response.status_code == 200:
        quote = response.json()
        return quote