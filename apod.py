import requests
import streamlit as st
import requests

api_key = "rTwSX417C7S9aa2ZqLYNwCBlpVab9uofZZjNvBCM"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
img_url = requests.get(response.json()["url"])
img_title = response.json()["title"]
img_desc = response.json()["explanation"]


with open("pic_of_the_day.jpg", "wb") as file:
    file.write(img_url.content)

st.title(img_title,text_alignment="center")
st.image("pic_of_the_day.jpg", caption="Astronomy Picture of the Day")
st.text(img_desc)
