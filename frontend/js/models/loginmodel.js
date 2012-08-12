var LoginStatus = Backbone.Model.extend({
    
    model: Employee,

    url:"/home/login/",

    login:function (username, password) {
        var self = this;
        $.ajax({
            type: 'POST',
            url: "/home/login/",
            data: {'username': username, 'password': password},
            dataType:"json",
            success:function (data) {
                console.log(data)
                //self.reset(data.objects);
            }
        });
    }

    // defaults: {
    //     loggedIn: false,
    //     apiKey: null
    // },
    // 
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