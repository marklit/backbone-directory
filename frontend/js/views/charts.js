window.ChartsView = Backbone.View.extend({
    
    initialize: function () {
        this.searchResults = new CameraSettingsCollection;
        this.model.on('change', this.render, this);
        this.model.on('destroy', this.remove, this);
    },
    
    buildChart:function( dataset ) {
        var width = 900,
            height = 400,
            padding = 50;
        
        var svg = d3.select(this.el)
                    .append("svg")
                    .attr("width", width)
                    .attr("height", height),
            xScale = d3.scale.linear()
                .domain([0, d3.max(dataset, function(d) { return d[0]; })])
                .range([padding, width - padding * 2]),
            yScale = d3.scale.linear()
                .domain([0, d3.max(dataset, function(d) { return d[1]; })])
                .range([height - padding, padding]),
            rScale = d3.scale.linear()
                .domain([0, d3.max(dataset, function(d) { return d[1]; })])
                .range([2, 5]);
        var xAxis = d3.svg.axis()
                .scale(xScale)
                .orient("bottom")
                .ticks(5),
            yAxis = d3.svg.axis()
                .scale(yScale)
                .orient("left")
                .ticks(5);
        
        svg.selectAll("circle")
            .data(dataset)
            .enter()
            .append("circle")
            .attr("cx", function(d) {
                return xScale(d[0]);
            })
            .attr("cy", function(d) {
                return yScale(d[1]);
            })
            .attr("r", function(d) {
                return rScale(d[1]);
            });
        
        svg.selectAll("text")
            .data(dataset)
            .enter()
            .append("text")
            .text(function(d) {
                return "f" + d[0] + ", 1/" + Math.round(d[1]*1000);
            })
            .attr("x", function(d) {
                return xScale(d[0]);
            })
            .attr("y", function(d) {
                return yScale(d[1]);
            })
            .attr("font-family", "sans-serif")
            .attr("font-size", "11px")
            .attr("fill", "red");
        
        svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(0," + (height - padding) + ")")
            .call(xAxis);

        svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + padding + ",0)")
            .attr("text-anchor","middle")
            .call(yAxis);
        
        svg.append("text")
            .attr("class", "x label")
            .attr("text-anchor", "end")
            .attr("x", width/2)
            .attr("y", height - 6)
            .text("f-stop");
            
        svg.append("text")
            .attr("class", "y label")
            .attr("text-anchor", "end")
            .attr("y", 6)
            .attr("x", -(height/3))
            .attr("dy", "0.25em")
            .attr("transform", "rotate(-90)")
            .text("shutter speed (seconds)");
    },
    
    render:function () {
        var self = this;
        this.searchResults.fetchAllStats(function(dataset) {
            self.buildChart(dataset);
        });
        $(this.el).html(this.template());
    }
    
});