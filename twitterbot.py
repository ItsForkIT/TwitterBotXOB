import sys, os, random, glob, codecs
from twython import Twython

_consumer_key =
_consumer_secret =
_access_token =
_access_token_secret =

_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

_api = Twython(_consumer_key, _consumer_secret, _access_token, _access_token_secret) 

_working_folder = 'Working'
_hashtag = '#DISARMnado'

def randomtweet():
	try:
		_randfile = random.choice(glob.glob1(_working_folder, '*.txt'))

		_format, _ttl, _type, _source, _destination, _lat, _long, _datetime, _group = _randfile.split('_')

		_tweetsfile = codecs.open(os.path.join(_location, _working_folder, _randfile), encoding='utf-8', mode='r')
		_tweetscontents = _tweetsfile.read()
		_tweetsfile.close()

		_status = _hashtag + ' ' + _source + ' ' + _lat + ' ' + _long + ' ' + _datetime + ' ' + _tweetscontents[:70]

		print(_status)

		_api.update_status(status=_status)

		return None

	except IOError:
		return None

randomtweet()
