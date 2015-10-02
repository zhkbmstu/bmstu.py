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
			for x in range(i):
				audios.append({'artist':'artist %s' % i,'title':'track %s' % i})

	return audios



def display_artist_track(audios):
	for counter, audio in enumerate( audios ):
		print '%s) %s - %s' % (
			counter + 1, audio['artist'], audio['title']
		)

def count_artists(audios, test):
	artists = []
	for audio in audios:
		artists.append(audio['artist'])

	artists_set = set(artists)	
	test_arr = []

	for i in artists_set:
		if test:
			test_arr.append({'artist': i, 'count': artists.count(i)})
		else:
			print "%s (%s)" % (i, artists.count(i)) 
	if test: return test_arr

def test_count_artists(audios_count, iterations):
	"""Фунеция писалась в 4 часа утра. За извращенство понять и простить"""
	result = False
	#Пробегаемся по кол-во нужных проверок
	for iteration in range(iterations):
		count = audios_count
		audios = gen_artist_track(count, False) #Генерируем аудио список с выключенной рандомизацией
		#это означает, что у первого артиста будет 1 трек, у 2-ого два и т.д.
		count = count_artists(audios, True) # Делаем подсчет с включенным тест режимом (отдает результыт в виде массива, а не выводит на экран)

		#Сама проверка
		for i in range(audios_count):
			i+=1
			for c in count:
				if c['count'] == i:result = True

	print "%s" % result








audios = gen_artist_track(10, True)

#display_artist_track(audios)

"""Будет ли адекватно писать так?"""
#display_artist_track(gen_artist_track())

count_artists(audios, False)
test_count_artists(5,1)