(function() {

  var app = angular.module('bagels.controllers', []);

  app.controller('IndexController', function($scope, $window, $state) {

    $window.init = function() {
      if (!$state.is('home')) {
        $state.go('home');
      }
    }
  });

})();
