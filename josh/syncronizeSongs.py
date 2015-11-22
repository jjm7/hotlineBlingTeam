import json
import requests
import urllib


API_KEY = 'RZ1JEQ5GYJZA2J1I7'
BASE = 'http://developer.echonest.com/api/v4/'
ARTIST = 'kanye%20west'
SONG = 'all%20of%20the%20lights'

## Lets do some stupid html requests to get song data
r = urllib.urlopen(BASE +'song/search?api_key='+API_KEY+ '&artist=' + ARTIST + '&title='+SONG)
strucMe = json.load(r)
songID = strucMe['response']['songs'][0]['id']
u = json.load(urllib.urlopen(BASE+'song/profile?api_key='+API_KEY+'&id='+ songID +'&bucket=audio_summary'))
songTempo =u['response']['songs'][0]['audio_summary']['tempo']

#Finnaly have the tempo of the song

print songTempo


