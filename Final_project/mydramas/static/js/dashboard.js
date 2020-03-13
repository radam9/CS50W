// Django documentation function to get csrftoken from cookies
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
function charttitle(chart, ctitle) {
  var title = chart.titles.create();
  title.text = ctitle;
  title.fontSize = 20;
  title.marginTop = 10;
  title.marginBottom = 10;
  return title;
}
function seriescolor(series) {
  series.colors.list = [
    am4core.color("rgba(81, 219, 104, 0.74)"),
    am4core.color("rgba(84, 238, 174, 0.842)"),
    am4core.color("rgba(111, 214, 255, 1)"),
    am4core.color("rgba(26, 76, 240, 0.644)"),
    am4core.color("rgba(124, 95, 255, 1)"),
    am4core.color("rgba(249, 113, 136, 1)"),
    am4core.color("rgba(240, 17, 17, 0.596)"),
    am4core.color("rgba(241, 131, 57, 1)"),
    am4core.color("rgba(241, 224, 71, 1)"),
    am4core.color("rgba(233, 240, 142, 1)")
  ];
  return series;
}
function favpie(data) {
  var chart = am4core.create("fav-pie", am4charts.PieChart);
  charttitle(chart, "Total Favorites");
  chart.innerRadius = am4core.percent(40);

  // Create pie series
  var series = chart.series.push(new am4charts.PieSeries());
  series.dataFields.value = "dramas";
  series.dataFields.category = "category";
  series.labels.template.disabled = true;
  series.slices.template.cornerRadius = 7;
  series.slices.template.innerCornerRadius = 7;

  // Add data
  chart.data = data;

  //Create Label
  var label = series.createChild(am4core.Label);
  label.text = "{values.value.sum}";
  label.horizontalCenter = "middle";
  label.verticalCenter = "middle";
  label.fontSize = 20;
}
function favarea(data) {
  var chart = am4core.create("fav-area", am4charts.XYChart);
  charttitle(chart, "Favorites/Year");
  chart.colors.step = 2;
  chart.data = data;

  // Creating Axis
  var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
  categoryAxis.dataFields.category = "Year";
  categoryAxis.title.text = "Year";
  categoryAxis.renderer.grid.template.location = 0;
  categoryAxis.renderer.labels.template.rotation = 270;
  categoryAxis.renderer.labels.template.horizontalCenter = "right";
  categoryAxis.renderer.labels.template.verticalCenter = "middle";
  categoryAxis.renderer.minGridDistance = 20;
  categoryAxis.tooltip.label.rotation = 270;
  categoryAxis.tooltip.label.horizontalCenter = "right";
  categoryAxis.tooltip.label.verticalCenter = "middle";
  categoryAxis.startLocation = 0.5;
  categoryAxis.endLocation = 0.5;

  var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
  valueAxis.title.text = "Percent";
  valueAxis.calculateTotals = true;
  valueAxis.min = 0;
  valueAxis.max = 100;
  valueAxis.strictMinMax = true;
  valueAxis.renderer.labels.template.adapter.add("text", function(text) {
    return text + "%";
  });

  //Create Series
  var series = chart.series.push(new am4charts.LineSeries());
  series.dataFields.valueY = "Favorites";
  series.dataFields.valueYShow = "totalPercent";
  series.dataFields.categoryX = "Year";
  series.dataFields.valueX = "Percent";
  series.name = "Favorites";
  series.calculatePercent = true;

  series.tooltipHTML =
    "<span style='font-size:14px; color:#000000;'><b>{valueY.value} ({valueX}%)</b></span>";

  series.tooltip.getFillFromObject = false;
  series.tooltip.background.fill = am4core.color("#FFF");

  series.tooltip.getStrokeFromObject = true;
  series.tooltip.background.strokeWidth = 3;

  series.fillOpacity = 0.85;
  series.stacked = true;
  // static
  series.legendSettings.labelText = "Favorites total:";
  series.legendSettings.valueText = "{valueY.sum}";

  // hovering
  series.legendSettings.itemLabelText = "Favorites:";
  series.legendSettings.itemValueText = "{valueY}";
  var series2 = chart.series.push(new am4charts.LineSeries());
  series2.dataFields.valueY = "Dramas";
  series2.dataFields.valueYShow = "totalPercent";
  series2.dataFields.categoryX = "Year";
  series2.name = "Dramas";

  series2.tooltipHTML =
    "<span style='font-size:14px; color:#000000;'><b>{valueY.value}</b></span>";

  series2.tooltip.getFillFromObject = false;
  series2.tooltip.background.fill = am4core.color("#FFF");

  series2.tooltip.getStrokeFromObject = true;
  series2.tooltip.background.strokeWidth = 3;

  series2.fillOpacity = 0.85;
  series2.stacked = true;

  // static
  series2.legendSettings.labelText = "Dramas total:";
  series2.legendSettings.valueText = "{valueY.sum}";

  // hovering
  series2.legendSettings.itemLabelText = "Dramas:";
  series2.legendSettings.itemValueText = "{valueY}";
  // Add cursor
  chart.cursor = new am4charts.XYCursor();

  // // add legend
  // chart.legend = new am4charts.Legend();
}
function netpie(data, element, title) {
  var chart = am4core.create(element, am4charts.PieChart);
  charttitle(chart, title);

  chart.innerRadius = am4core.percent(40);

  // Create pie series
  var series = chart.series.push(new am4charts.PieSeries());
  series.dataFields.value = "Dramas";
  series.dataFields.category = Object.keys(data[0])[0];
  // Disable labels
  series.labels.template.disabled = true;
  series.slices.template.cornerRadius = 7;
  series.slices.template.innerCornerRadius = 7;
  // info - https://www.amcharts.com/docs/v4/concepts/colors/
  seriescolor(series);

  // Add data
  chart.data = data;

  // Add Legend
  // chart.legend = new am4charts.Legend();
  // chart.legend.maxHeight = 50;
  // chart.legend.scrollable = true;
  // chart.legend.markers.template.disabled = true;
  // chart.legendSettings.labelText = "[{stroke}]{name}[/]";

  //Create Label
  var label = series.createChild(am4core.Label);
  label.text = "{values.value.sum}";
  label.horizontalCenter = "middle";
  label.verticalCenter = "middle";
  label.fontSize = 20;
}
function netline(data, element, title) {
  var chart = am4core.create(element, am4charts.XYChart);
  charttitle(chart, title);
  var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
  categoryAxis.dataFields.category = "Year";
  categoryAxis.title.text = "Year";
  categoryAxis.renderer.grid.template.location = 0;
  categoryAxis.renderer.labels.template.rotation = 270;
  categoryAxis.renderer.labels.template.horizontalCenter = "right";
  categoryAxis.renderer.labels.template.verticalCenter = "middle";
  categoryAxis.renderer.minGridDistance = 20;
  categoryAxis.tooltip.label.rotation = 270;
  categoryAxis.tooltip.label.horizontalCenter = "right";
  categoryAxis.tooltip.label.verticalCenter = "middle";
  categoryAxis.startLocation = 0.5;
  categoryAxis.endLocation = 0.5;

  var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
  valueAxis.title.text = "Dramas";

  for (var i = 0; i < data.networks.length; i++) {
    createSeries(data.networks[i]);
  }

  // Loop to create series
  function createSeries(network, percent) {
    var series = chart.series.push(new am4charts.LineSeries());
    series.dataFields.valueY = network;
    // series.dataFields.valueYShow = "totalPercent";
    series.dataFields.categoryX = "Year";
    series.dataFields.valueX = network + " percent";
    series.name = network;
    series.calculatePercent = true;

    series.tooltipHTML =
      "<span style='font-size:14px; color:#000000;'><b>{name}: {valueY.value} ({valueX}%)</b></span>";

    series.tooltip.getFillFromObject = false;
    series.tooltip.background.fill = am4core.color("#FFF");

    series.tooltip.getStrokeFromObject = true;
    series.tooltip.background.strokeWidth = 3;
    // static
    series.legendSettings.labelText = network + " total:";
    series.legendSettings.valueText = "{valueY.sum}";

    // hovering
    series.legendSettings.itemLabelText = network + ":";
    series.legendSettings.itemValueText = "{valueY}";
  }
  chart.data = data.data;
  // Add cursor
  chart.cursor = new am4charts.XYCursor();

  // // add legend
  // chart.legend = new am4charts.Legend();
  // chart.legend.position = "bottom";
  // chart.legend.scrollable = true;
}
function rathisto(data, keys, element, title) {
  var chart = am4core.create(element, am4charts.XYChart);
  charttitle(chart, title);
  var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
  categoryAxis.dataFields.category = "category";
  categoryAxis.renderer.grid.template.location = 0;
  categoryAxis.renderer.minGridDistance = 30;
  categoryAxis.renderer.labels.template.horizontalCenter = "right";
  categoryAxis.renderer.labels.template.verticalCenter = "middle";
  categoryAxis.renderer.labels.template.rotation = 270;
  categoryAxis.tooltip.disabled = true;
  categoryAxis.renderer.minHeight = 110;

  var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
  valueAxis.renderer.minWidth = 50;
  chart.data = data.data[keys[0]];
  // Create series
  var series = chart.series.push(new am4charts.ColumnSeries());
  series.sequencedInterpolation = true;
  series.dataFields.valueY = "count";
  series.dataFields.categoryX = "category";
  series.dataFields.valueX = "percent";
  series.tooltipText = "[bold]{categoryX}:[/] {valueY} ({valueX}%)";
  series.columns.template.strokeWidth = 0;

  series.tooltip.pointerOrientation = "vertical";

  series.columns.template.column.cornerRadiusTopLeft = 10;
  series.columns.template.column.cornerRadiusTopRight = 10;
  series.columns.template.column.fillOpacity = 0.8;
  seriescolor(chart);

  // on hover, make corner radiuses bigger
  var hoverState = series.columns.template.column.states.create("hover");
  hoverState.properties.cornerRadiusTopLeft = 0;
  hoverState.properties.cornerRadiusTopRight = 0;
  hoverState.properties.fillOpacity = 1;

  series.columns.template.adapter.add("fill", function(fill, target) {
    return chart.colors.getIndex(target.dataItem.index);
  });

  // Cursor
  chart.cursor = new am4charts.XYCursor();
  return chart;
}

