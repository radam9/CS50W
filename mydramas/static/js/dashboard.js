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

function favarea(data) {
  console.log(data);
  var fav_area = am4core.create("fav-area", am4charts.XYChart);
  fav_area.colors.step = 2;
  fav_area.data = data;

  // Creating Axis
  var categoryAxis = fav_area.xAxes.push(new am4charts.CategoryAxis());
  categoryAxis.renderer.labels.template.rotation = 270;
  categoryAxis.dataFields.category = "Year";
  categoryAxis.title.text = "Year";
  categoryAxis.renderer.grid.template.location = 0;
  categoryAxis.renderer.labels.template.horizontalCenter = "right";
  categoryAxis.renderer.labels.template.verticalCenter = "middle";
  categoryAxis.renderer.minGridDistance = 20;
  categoryAxis.tooltip.label.rotation = 270;
  categoryAxis.tooltip.label.horizontalCenter = "right";
  categoryAxis.tooltip.label.verticalCenter = "middle";
  categoryAxis.startLocation = 0.5;
  categoryAxis.endLocation = 0.5;

  var valueAxis = fav_area.yAxes.push(new am4charts.ValueAxis());
  valueAxis.title.text = "Percent";
  valueAxis.calculateTotals = true;
  valueAxis.min = 0;
  valueAxis.max = 100;
  valueAxis.strictMinMax = true;
  valueAxis.renderer.labels.template.adapter.add("text", function(text) {
    return text + "%";
  });

  //Create Series
  var series = fav_area.series.push(new am4charts.LineSeries());
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
  var series2 = fav_area.series.push(new am4charts.LineSeries());
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
  fav_area.cursor = new am4charts.XYCursor();

  // add legend
  fav_area.legend = new am4charts.Legend();
}
function favpie(data) {
  var fav_pie = am4core.create("fav-pie", am4charts.PieChart);
  fav_pie.innerRadius = am4core.percent(40);

  // Create pie series
  var series = fav_pie.series.push(new am4charts.PieSeries());
  series.dataFields.value = "dramas";
  series.dataFields.category = "category";

  // Add data
  fav_pie.data = data;

  //Create Label
  var label = series.createChild(am4core.Label);
  label.text = "{values.value.sum}";
  label.horizontalCenter = "middle";
  label.verticalCenter = "middle";
  label.fontSize = 20;
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
    favpie(data.favpie);
    favarea(data.favarea);
  })
  .catch(function(ex) {
    console.log("parsing failed", ex);
  });
