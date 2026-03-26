import requests

api_key = "rTwSX417C7S9aa2ZqLYNwCBlpVab9uofZZjNvBCM"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
img_url = response.json()["url"]
get_img = requests.get(img_url)

with open("apod.jpg", "wb") as file:
    file.write(get_img.content)