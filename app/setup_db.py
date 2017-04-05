from main import db
from models import Book, Author, Publisher, Review
import json

def init_db():
	db.drop_all()
	db.create_all()

	with open("test3.json") as test_json:
		test_data = json.load(test_json)

	'''for item in test_data['items']:
		book = Book(item["volumeInfo"]['title'], item["volumeInfo"]['categories'][0], item["volumeInfo"]['publishedDate'], 69, item["volumeInfo"]['industryIdentifiers'][1]["identifier"], item["saleInfo"]['retailPrice']['amount'])
		db.session.add(book)'''

	with open("../scraper/books.json") as books_json:
		books_data = json.load(books_json)

	for item in books_data["books"] + test_data[items]:
		try:
			title = item["volumeInfo"]['title']
		except:
			title = 'error fetching title'
		try:
			genre = item["volumeInfo"]['categories'][0]
		except:
			genre = 'error fetching genre'
		try:
			year = item["volumeInfo"]['publishedDate']
		except:
			year = 'error fetching year'
		try:
			isbn = item["volumeInfo"]['industryIdentifiers'][1]["identifier"]
		except:
			isbn = 'error fetching isbn'
		try:
			price = item["saleInfo"]["retailPrice"]['amount']
		except:
			price = 0
		book = Book(title, genre, year, 420, isbn, price)
		db.session.add(book)

	db.session.commit()

init_db()

print('~~~~~~~~~~~~~~~~~~~~~~')
print(db.session.query(Book).filter_by(title="Flowers for Algernon").first().title)
print('!!!!!!!!!!!!!!!!!!!!!!')
