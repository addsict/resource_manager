(function (Backbone, _, $, global) {

  var ResourceView = Backbone.View.extend({

    tagName: 'li',

    initialize: function (options) {
      _.bindAll(this, 'render');
      this.model.bind('change', this.render);
    },

    events: {
      'click a.resource-link': 'showDialog'
    },

    render: function () {
      var templateStr = $('#resource_template').html();
      var template = _.template(templateStr);
      var html = template({
        id: this.model.get('id'),
        name: this.model.get('name'),
        is_used: this.model.get('is_used')
      });
      this.$el.html(html);

      return this;
    },

    showDialog: function (e) {
      var templateStr = $('#dialog_template').html();
      var template = _.template(templateStr);
      var model = this.model;
      var html = template(model.toJSON());
      $('#resource_dialog').html(html);

      var dialogButtons = model.get('is_used') ? {
        '返却する': function () {
          // update model
          model.set('is_used', false)
               .set('user', '')
               .set('room_used', '')
               .set('using_date', '');
          model.save();

          $(this).dialog('close')
        }
      } : {
        '使用する': function () {
          var user = $('#user').val(),
              room_used = $('#room_used').val(),
              using_date = $('#using_date').val();

          // update model
          model.set('is_used', true)
               .set('user', user)
               .set('room_used', room_used)
               .set('using_date', using_date);
          model.save();
          
          $(this).dialog('close')
        }
      }
      dialogButtons.Cancel = function () {
        $(this).dialog('close')
      };

      // dialog setting
      $('#resource_dialog_inner').dialog({
        autoOpen: false,
        height: 600,
        width: 350,
        modal: true,
        closeOnEscape: false,
        buttons: dialogButtons,
        close: function () {
            $('#resource_dialog').empty();
            $('.ui-dialog').remove();
        }
      });
      $('#resource_dialog_inner').dialog('open');
    }
  });

  global.ResourceView = ResourceView;
})(Backbone, _, jQuery, this);
