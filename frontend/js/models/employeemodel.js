window.Employee = Backbone.Model.extend({
    
    urlRoot:"/api/v1/person/?format=json",
    
    initialize:function () {
        this.reports = new EmployeeCollection();
        this.reports.url = this.urlRoot + '&id=' + this.id;
    },
    
    parse: function(response) {
       return response.objects[0];
    }
});

window.EmployeeCollection = Backbone.Collection.extend({

    model: Employee,

    url:"/api/v1/person/?format=json",

    findByName:function (key) {
        var url = (key == '') ? this.url : this.url + '&q=' + key;
        var self = this;
        $.ajax({
            url:url,
            dataType:"json",
            success:function (data) {
                self.reset(data.objects);
            }
        });
    }

});