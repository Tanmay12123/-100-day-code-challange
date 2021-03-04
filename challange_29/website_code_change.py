import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

data = requests.get(URL)
HTML = data.text

soup = BeautifulSoup(HTML, "html.parser")

all_movies = soup.find_all(name = "h3")
print(all_movies)
print(soup.prettify())

# with open("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_29/movies.txt") as movie_storage:
