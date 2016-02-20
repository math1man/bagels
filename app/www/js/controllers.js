(function() {

  var app = angular.module('bagels.controllers', []);

  app.controller('IndexController', function($scope, $window, $state) {

    $window.init = function() {
      if (!$state.is('home')) {
        $state.go('home');
      }
    };

    $scope.showSettings = function() {
      // TODO settings eventually
    };

  });

  app.controller('ActivityController', function($scope, $cordovaInAppBrowser, Activity) {

    $scope.showDesc = false;

    $scope.toggleDesc = function() {
      $scope.showDesc = !$scope.showDesc;
    };

    $scope.goWebsite = function() {
      $cordovaInAppBrowser.open(Activity.url, '_system')
    };

    $scope.activity = function(field) {
      return Activity[field];
    };


  });

})();
