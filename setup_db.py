from main import db
from models import Book, Author, Publisher, Review
import json

def init_db():
	db.drop_all()
	db.create_all()

	with open("test3.json") as test_json:
		test_data = json.load(test_json)

	for item in test_data['items']:
		book = Book(item["volumeInfo"]['title'], item["volumeInfo"]['categories'][0], item["volumeInfo"]['publishedDate'], 420, item["volumeInfo"]['industryIdentifiers'][1]["identifier"], item["saleInfo"]['retailPrice']['amount'])

init_db()
