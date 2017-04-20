import re

def clean():
	cleanr = re.compile('<.*?>')
	raw = input('clean: ')
	cleantext = re.sub(cleanr, '', raw)
	print(cleantext)

clean()