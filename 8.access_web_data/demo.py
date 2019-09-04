import urllib.request, urllib.parse, urllib.error
import json
import ssl


api_key = '34b041a422f882244116c2c49cfe9554'
# https://developers.google.com/maps/documentation/geocoding/intro

serviceurl = 'https://api.themoviedb.org/3/movie/popular?api_key=34b041a422f882244116c2c49cfe9554'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = serviceurl 
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

results = js['results']

movies = []
for movie in results:
    movie = Movie()
    movies.append(mo)

print(movies)