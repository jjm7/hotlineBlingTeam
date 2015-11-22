import json
import requests
import urllib
import echonest.remix.audio as audio
from pyechonest import config

API_KEY = 'RZ1JEQ5GYJZA2J1I7'
BASE = 'http://developer.echonest.com/api/v4/'
ARTIST = 'drake'
SONG = 'hotline%20bling'

FILE_NAME = 'Drake - Hotline Bling.mp3'

config.ECHO_NEST_API_KEY=API_KEY

#ARTIST = 'kanye%20west'
#SONG = 'all%20of%20the%20lights'

## Lets do some stupid html requests to get song data
r = urllib.urlopen(BASE +'song/search?api_key='+API_KEY+ '&artist=' + ARTIST + '&title='+SONG)
strucMe = json.load(r)
songID = strucMe['response']['songs'][0]['id']
u = json.load(urllib.urlopen(BASE+'song/profile?api_key='+API_KEY+'&id='+ songID +'&bucket=audio_summary'))
songTempo =u['response']['songs'][0]['audio_summary']['tempo']

#Finnaly have the tempo of the song

print u

# Easy around wrapper mp3 decoding and Echo Nest analysis
audio_file = audio.LocalAudioFile(FILE_NAME)

# You can manipulate the beats in a song as a native python list
beats = audio_file.analysis.beats
beats.reverse()

# And render the list as a new audio file!
audio.getpieces(audio_file, beats).encode("backwards.mp3")
            


