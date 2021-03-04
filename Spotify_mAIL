import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.billboard.com/charts/hot-100"

data = requests.get(URL)
HTML = data.text

soup = BeautifulSoup(HTML, "html.parser")

all_songs = soup.find_all(
    name="span", class_="chart-element__information__song text--truncate color--primary")
song_names = [song.getText() for song in all_songs]

MY_EMAIL = "2005010025@orchids.edu.in"
MY_PASSWORD = "welcome@123"

top_10_songs = []
for i in range(10):
    song = song_names[i]
    top_10_songs.append(song)

top_10_songs = '\n'.join(top_10_songs)
# print(top_10_songs)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="mutalikdesaitanmay@gmail.com",
        msg=f"Subject:Hey Man! Spotify Feeds Here\n\nHere are top 10 best songs of this week:\n\n {top_10_songs} \n\nTo:  Pytan")
