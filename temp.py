import requests

# Using the example query "demon".
url = "https://api.consumet.org/manga/mangadex/demon"
response = requests.get(url)
data = response.json()

print(data)
