import urllib.request

fhand = urllib.request.urlopen('https://docs.python.org/3/library/')
for line in fhand:
    print(line.decode().strip())