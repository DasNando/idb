var app = angular.module('sweReaders', ['angularUtils.directives.dirPagination']);

app.controller('BookController', function($scope, $http){

	$scope.sortKey = 'title';
	$scope.reverse = false;
	$scope.searchBooks = '';

	var myUrl = 'https://cs373-idb.appspot.com/api/books/all/';

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

app.controller('AuthorController', function($scope, $http) {
	$scope.sortKey = 'name';
	$scope.reverse = false;
	$scope.searchAuthors = '';

	var myUrl = 'https://cs373-idb.appspot.com/api/authors/all/';

	$scope.authorlist = [];

	$http.get(myUrl).success(function(data) {
		var myjson = data/*JSON.parse(data)*/;
		$scope.authorlist = myjson;
		angular.forEach($scope.authorlist, function (author) {
			author.num_works = parseInt(author.num_works);
		});
	});

	$scope.searchFilter = function (obj) {
		var re = new RegExp($scope.searchAuthors, 'i');
		return !$scope.searchAuthors || re.test(obj.name) || re.test(obj.birth_date) || re.test(obj.death_date) || re.test(obj.num_works);
	};

	$scope.sort = function(keyname){
		if ($scope.sortKey != keyname) {
			$scope.sortKey = keyname;
			$scope.reverse = true;
		};
		$scope.reverse = !$scope.reverse;
	};
});

app.controller('PublisherController', function($scope, $http) {
	$scope.sortKey = 'name';
	$scope.reverse = false;
	$scope.searchPublishers = '';

	var myUrl = 'https://cs373-idb.appspot.com/api/publishers/all/';

	$scope.publisherlist = [];

	$http.get(myUrl).success(function(data) {
		var myjson = data/*JSON.parse(data)*/;
		$scope.publisherlist = myjson;
	});

	$scope.searchFilter = function (obj) {
		var re = new RegExp($scope.searchPublishers, 'i');
		return !$scope.searchPublishers || re.test(obj.name) || re.test(obj.country) || re.test(obj.headquarters) || re.test(obj.founding_date);
	};

	$scope.sort = function(keyname){
		if ($scope.sortKey != keyname) {
			$scope.sortKey = keyname;
			$scope.reverse = true;
		};
		$scope.reverse = !$scope.reverse;
	}
});

app.controller('ReviewController', function($scope, $http) {
	$scope.sortKey = 'reviewer';
	$scope.reverse = false;
	$scope.searchReviews = '';

	var myUrl = 'https://cs373-idb.appspot.com/api/reviews/all/';

	$scope.reviewlist = [];

	$http.get(myUrl).success(function(data){
		var myjson = data;
		$scope.reviewlist = myjson;
	});

	$scope.searchFilter = function (obj) {
		var re = new RegExp($scope.searchReviews, 'i');
		return !$scope.searchReviews || re.test(obj.reviewer) || re.test(obj.book);
	};

	$scope.sort = function(keyname){
		if ($scope.sortKey != keyname) {
			$scope.sortKey = keyname;
			$scope.reverse = true;
		};
		$scope.reverse = !$scope.reverse;
	}
});

app.controller('BookEntryController', function($scope, $http, $location){
	$scope.potato = $location.absUrl().substring($location.absUrl().indexOf("=")+1);
	
	var myUrl = 'https://cs373-idb.appspot.com/api/books/title='+$scope.potato;

	$http.get(myUrl).success(function(data) {
		var myjson = data;
		$scope.book = myjson;
		console.log("What is the in potato? "+$scope.potato);
	});
});