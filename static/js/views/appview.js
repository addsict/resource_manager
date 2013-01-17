(function (Backbone, _, $, global) {

  var AppView = Backbone.View.extend({

    initialize: function (options) {
      _.bindAll(this, 'render');
      this.collection.bind('reset', this.render);
      this.collection.bind('update', this.render);

      this.collection.fetch();

    },

    events: {
    },

    render: function () {
      this.collection.each(function (resource) {
        var resourceView = new ResourceView({
          model: resource
        });
        var category = resource.get('category');
        this.$('#' + category + '_list').append(resourceView.render().el);
      });

      return this;
    },
  });

  global.AppView = AppView;
})(Backbone, _, jQuery, this);
