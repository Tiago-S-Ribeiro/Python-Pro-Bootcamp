import requests
import bs4

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
content = response.text

soup = bs4.BeautifulSoup(content, 'lxml')
h3_tags = soup.find('div') 

image_tags = [img_tag.get("alt") for img_tag in soup.select(selector=".jsx-3523802742.listicle-item img")]

movies = [alt_name for alt_name in image_tags if alt_name != "Amazon"]
movies.reverse()
length = len(movies)

movies_with_ratings = [f"{i+1}) {movies[i]}\n" for i in range(length-1, -1, -1)]
movies_with_ratings.reverse()

with open("top_100_movies.txt", "w") as file:
    file.writelines(movies_with_ratings)
file.close()