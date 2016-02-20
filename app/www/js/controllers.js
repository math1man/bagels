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


    $scope.changeView = function(){
      $state.go('settings')
    };
  });

  app.controller('HomeController', function($scope, $interval) {
    var verbs = [
      'dance',
      'try something new',
      'catch the game',
      'paint',
      'visit a polar bear',
      'jam',
      'experience nature',
      'snowboard',
      'seize the day',
      'discover',
      'get outside',
      'explore',
      'change the world',
      'hike',
      'feel the city',
      'cheer',
      'be amazed',
      'party',
      'experience history',
      'watch a film'
    ];

    var index = 0;

    $interval(function() {
      index++;
      if (index >= verbs.length) {
        index = 0;
      }
    }, 1000);

    $scope.getVerb = function() {
      return verbs[index];
    }

  });

  app.controller('SettingsController', function($scope, Preferences) {

    $scope.preferences = Preferences;

  });

})();
