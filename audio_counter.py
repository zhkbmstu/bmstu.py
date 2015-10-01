# coding=utf-8
#audios = ({'artist':'artist1','track':'track1'})

def gen_artist_track(count):
	audios = []
	for i in range(count):
		i+=1
		audios.append(
			{
			'artist':'artist %s' % i,
			'title':'track %s' % i
			}
		)

	return audios

def display_artist_track(audios):
	for counter, audio in enumerate( audios ):
		print '%s) %s - %s' % (
			counter + 1, audio['artist'], audio['title']
		)

""" Генерируем 10 исполнителей и столько же названий треков"""
audios = gen_artist_track(10)

""" Выводим всех исполнителей и название треков"""
display_artist_track(audios)