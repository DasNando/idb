/**
 * Created by Nando on 4/7/2017.
 */
'use strict';

angular.module('services',[])
    .factory('bookService', function($http) {
        return {
            getBooks: function () {
                return $http.get('/api/books/').then(function (result) {
                    return result.data;
                });
            }
        }
    });