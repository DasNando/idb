var app = angular.module('sweReaders', ['angularUtils.directives.dirPagination']);

app.controller('BookController', function($scope, $http){

	$scope.sortKey = 'title';
	$scope.reverse = false;
	$scope.searchBooks = '';

	var myUrl = 'https://cs373-idb.appspot.com/api/books/params&genre=Fiction';

	$scope.booklist = [];

	$http.get(myUrl).success(function(data) {
		var myjson = data/*JSON.parse(data)*/;
		$scope.booklist = myjson;
	});

	$scope.searchFilter = function (obj) {
        var re = new RegExp($scope.searchBooks, 'i');
        return !$scope.searchBooks || re.test(obj.title) || re.test(obj.author) || re.test(obj.year) || re.test(obj.publisher) || re.test(obj.rating) || re.test(obj.genre);
    };

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