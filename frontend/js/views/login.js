window.LoginView = Backbone.View.extend({

    // _loggedInTemplate: _.template($('#logged_in').html()),
    // _notLoggedInTemplate: _.template($('#not_logged_in').html()),

    initialize: function () {
       // this.model.bind('change:loggedIn', this.render, this);
    },

    events: {
        'submit': 'onLoginViaApiSubmit'
    },

    onLoginViaApiSubmit: function(e){
        e.preventDefault();
        this.model.login(this.$('input[name=username]').val(), this.$('input[name=password]').val());
        // this.model.setApiKey(this.$('input[name=api_key]').val());
    },

    render: function () {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
        // if (this.model.get('loggedIn')) {
        //     $(this.el).empty().html(this._loggedInTemplate(this.model));
        // } else {
        //     $(this.el).empty().html(this._notLoggedInTemplate(this.model));
        // }
        return this;
    }
});