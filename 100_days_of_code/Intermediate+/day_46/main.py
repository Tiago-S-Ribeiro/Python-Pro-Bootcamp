from spotipy.oauth2 import SpotifyOAuth
from str_formatter import parse_date
from dotenv import load_dotenv
import requests
import spotipy
import bs4
import re
import os
os.system("clear")
#print("\033c")   
load_dotenv()

CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
PATTERN = re.compile("^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$")
SCOPE = "playlist-modify-private"

date_input = input("Which date do you want to travel to (DD/MM/YYYY)?\n").strip()

if PATTERN.match(date_input):
    date = parse_date(date_input)
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
    response.raise_for_status()
    content = response.text

    soup = bs4.BeautifulSoup(content, 'html.parser')
                                                                                                                                    # Alternative
    row_divs = soup.find_all(name="div", class_="o-chart-results-list-row-container")                                               # songs = soup.find_all(name="h3", id="title-of-a-story", class_="u-line-height-normal@mobile-max")
    songs = [song.find(name="h3", id="title-of-a-story").getText().strip() for song in row_divs]                                    # song_titles = [title.getText().strip("\n") for title in songs]
    #song_authors = [artist.find(name="span", class_="u-line-height-normal@mobile-max").getText().strip() for artist in row_divs] 

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, show_dialog=True, cache_path="token.txt"))
    user_id = sp.current_user()["id"]
    song_uris = []
    
    for song in songs:
        json_data = sp.search(q=f"track:{song} year:{date.split('-')[0]}", type="track")
        try:
            uri = json_data["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify.")
    
    playlist = sp.user_playlist_create(user=user_id, name=f"Top 100 Billboard ({date})", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

else:
    print("Invalid date format.")
