# Billboard-Bot
A python bot that extracts the songs in the Billboard Hot 100 list of a date you choose, and creates a spotify playlist

## To use this bot you need to authenticate the spotify api

Go to https://developer.spotify.com/dashboard/applications and create an app and get the client ID and secret
Set up a redirect url

##create environment variables using the id and secret

#### environment variables on mac
export SPOTIPY_CLIENT_ID='YOUR CLIENT ID FROM SPOTIFY API'
export SPOTIPY_CLIENT_SECRET='YOUR CLIENT SECRET FROM SPOTIFY API'
export SPOTIPY_REDIRECT_URI='https://example.com'

###environment variables on windows

set SPOTIPY_CLIENT_ID='YOUR CLIENT ID FROM SPOTIFY API'
set SPOTIPY_CLIENT_SECRET='YOUR CLIENT SECRET FROM SPOTIFY API'
set SPOTIPY_REDIRECT_URI='https://example.com'

Note: the redirect url is just to test authentication better to keep it at example.com
