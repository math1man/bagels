(function() {

  const URL = 'https://macathon2016.appspot.com/_ah/api';

  var app = angular.module('bagels.controllers', []);

  app.controller('IndexController', function($scope, $window, $state, API) {

    $window.init = function() {
      if (!$state.is('home')) {
        $state.go('home');
      }

      gapi.client.load('events', 'v1', function() { // TODO
        // initialize API variable
        API.init(gapi.client.events.eventsApi);   // TODO

        //API.getEvent();

      }, URL);
    };

  });

  app.controller('HomeController', function($scope, $state, $interval, API, Activity, Loading) {

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
    };

    $scope.whatDo = function() {
      Loading.is = true;
      API.getEvent().then(function(resp) {
        Activity.activity = resp.result;
        Loading.is = false;
      });
    };

  });

  app.controller('ActivityController', function($scope, $cordovaInAppBrowser, $ionicPopup, API, Activity, Loading) {

    $scope.showDesc = false;
    $scope.toggleDesc = function() {
      $scope.showDesc = !$scope.showDesc;
    };

    $scope.goWebsite = function() {
      if (Activity.activity.url.length > 0) {
        $cordovaInAppBrowser.open(Activity.activity.url, '_system'); // TODO this doesn't seem to work on real phones
      }
    };

    $scope.activity = function(field) {
      return Activity.activity[field];
    };

    $scope.refresh = function() {
      Loading.is = true;
      API.getEvent().then(function(resp) {
        Activity.activity = resp.result;
        Loading.is = false;
      });
    };

    $scope.isLoading = function() {
      return Loading.is;
    };

    $scope.tooExpensive = function() {
      var confirmPopup = $ionicPopup.confirm({
        title: 'Too expensive',
        template: 'This activity is too expensive for me.'
      });

      confirmPopup.then(function(res) {
        if(res) {
          Loading.is = true;
          API.getEvent().then(function(resp) {
            Activity.activity = resp.result;
            Loading.is = false;
          });
        }
      });
    };

    $scope.tooManyPeople = function() {
      var confirmPopup = $ionicPopup.confirm({
        title: 'Too many people',
        template: 'We have too many people for this activity.'
      });

      confirmPopup.then(function(res) {
        if(res) {
          Loading.is = true;
          API.getEvent().then(function(resp) {
            Activity.activity = resp.result;
            Loading.is = false;
          });
        }
      });
    };

    $scope.tooLong = function() {
      var confirmPopup = $ionicPopup.confirm({
        title: 'Too long',
        template: 'This activity will take too long.'
      });

      confirmPopup.then(function(res) {
        if(res) {
          Loading.is = true;
          API.getEvent().then(function(resp) {
            Activity.activity = resp.result;
            Loading.is = false;
          });
        }
      });
    };

    $scope.tooFarAway = function() {
      var confirmPopup = $ionicPopup.confirm({
        title: 'Too far away',
        template: 'This activity is too far away.'
      });

      confirmPopup.then(function(res) {
        if(res) {
          Loading.is = true;
          API.getEvent().then(function(resp) {
            Activity.activity = resp.result;
            Loading.is = false;
          });
        }
      });
    };

  });

  app.controller('SettingsController', function($scope, Preferences) {

    $scope.preferences = Preferences;

  });

})();
