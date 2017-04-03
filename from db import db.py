from main import db
from models import Book, Author, Publisher, Review
import json

def init_db():
	db.drop_all()
	db.create_all()

	with open("test3.json") as test_json:
		test_data = json.load(test_json)

	for item in test_data['items']:
		book = Book(item['title'], item['publisher'], item['categories'][0], item['authors'][0], item['publisedDate'], 420, item['industryIdentifiers'][1], item['retailPrice']['amount'], "todo: review goes here")

init_db()
