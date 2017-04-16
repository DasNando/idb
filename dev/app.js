var app = angular.module('sweReaders', ['angularUtils.directives.dirPagination']);

app.controller('BookController', function($scope, $http){

	$scope.sortKey = 'title';
	$scope.reverse = false;
	$scope.searchBooks = '';

	var myUrl = 'https://cs373-idb.appspot.com/api/books/params&genre=Fiction';

	$scope.booklist = [];

	$http.get(myUrl).success(function(data) {
		var myjson = JSON.parse(data);
		$scope.booklist = myjson;
	});


	// $scope.booklist = $http.get("http://cs373-idb.appspot.com/api/books/params&genre=Science");

	// $scope.booklist = [
	// 	{
	// 		coverart: "",
	// 		title: "Ender's Game",
	// 		author: "Orson Scott Card",
	// 		published: "January 15, 1985",
	// 		rating: 4.8,
	// 		publisher: "Publish McPublishson",
	// 		genre: "Good Book",
	// 		isbn: "MAMBO #6",
	// 		prices: "$7?"
	// 	}, {
	// 		coverart: "",
	// 		title: "Slaughterhouse-Five",
	// 		author: "Kurt Vonnegut",
	// 		published: "March 1969",
	// 		rating: 3.9,
	// 		publisher: "Publish McPublishson",
	// 		genre: "Good Book",
	// 		isbn: "MAMBO #3",
	// 		prices: "$9?"
	// 	}, {
	// 		coverart: "",
	// 		title: "The Great Gatsby",
	// 		author: "F Scott Fitzgerald",
	// 		published: "1925",
	// 		rating: 5.0,
	// 		publisher: "Publish McPublishson",
	// 		genre: "Good Book",
	// 		isbn: "MAMBO #5",
	// 		prices: "$10?"
	// 	}, {
	// 		coverart: "1",
	// 		title: "1",
	// 		author: "1",
	// 		published: "1",
	// 		rating: "1",
	// 		publisher: "1",
	// 		genre: "1",
	// 		isbn: "1",
	// 		prices: "1"
	// 	}, {
	// 		coverart: "2",
	// 		title: "2",
	// 		author: "2",
	// 		published: "2",
	// 		rating: "2",
	// 		publisher: "2",
	// 		genre: "2",
	// 		isbn: "2",
	// 		prices: "2"
	// 	}, {
	// 		coverart: "3",
	// 		title: "3",
	// 		author: "3",
	// 		published: "3",
	// 		rating: "3",
	// 		publisher: "3",
	// 		genre: "3",
	// 		isbn: "3",
	// 		prices: "3"
	// 	}, {
	// 		coverart: "4",
	// 		title: "4",
	// 		author: "4",
	// 		published: "4",
	// 		rating: "4",
	// 		publisher: "4",
	// 		genre: "4",
	// 		isbn: "4",
	// 		prices: "4"
	// 	}, {
	// 		coverart: "5",
	// 		title: "5",
	// 		author: "5",
	// 		published: "5",
	// 		rating: "5",
	// 		publisher: "5",
	// 		genre: "5",
	// 		isbn: "5",
	// 		prices: "5"
	// 	}, {
	// 		coverart: "6",
	// 		title: "6",
	// 		author: "6",
	// 		published: "6",
	// 		rating: "6",
	// 		publisher: "6",
	// 		genre: "6",
	// 		isbn: "6",
	// 		prices: "6"
	// 	}, {
	// 		coverart: "7",
	// 		title: "7",
	// 		author: "7",
	// 		published: "7",
	// 		rating: "7",
	// 		publisher: "7",
	// 		genre: "7",
	// 		isbn: "7",
	// 		prices: "7"
	// 	}, {
	// 		coverart: "8",
	// 		title: "8",
	// 		author: "8",
	// 		published: "8",
	// 		rating: "8",
	// 		publisher: "8",
	// 		genre: "8",
	// 		isbn: "8",
	// 		prices: "8"
	// 	}, {
	// 		coverart: "9",
	// 		title: "9",
	// 		author: "9",
	// 		published: "9",
	// 		rating: "9",
	// 		publisher: "9",
	// 		genre: "9",
	// 		isbn: "9",
	// 		prices: "9"
	// 	}, {
	// 		coverart: "10",
	// 		title: "10",
	// 		author: "10",
	// 		published: "10",
	// 		rating: "10",
	// 		publisher: "10",
	// 		genre: "10",
	// 		isbn: "10",
	// 		prices: "10"
	// 	}, {
	// 		coverart: "11",
	// 		title: "11",
	// 		author: "11",
	// 		published: "11",
	// 		rating: "11",
	// 		publisher: "11",
	// 		genre: "11",
	// 		isbn: "11",
	// 		prices: "11"
	// 	}, {
	// 		coverart: "12",
	// 		title: "12",
	// 		author: "12",
	// 		published: "12",
	// 		rating: "12",
	// 		publisher: "12",
	// 		genre: "12",
	// 		isbn: "12",
	// 		prices: "12"
	// 	}
	// ];

	console.log("NIGGA PLEASE WORK: "+$scope.booklist.length);

	$scope.sort = function(keyname){
		if ($scope.sortKey != keyname) {
			$scope.sortKey = keyname;
			$scope.reverse = true;
		};
		$scope.reverse = !$scope.reverse;
	}
});

