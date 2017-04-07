import db
from flask_restful import Api, Resource
from models import Book, Author, Publisher, Review

db1 = db.db
api = Api(db.app)


class Q_Books(Resource):
    def get(self, q_genre):
        return db1.session.query(Book).filter_by(genre=q_genre)


api.add_resource(Q_Books, '/<string:genre>')