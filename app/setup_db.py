import json

from db import db
from models import Book, Author, Review


def init_db():
	db.drop_all()
	db.create_all()

	count = 0

	with open("test3.json") as test_json:
		test_data = json.load(test_json)

	with open("../scraper/books.json") as books_json:
		books_data = json.load(books_json)

	for item in (books_data["books"] + test_data['items']):
		
		#finding book info
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
			price = str(item["saleInfo"]["retailPrice"]['amount'])
		except:
			price = 'This title is not for sale.'
		try:
			pic = item["volumeInfo"]["imageLinks"]["thumbnail"]
		except:
			print('Error fetching image url')
			pic = 'about:blank'
		book = Book(title, genre, year, isbn, price, pic)
		db.session.add(book)

		count = count + 1

		#finding author info
		try:
			name = item['volumeInfo']["authors"][0]
		except:
			name = 'error fetching author'
		author = Author(True, name, "1/1/1901", "1/1/2001", genre)
		q = db.session.query(Author).filter_by(name=name)
		if not db.session.query(q.exists()).scalar():
			db.session.add(author)
			print('added author with name: ', name)
		else:
			print("couldn't add author with name: ", name)

	db.session.commit()
	print("added ", count, ' books')

init_db()

'''print('~~~~~~~~~~~~~~~~~~~~~~')
print(db.session.query(Book).filter_by(title="Flowers for Algernon").first().title)
print('!!!!!!!!!!!!!!!!!!!!!!')'''
