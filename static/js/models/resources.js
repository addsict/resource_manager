(function (Backbone, _, $, global) {
  var Resources = Backbone.Collection.extend({

    model: Resource,

    url: 'api/resources',

    initialize: function () {
    },

    parse: function (resp) {
      return resp.items;
    }
  });

  // exports
  global.Resources = Resources;
})(Backbone, _, jQuery, this);
