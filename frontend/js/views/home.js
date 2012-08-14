window.HomeView = Backbone.View.extend({

    initialize:function () {
        
    },

    events:{
        "click #showMeBtn":"showMeBtnClick"
    },

    render:function () {
        $(this.el).html(this.template());
        return this;
    },

    showMeBtnClick:function () {
        app.headerView.search();
    }

});