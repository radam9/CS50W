const x = document.getElementsByName("csrfmiddlewaretoken")[0].value;
$(".btn-cart").on("click", e => {
  var id = e.currentTarget.id;
  $.ajax({
    headers: {
      "X-CSRFToken": x
    },
    type: "POST",
    url: "/cart/",
    data: { itemid: id.slice(10) },
    success: function(data) {
      var tot = parseFloat($("#totprice").text());
      tot = tot - parseFloat(data["price"]);
      $("#totprice").text(tot.toFixed(2));
      $("." + id).empty();
    }
  });
});
$("#place-order").on("click", () => {
  $.ajax({
    type: "GET",
    url: "/modalcart/",
    success: function(data) {
      $(".modalslot").append(data);
      $(".modal").modal({ backdrop: "static" });
      //delete modal html after it is closed.
      $(".modal").on("hidden.bs.modal", () => {
        $(".modalslot").empty();
      });
      $("#confirm").on("click", () => {
        $("#formsubmit").submit();
      });
    }
  });
});
