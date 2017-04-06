import json

from db import db
from models import Book, Author, Review, Publisher

def path(f):
	return "../scraper/" + f

def init_db():
	db.drop_all()
	db.create_all()

	with open(path("test3.json")) as test_json:
		test_data = json.load(test_json)

	with open(path("books.json")) as books_json:
		books_data = json.load(books_json)

	with open(path("reviews.json")) as reviews_json:
		review_data = json.load(reviews_json)

	with open(path("authors.json")) as authors_json:
		author_data = json.load(authors_json)

	books = 0
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

		books = books + 1		

		#publisher info
		try:
			name = item['volumeInfo']["publisher"]
		except:
			name = 'error fetching publisher'
		publisher = Publisher(name, "founding date unknown", "New York", "USA", "founders unknown")
		q = db.session.query(Publisher).filter_by(name=name)
		if not db.session.query(q.exists()).scalar():
			db.session.add(publisher)
		else:
			print('Unable to add publisher with name: ', name)

	#review initialization
	reviews = 0
	for item in review_data['reviews']:
		try:
			name = item['reviewer']
		except:
			name = 'unknown reviewer'
		try:
			rating = item['rating']
		except:
			rating = 'unknown rating'
		try:
			content = item['review']
		except:
			content = 'no content'
		try:
			source = item['source']
		except:
			source = 'unknown source'

		reviews = reviews + 1
		review = Review(name, rating, content, source)
		db.session.add(review)

	authors = 0
	for item in author_data['authors']:
		try:
			name = item["name"]
			print('found author: ', name)
		except:
			name = 'Something has gone horribly wrong and we were, sadly, unable to fetch the name for this author.'
			print('failed to find author')
		try:
			image = item["image_url"]
		except:
			image = "about:blank"
		try:
			about = item["about"]
		except:
			about = ''
		try:
			num_works = str(item["works_count"])
		except:
			num_works = '0'
		try:
			birthday = item["birthdate"]
		except:
			birthday = ''
		try:
			deathday = item['deathdate']
		except:
			deathday = ''

		author = Author(name, birthday, deathday, pic, about, num_works)
		q = db.session.query(Author).filter_by(name=name)
		if not db.session.query(q.exists()).scalar():
			db.session.add(author)
			authors = authors + 1
			print('added author with name: ', name)
		else:
			print("couldn't add author with name: ", name)

	db.session.commit()
	print("added ", books, ' books')
	print('added ', authors, ' authors')
	print('added ', reviews, ' reviews')

init_db()
