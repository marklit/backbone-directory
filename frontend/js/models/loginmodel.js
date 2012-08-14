var LoginStatus = Backbone.Model.extend({

    url:"/home/login/",
    
    defaults: {
        loggedIn: false,
        lastFailure: ''
    },
    
    isLoggedIn:function () {
        return this.loggedIn
    },

    login:function (username, password) {
        var self = this;
        $.ajax({
            type: 'POST',
            url: self.url,
            data: {'username': username, 'password': password},
            dataType:"json",
            success:function (data) {
                self.set({'loggedIn': data.login_successful});
                self.set({'lastFailure': data.login_successful ? "" : data.reason});
            }
        });
    }

    // initialize: function () {
    //     this.bind('change:apiKey', this.onApiKeyChange, this);
    //     this.set({'apiKey': localStorage.getItem('apiKey')});
    // },
    // 
    // onApiKeyChange: function (status, apiKey) {
    //     this.set({'loggedIn': !!apiKey});
    // },
    // 
    // setApiKey: function(apiKey) {
    //     localStorage.setItem('apiKey', apiKey)
    //     this.set({'apiKey': apiKey});
    // }

});