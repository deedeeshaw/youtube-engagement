d3.json("../static/data/youtubejs.json").then(function (data) {

    var tbody = d3.select("tbody");
    data.forEach(function (youtube) {
        var row = tbody.append("tr");
        Object.entries(youtube).forEach(function ([key, value]) {
            if ([key] == "title" || [key] == "category_desc" || [key] == "publish_date" || [key] == "views") {
                var cell = tbody.append("td");
                cell.text(value);
            }
        });
    });

    var submit = d3.select("#filter-btn");

    submit.on("click", function () {

        var copied_data = data;

        // prevent refreshing
        d3.event.preventDefault();

        // clear the table
        d3.select("tbody").selectAll("*").remove();

        // get the title value from input
        var title = d3.select("#title");
        var title_value = title.property("value");
        console.log(title_value);

        // get the category value from input
        var category = d3.select("#category");
        var category_value = category.property("value");
        console.log(category_value);

        // get the date value from input
        var date = d3.select("#date");
        var date_value = date.property("value");
        console.log(date_value);

        // get the views value from input
        var views = d3.select("#views");
        var views_value = views.property("value");
        console.log(views_value);

        // title filter
        function titlefilter(copied_data) {
            if (title_value != "") {
                var index_of_string = copied_data["title"].toLowerCase().search(title_value);
                return index_of_string > -1;
            } else {
                return true;
            }
        }

        //views filter
        function viewfilter(copied_data) {
            if (views_value != "") {
                return copied_data["views"] >= parseInt(views_value);
            } else {
                return true;
            }
        }

        //date filter
        function datefilter(copied_data) {
            if (date_value != "") {
                return copied_data["publish_date"] == date_value;
            } else {
                return true;
            }
        }

        //category filter
        function catgoryfilter(copied_data) {
            if (category_value != "") {
                var index_of_string = copied_data["category_desc"].toLowerCase().search(category_value);
                return index_of_string > -1;
            } else {
                return true;
            }
        }

        // get the filtered data
        var filtered_data = copied_data.
            filter(titlefilter).
            filter(viewfilter).
            filter(datefilter).
            filter(catgoryfilter);

        // indert the filtered data into html
        var tbody = d3.select("tbody");
        filtered_data.forEach(function (data) {
            var row = tbody.append("tr");
            Object.entries(data).forEach(function ([key, value]) {
                if ([key] == "title" || [key] == "category_desc" || [key] == "publish_date" || [key] == "views") {
                    var cell = tbody.append("td");
                    cell.text(value);
                }
            });
        });

    });

});




