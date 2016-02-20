(function () {

// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'bagels' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
  var app = angular.module('bagels', ['ionic', 'ngCordova', 'bagels.controllers', 'bagels.services']);

  app.run(function ($window, $cordovaKeyboard, $ionicPlatform) {
    $ionicPlatform.ready(function () {
      if ($window.cordova) {
        // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
        // for form inputs)
        $cordovaKeyboard.hideKeyboardAccessoryBar(true);
        if (ionic.Platform.isIOS()) {
          // Don't remove this line unless you know what you are doing. It stops the viewport
          // from snapping when text inputs are focused. Ionic handles this internally for
          // a much nicer keyboard experience.
          $cordovaKeyboard.disableScroll(true);
        }
      }
    });
  });

  app.config(function ($stateProvider, $urlRouterProvider) {
    $stateProvider
      .state('home', {
        url: '/home',
        templateUrl: 'templates/home.html'
      })
      .state('activity', {
        url: '/activity',
        templateUrl: 'templates/activity.html'
      })
      .state('settings', {
        url: '/settings',
        templateUrl: 'templates/settings.html'
      });

    $urlRouterProvider.otherwise('/home');
  });

})();
