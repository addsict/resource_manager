(function (Backbone, _, $, global) {
  var Resource = Backbone.Model.extend({
    default: {
    },

    initialize: function (options) {
    },

    urlRoot: '/api/resource/',

    url: function () {
      var url = this.urlRoot + this.get('id');
      return url;
    }
  });

  // exports
  global.Resource = Resource;
})(Backbone, _, jQuery, this);
