window.LoginView = Backbone.View.extend({

    initialize: function () {
       this.model.bind('change:loggedIn', this.render, this);
    },

    events: {
        'submit': 'onLoginViaApiSubmit'
    },

    onLoginViaApiSubmit: function(e){
        e.preventDefault();
        this.model.login(   this.$('input[name=username]').val(), 
                            this.$('input[name=password]').val());
    },

    render: function () {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }
});