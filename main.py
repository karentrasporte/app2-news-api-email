import requests

api_key="8c0f46f20ee44bad8d56878f054e2e97"

url = f"https://newsapi.org/v2/everything?q=tesla&from=2026-02-26&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])