window.Router = Backbone.Router.extend({

    routes: {
        "": "home",
        "charts": "charts",
        "contact": "contact",
        "login": "login",
        "employees/:id": "employeeDetails"
    },

    initialize: function () {
        this.headerView = new HeaderView();
        $('.header').html(this.headerView.render().el);

        // Close the search dropdown on click anywhere in the UI
        $('body').click(function () {
            $('.dropdown').removeClass("open");
        });
    },

    home: function () {
        // Since the home view never changes, we instantiate it and render it only once
        if (!this.homeView) {
            this.homeView = new HomeView();
            this.homeView.render();
        } else {
            this.homeView.delegateEvents(); // delegate events when the view is recycled
        }
        $("#content").html(this.homeView.el);
        this.headerView.select('home-menu');
    },
    
    charts: function () {
        if (!this.chartsView) {
            this.chartsView = new ChartsView({model: new CameraSettings()});
            this.chartsView.render();
        }
        $('#content').html(this.chartsView.el);
        this.headerView.select('charts-menu');
    },

    contact: function () {
        if (!this.contactView) {
            this.contactView = new ContactView();
            this.contactView.render();
        }
        $('#content').html(this.contactView.el);
        this.headerView.select('contact-menu');
    },
    
    login: function () {
        if (!this.loginView) {
            this.loginView = new LoginView({model: new LoginStatus()});
            this.loginView.render();
        }
        $('#content').html(this.loginView.el);
        this.headerView.select('login-menu');
    },

    employeeDetails: function (id) {
        var employee = new Employee({id: id});
        employee.fetch({
            success: function (data) {
                // Note that we could also 'recycle' the same instance of EmployeeFullView
                // instead of creating new instances
                $('#content').html(new EmployeeView({model: data}).render().el);
            }
        });
    }

});

// Loads them out of views/
templateLoader.load(["HomeView", "ContactView", "HeaderView", "EmployeeView", 
    "EmployeeSummaryView", "EmployeeListItemView", "LoginView", 
    "ChartsView"], function () {
        app = new Router();
        Backbone.history.start();
    }
);