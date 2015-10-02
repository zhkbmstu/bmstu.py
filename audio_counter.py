# coding=utf-8

import random


def gen_artist_track(count, is_use_random_songs_amount=True):
	audios = []
	for i in range(1, count + 1):

		if is_use_random_songs_amount:
			use_range = range(random.randrange(2,15))
		else:
			use_range = range(i)

		for x in use_range:
			audios.append({'artist':'artist %s' % i,'title':'track %s' % i})

	return audios



def display_artist_track(audios):
	for counter, audio in enumerate( audios ):
		print '%s) %s - %s' % (
			counter + 1, audio['artist'], audio['title']
		)


def count_artists(audios):

	artists = [audio['artist'] for audio in audios]

	artists_set = set(artists)	
	artists_songs_amount = []

	for i in artists_set:
		artists_songs_amount.append({'artist': i, 'count': artists.count(i)})
		print "%s (%s)" % (i, artists.count(i)) 


def test_count_artists(audios_count, iterations):
	pass








audios = gen_artist_track(10)

#display_artist_track(audios)

count_artists(audios)
