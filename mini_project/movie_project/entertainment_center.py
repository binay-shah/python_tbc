import media
import urllib.request, urllib.parse, urllib.error
import json
import ssl
import fresh_tomatoes


YOUTUBE_WEB_URL = "https://www.youtube.com/watch?v="
api_key = '34b041a422f882244116c2c49cfe9554'
IMAGE_BASE_URL = "http://image.tmdb.org/t/p/w185"
# https://developers.google.com/maps/documentation/geocoding/intro

popular_movies_url = 'https://api.themoviedb.org/3/movie/popular?api_key=34b041a422f882244116c2c49cfe9554'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(popular_movies_url, context=ctx)
data = uh.read().decode()

try:
    js = json.loads(data)
except:
    js = None

results = js['results']
#print(results)


movies = []

for movie in results:	
    movie_videos_url = 'https://api.themoviedb.org/3/movie/{}/videos?api_key=34b041a422f882244116c2c49cfe9554'.format(movie['id'])
    
    video_response = urllib.request.urlopen(movie_videos_url, context=ctx)
    data = video_response.read().decode()
    js = json.loads(data)
    
    trailer_url = YOUTUBE_WEB_URL + js['results'][0]['key']
    image_path = IMAGE_BASE_URL + movie['poster_path']
    obj =  media.Movie(movie['title'], movie['overview'], image_path, trailer_url)
    movies.append(obj)
    
    
fresh_tomatoes.open_movies_page(movies)


#movie = media.Movie()