fetch("/api/favorite/", {
  method: "get",
  credentials: "same-origin",
  headers: {
    "X-CSRFToken": getCookie("csrftoken"),
    Accept: "application/json",
    "Content-Type": "application/json"
  }
})
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    localStorage.setItem("datahisto1", JSON.stringify(data.ratinghisto1));
    localStorage.setItem("datahisto2", JSON.stringify(data.ratinghisto2));
    favpie(data.favpie);
    favarea(data.favarea);
    netpie(data.netpie1, "net-pie1", "Total Network Drama Share");
    netline(data.netline1, "net-line1", "Network Drama Share / Year");
    netpie(data.netpie2, "net-pie2", "Favorite Network Drama Share");
    netline(data.netline2, "net-line2", "Favorite Network Share / Year");
    netpie(data.ratingpie1, "rat-pie1", "Drama Rating Share");
  })
  .catch(function(ex) {
    console.log("parsing failed", ex);
  });

var chart;
var chart2;
// function ratinghelper(dataname, element, title, selector){
//     data = JSON.parse(localStorage.getItem(dataname))
//     var keys = Object.keys(data.data);
//     var selectlist = document.getElementById(selector);
//     for (var i = 0; i < keys.length; i++) {
//       var option = document.createElement("option");
//       option.value = keys[i];
//       option.text = keys[i];
//       selectlist.appendChild(option);
//     }
//     chart = rathisto(data, keys, element, title);
//     return chart
// }
// setTimeout(function() {
//     ratinghelper("datahisto1", "rat-histo1", "Drama Rating Share / Year", "rat-histo1-select");
//     ratinghelper("datahisto2", "rat-histo2", "Network Rating Share / Year", "rat-histo2-select");
// },3000);

setTimeout(function() {
  data = JSON.parse(localStorage.getItem("datahisto1"));
  var keys = Object.keys(data.data);
  var selectlist = document.getElementById("rat-histo1-select");
  for (var i = 0; i < keys.length; i++) {
    var option = document.createElement("option");
    option.value = keys[i];
    option.text = keys[i];
    selectlist.appendChild(option);
  }
  chart = rathisto(data, keys, "rat-histo1", "Drama Rating Share / Year");
  return chart;
}, 2000);
setTimeout(function() {
  data = JSON.parse(localStorage.getItem("datahisto2"));
  var keys = Object.keys(data.data);
  var selectlist = document.getElementById("rat-histo2-select");
  for (var i = 0; i < keys.length; i++) {
    var option = document.createElement("option");
    option.value = keys[i];
    option.text = keys[i];
    selectlist.appendChild(option);
  }
  chart2 = rathisto(data, keys, "rat-histo2", "Network Rating Share / Year");
  return chart2;
}, 2000);

function selectDataset(set) {
  var data = JSON.parse(localStorage.getItem("datahisto1"));
  chart.data = data.data[set];
}
function selectDataset2(set) {
  var data = JSON.parse(localStorage.getItem("datahisto2"));
  chart2.data = data.data[set];
}
