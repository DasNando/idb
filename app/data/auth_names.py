import json

def path(f):
	return "../scraper/" + f

with open(path("book_test3.json")) as books3_json:
	books3_data = json.load(books3_json)

auths = set()

for search in books3_data['books']:
	for item in search['items']:
		try:
			name = item['volumeInfo']["authors"][0]
			auths.add(name)
		except:
			continue

print(list(auths))
