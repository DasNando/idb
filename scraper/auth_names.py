import json

def path(f):
	return "../scraper/" + f

with open(path("book_test3.json")) as books3_json:
	books3_data = json.load(books3_json)

with open(path('books.json')) as books_json:
	books_data = json.load(books_json)

auths = set()

for search in (books_data["books"] + books3_data['books']):
	for item in search['items']:
		try:
			for name in item['volumeInfo']["authors"]:
				auths.add(name)
		except:
			continue

print(list(auths))
