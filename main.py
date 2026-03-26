import requests
import send_email

api_key="8c0f46f20ee44bad8d56878f054e2e97"

url = f"https://newsapi.org/v2/everything?q=tesla&from=2026-02-26&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()

email_message = ""

for article in content["articles"]:
    try:
        email_message = email_message + (article["title"]) + "\n" + (article["description"]) + "\n" + (article["url"] + "\n" + "\n")
    except:
        print(article["title"])
        pass
    # print(article["title"])
    # print(article["description"])
    # print(article["url"])


send_email.send_email(
    sender_email="traspo811@gmail.com",
    app_password="gludymxnthvmohff",
    recipient_email="traspo811@gmail.com",
    subject="Test Email",
    body=str(email_message)
)
