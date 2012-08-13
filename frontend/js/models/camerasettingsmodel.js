window.CameraSettings = Backbone.Model.extend({
    
    urlRoot:"/api/v1/camera_settings/?format=json",
    
    initialize:function () {
        this.reports = new CameraSettingsCollection();
        this.reports.url = '/api/v1/camera_settings/?format=json'; // &id=' + this.id;
    },
    
    parse: function(response) {
       return response.objects[0];
    }

});

window.CameraSettingsCollection = Backbone.Collection.extend({

    model: CameraSettings,

    url:"/api/v1/camera_settings/?format=json&limit=1000",

    getAllData:function () {
        var url = '/api/v1/camera_settings/?format=json&limit=1000'
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