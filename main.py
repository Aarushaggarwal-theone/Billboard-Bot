
import requests
import bs4
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

'''
# environment variables on mac
export SPOTIPY_CLIENT_ID='YOUR CLIENT ID FROM SPOTIFY API'
export SPOTIPY_CLIENT_SECRET='YOUR CLIENT SECRET FROM SPOTIFY API'
export SPOTIPY_REDIRECT_URI='https://example.com'

#environment variables on windows

set SPOTIPY_CLIENT_ID='YOUR CLIENT ID FROM SPOTIFY API'
set SPOTIPY_CLIENT_SECRET='YOUR CLIENT SECRET FROM SPOTIFY API'
set SPOTIPY_REDIRECT_URI='https://example.com'

Note: the redirect url is just to test authentication better to keep it at example.com
'''

spotify_image = """

  _____ ____    ___   ______  ____  _____  __ __      ____   ___    ______ 
 / ___/|    \  /   \ |      ||    ||     ||  |  |    |    \ |   \  |      |
(   \_ |  o  )|     ||      | |  | |   __||  |  |    |  o  )|    \ |      |
 \__  ||   _/ |  O  ||_|  |_| |  | |  |_  |  ~  |    |     ||  D  ||_|  |_|
 /  \ ||  |   |     |  |  |   |  | |   _] |___, |    |  O  ||     |  |  |  
 \    ||  |   |     |  |  |   |  | |  |   |     |    |     ||     |  |  |  
  \___||__|    \___/   |__|  |____||__|   |____/     |_____||_____|  |__|  
                                                                           
"""
print("\n\n\n" + spotify_image+ "\n\n\n")

#getting top songs from billboard hot 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/").text

soup = bs4.BeautifulSoup(response, "html.parser")
top = [i.findAll("h3")[0].string.split("\n")[5].split("\t")[5] for i in soup.findAll(class_="o-chart-results-list-row-container")]
spoauth = SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    show_dialog=True,
    open_browser=True,
    cache_path=".cache")

#searching for tracks of the songs from billboard hot 100
sp = spotipy.Spotify(oauth_manager=spoauth)
user_id = sp.current_user()["id"]
search_result = []
for i in range(0, 100):
    try: 
        result = sp.search(q="track:"+top[i], limit=1)['tracks']["items"][0]["uri"]
    except IndexError: 
        pass
    finally:
        search_result.append(result)

#creating playlist and adding songs to the playlist
playlist = sp.user_playlist_create(user=user_id, name=date+" Billboard Hot 100", public=False, description=f'Enjoy a time capsule to {date}')
sp.playlist_add_items(playlist_id=playlist["id"], items=search_result)