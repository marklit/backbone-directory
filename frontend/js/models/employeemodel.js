window.Employee = Backbone.Model.extend({
    
    urlRoot:"/api/v1/person/?format=json",
    
    initialize:function () {
        this.reports = new EmployeeCollection();
        this.reports.url = '/api/v1/person/?format=json&id=' + this.id;
    },
    
    parse: function(response){
        //console.log('parse called', response)
       return response.objects[0];
    }

});

window.EmployeeCollection = Backbone.Collection.extend({

    model: Employee,

    url:"/api/v1/person/?format=json",

    findByName:function (key) {
        var url = (key == '') ? 
            '/api/v1/person/?format=json' : 
            "/api/v1/person/?format=json&first_name__contains=" + key;
        console.log('findByName: ' + key);
        var self = this;
        $.ajax({
            url:url,
            dataType:"json",
            success:function (data) {
                console.log("search success");
                console.log(data.objects)
                self.reset(data.objects);
            }
        });
    }

});