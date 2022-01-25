import bs4
import requests

response = requests.get("https://news.ycombinator.com/newest")
content = response.text

soup = bs4.BeautifulSoup(content, 'html.parser')
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article in articles:
    print("\n")
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

max_val = max(article_upvotes)
max_val_index = article_upvotes.index(max_val)

print(article_texts[max_val_index])
print(article_links[max_val_index])
print(max_val)