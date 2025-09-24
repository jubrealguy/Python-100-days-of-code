from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
web = res.text
soup = BeautifulSoup(web, "html.parser")

movies = soup.select("h2 strong")
all_movies = [movie.getText() for movie in movies]

with open("movies.txt", mode="w") as file:
    for movie in all_movies[::-1]:
        file.write(f"{movie}\n")
