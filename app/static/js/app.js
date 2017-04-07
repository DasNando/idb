(function() {
	var app = angular.module('sweReaders', []);

	app.controller('BookController', function() {
		this.books = booklist;
	});

	var booklist = [
		{
			coverart: "{{ url_for('static', filename='img/books/books-ender.jpg') }}",
			title: "Ender's Game",
			author: "Orson Scott Card",
			published: "January 15, 1985",
			rating: "4.9/5",
			publisher: "Publish McPublishson",
			genre: "Good Book",
			isbn: "MAMBO #5",
			prices: "$10?"
		}, {
			coverart: "{{ url_for('static', filename='img/books/books-ender.jpg') }}",
			title: "Slaughterhouse-Five",
			author: "Kurt Vonnegut",
			published: "March 1969",
			rating: "4.8/5",
			publisher: "Publish McPublishson",
			genre: "Good Book",
			isbn: "MAMBO #5",
			prices: "$10?"
		}, {
			coverart: "{{ url_for('static', filename='img/books/books-ender.jpg') }}",
			title: "The Great Gatsby",
			author: "F Scott Fitzgerald",
			published: "1925",
			rating: "4.8/5",
			publisher: "Publish McPublishson",
			genre: "Good Book",
			isbn: "MAMBO #5",
			prices: "$10?"
		}, {
			coverart: "{{ url_for('static', filename='img/books/books-ender.jpg') }}",
			title: "TEST TITLE",
			author: "TEST AUTHOR",
			published: "TEST DATE",
			rating: "TEST RATING",
			publisher: "TEST PUBLISHER",
			genre: "TEST GENRE",
			isbn: "TEST ISBN",
			prices: "TEST PRICES"
		}, {
			coverart: "{{ url_for('static', filename='img/books/books-ender.jpg') }}",
			title: "TEST TITLE",
			author: "TEST AUTHOR",
			published: "TEST DATE",
			rating: "TEST RATING",
			publisher: "TEST PUBLISHER",
			genre: "TEST GENRE",
			isbn: "TEST ISBN",
			prices: "TEST PRICES"
		}, {
			coverart: "{{ url_for('static', filename='img/books/books-ender.jpg') }}",
			title: "TEST TITLE",
			author: "TEST AUTHOR",
			published: "TEST DATE",
			rating: "TEST RATING",
			publisher: "TEST PUBLISHER",
			genre: "TEST GENRE",
			isbn: "TEST ISBN",
			prices: "TEST PRICES"
		}
	];

})();