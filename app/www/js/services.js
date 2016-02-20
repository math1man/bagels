(function() {

  var app = angular.module('bagels.services', []);

  app.service('Activity', function() {
    this.name = 'Walker Art Center';
    this.url = 'http://www.walkerart.org/';
    this.cost = '$9-14 per person';
    this.duration = 'Varies';
    this.groupSize = 'Any';
    this.distance = '8 miles';
    this.description = 'The Walker Art Center is a multidisciplinary contemporary art center. ' +
        'The Walker is considered one of America\'s premier museums for modern art.';
  });

})();
