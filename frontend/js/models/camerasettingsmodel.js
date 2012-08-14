window.CameraSettings = Backbone.Model.extend({
    
    urlRoot:"/api/v1/camera_settings/?format=json",
    
    initialize:function () {
        this.url = this.urlRoot + '&id=' + this.id;
    },
    
    parse: function(response) {
       return response.objects[0];
    }

});

window.CameraSettingsCollection = Backbone.Collection.extend({
    url: '/api/v1/camera_settings/?format=json&limit=50',
    model: CameraSettings,

    fetchAllStats:function(callback) {
        var self = this;
        $.ajax({
            url:self.url,
            dataType:"json",
            success:function (data) {
                var dataset = []
                data.objects.forEach(function(item) {
                    dataset.push([item.aperture, item.shutter_speed])
                });
                self.reset(dataset);
                callback(dataset);
            }
        });
    }
});