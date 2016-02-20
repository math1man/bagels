(function() {

  var app = angular.module('bagels.services', []);

  app.service('Activity', function() {
    this.activity = {
      name: '-',
      url: '-',
      cost: '-',
      duration: '-',
      groupSize: '-',
      distance: '-',
      description: '-'
    };
  });

  app.service('Preferences', function() {
    this.art = true;
    this.history = true;
    this.outdoors = true;
    this.shopping = true;
    this.shows = true;
    this.sports = true;
    this.social = true;
    this.volunteering = true;
  });

  app.factory('API', function() {

    var api = null;

    return {
      init: function(apiInit) {
        api = apiInit;
      },
      getEvent: function() {
        return api.getEvent({id: 0});
      }
    };
  });

  app.service('Loading', function() {
    this.is = false;
  });

})();
