# coding=utf-8
#audios = ({'artist':'artist1','track':'track1'})

import random

def gen_artist_track(count, dif):
	audios = []
	for i in range(count):
		i+=1

		if dif:
			for x in range(random.randrange(2,15)):
				audios.append({'artist':'artist %s' % i,'title':'track %s' % i})
		else:
			audios.append({'artist':'artist %s' % i,'title':'track %s' % i})

	return audios



def display_artist_track(audios):
	for counter, audio in enumerate( audios ):
		print '%s) %s - %s' % (
			counter + 1, audio['artist'], audio['title']
		)

def count_artists(audios):
	artists = []
	for audio in audios:
		artists.append(audio['artist'])

	artists_set = set(artists)

	for i in artists_set:
		print "%s (%s)" % (i, artists.count(i)) 




audios = gen_artist_track(10, True)

#display_artist_track(audios)

"""Будет ли адекватно писать так?"""
#display_artist_track(gen_artist_track())

count_artists(audios)