import requests
import send_email

api_key="8c0f46f20ee44bad8d56878f054e2e97"
topic="tesla"

url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2026-02-26&sortBy=publishedAt&" \
       f"apiKey={api_key}&" \
       "language=en"

request = requests.get(url)
content = request.json()

email_message = ""
for article in content["articles"]:
    try:
        email_message = email_message + (article["title"]) + "\n" + (article["description"]) + "\n" + (article["url"] + 2* "\n")
    except TypeError:
       pass
    #print(article["title"])
    # print(article["description"])
    # print(article["url"])


send_email.send_email(
    sender_email="traspo811@gmail.com",
    app_password="gludymxnthvmohff",
    recipient_email="traspo811@gmail.com",
    subject="Today's News!",
    body=str(email_message)
)
