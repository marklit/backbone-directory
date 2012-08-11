window.Employee = Backbone.Model.extend({
    
    urlRoot:"http://172.16.91.179:8001/api/v1/person/?format=json",
    
    initialize:function () {
        this.reports = new EmployeeCollection();
        this.reports.url = '&id=' + this.id;
    }

});

window.EmployeeCollection = Backbone.Collection.extend({

    model: Employee,

    url:"../api/employees",

    findByName:function (key) {
        var url = (key == '') ? 
            'http://172.16.91.179:8001/api/v1/person/?format=json' : 
            "http://172.16.91.179:8001/api/v1/person/?format=json&first_name__contains=" + key;
        console.log('findByName: ' + key);
        var self = this;
        $.ajax({
            url:url,
            dataType:"json",
            success:function (data) {
                console.log("search success: " + data.length);
                self.reset(data);
            }
        });
    }

});