app.controller('AuthorController', function($scope) {
	$scope.sortKey = 'name';
	$scope.reverse = false;
	$scope.searchAuthors = '';

	$scope.authorlist = [{
		pic: "https://cs373-idb.appspot.com/static/img/authors/authors-static.jpg",
		name: "Sir Writes-alot",
		about: "Literally the greatest.",
		dob: 1969,
		dod: 2020,
		works: "69 MILLION",
	}, {
		pic: "https://cs373-idb.appspot.com/static/img/authors/authors-static.jpg",
		name: "Sir Writes-alot",
		about: "Literally the greatest.",
		dob: 1969,
		dod: 2020,
		works: "68 MILLION",
	}, {
		pic: "https://cs373-idb.appspot.com/static/img/authors/authors-static.jpg",
		name: "Sir Writes-alot",
		about: "Literally the greatest.",
		dob: 1969,
		dod: 2020,
		works: "67 MILLION",
	}, {
		pic: "https://cs373-idb.appspot.com/static/img/authors/authors-static.jpg",
		name: "Sir Writes-alot",
		about: "Literally the greatest.",
		dob: 1969,
		dod: 2020,
		works: "65 MILLION",
	}, {
		pic: "https://cs373-idb.appspot.com/static/img/authors/authors-static.jpg",
		name: "Sir Writes-alot",
		about: "Literally the greatest.",
		dob: 1969,
		dod: 2020,
		works: "66 MILLION",
	}, {
		pic: "https://cs373-idb.appspot.com/static/img/authors/authors-static.jpg",
		name: "Sir Writes-alot",
		about: "Literally the greatest.",
		dob: 1969,
		dod: 2020,
		works: "70 MILLION",
	}];

	$scope.sort = function(keyname){
		if ($scope.sortKey != keyname) {
			$scope.sortKey = keyname;
			$scope.reverse = true;
		};
		$scope.reverse = !$scope.reverse;
	}
});

app.controller('PublisherController', function($scope) {
	$scope.sortKey = 'name';
	$scope.reverse = false;
	$scope.searchPublishers = '';

	$scope.publisherlist = [{
		pic: "1",
		name: "1",
		about: "1",
		headquarters: "1",
		country: "1",
		founded: "1"
	}, {
		pic: "2",
		name: "2",
		about: "2",
		headquarters: "2",
		country: "2",
		founded: "2"
	}, {
		pic: "3",
		name: "3",
		about: "3",
		headquarters: "3",
		country: "3",
		founded: "3"
	}, {
		pic: "1",
		name: "1",
		about: "1",
		headquarters: "1",
		country: "1",
		founded: "1"
	}, {
		pic: "2",
		name: "2",
		about: "2",
		headquarters: "2",
		country: "2",
		founded: "2"
	}, {
		pic: "3",
		name: "3",
		about: "3",
		headquarters: "3",
		country: "3",
		founded: "3"
	}, {
		pic: "1",
		name: "1",
		about: "1",
		headquarters: "1",
		country: "1",
		founded: "1"
	}, {
		pic: "2",
		name: "2",
		about: "2",
		headquarters: "2",
		country: "2",
		founded: "2"
	}, {
		pic: "3",
		name: "3",
		about: "3",
		headquarters: "3",
		country: "3",
		founded: "3"
	}];

	$scope.sort = function(keyname){
		if ($scope.sortKey != keyname) {
			$scope.sortKey = keyname;
			$scope.reverse = true;
		};
		$scope.reverse = !$scope.reverse;
	}
});

app.controller('ReviewController', function($scope) {
	$scope.sortKey = 'name';
	$scope.reverse = false;
	$scope.searchReviews = '';

	$scope.reviewlist = [{
		pic: "1",
		reviewer: "1",
		rating: "1",
		content: "1",
		source: "1",
		book: "1"
	}, {
		pic: "2",
		reviewer: "2",
		rating: "2",
		content: "2",
		source: "2",
		book: "2"
	}, {
		pic: "3",
		reviewer: "3",
		rating: "3",
		content: "3",
		source: "3",
		book: "3"
	}, {
		pic: "1",
		reviewer: "1",
		rating: "1",
		content: "1",
		source: "1",
		book: "1"
	}, {
		pic: "2",
		reviewer: "2",
		rating: "2",
		content: "2",
		source: "2",
		book: "2"
	}, {
		pic: "3",
		reviewer: "3",
		rating: "3",
		content: "3",
		source: "3",
		book: "3"
	}, {
		pic: "1",
		reviewer: "1",
		rating: "1",
		content: "1",
		source: "1",
		book: "1"
	}, {
		pic: "2",
		reviewer: "2",
		rating: "2",
		content: "2",
		source: "2",
		book: "2"
	}, {
		pic: "3",
		reviewer: "3",
		rating: "3",
		content: "3",
		source: "3",
		book: "3"
	}];

	$scope.sort = function(keyname){
		if ($scope.sortKey != keyname) {
			$scope.sortKey = keyname;
			$scope.reverse = true;
		};
		$scope.reverse = !$scope.reverse;
	}
});