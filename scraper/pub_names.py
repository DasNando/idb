import json

def path(f):
	return "../scraper/" + f

with open(path("book_test3.json")) as books3_json:
	books3_data = json.load(books3_json)

pubs = set()

for search in books3_data['books']:
	for item in search['items']:
		try:
			name = item['volumeInfo']["publisher"]
			pubs.add(name)
		except:
			continue

print(list(pubs))
