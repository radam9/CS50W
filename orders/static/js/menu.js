$(".additem").on("click", e => {
  var id = e.currentTarget.id.slice(5);
  $.ajax({
    type: "GET",
    url: "/modal/",
    data: { item: id },
    success: function(data) {
      $(".modalslot").append(data);
      $(".modal").modal({ backdrop: "static" });
      // limit number of multiselect using jquery bootstrap-select library
      $(".selectpicker").selectpicker({
        maxOptions: parseInt($(".tops").attr("id"))
      });
      // change the value of sub-total depending on selection
      $(
        "#id_size_1, #id_size_2, #id_quantity, #id_toppings.selectpicker"
      ).change(() => {
        var baseprice = parseFloat($("#price").val());
        if ($("#id_size_1").is(":checked")) {
          if ($("#id_size_2").length) {
            baseprice = parseFloat($(".sprice-" + id).text());
          } else {
            baseprice = parseFloat($(".lprice-" + id).text());
          }
        } else if ($("#id_size_2").is(":checked")) {
          baseprice = parseFloat($(".lprice-" + id).text());
        }
        if (id > 23 && id < 39) {
          let extra = $("li.selected").length * 0.5;
          baseprice = baseprice + extra;
        }
        let quantity = parseFloat($("#id_quantity").val());
        let newprice = baseprice * quantity;
        $("#price").val(newprice.toFixed(2));
      });

      //delete modal html after it is closed.
      $(".modal").on("hidden.bs.modal", () => {
        $(".modalslot").empty();
      });
      //submit form
      $("#sform").submit(e => {
        const x = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        e.preventDefault();
        $.ajax({
          headers: {
            "X-CSRFToken": x
          },
          type: "POST",
          url: "/modal/",
          datatype: JSON,
          data: {
            size: $(".form-check-input:checked").val(),
            quantity: $("#id_quantity").val(),
            itemid: id,
            price: $("#price").val(),
            toppings: $("#id_toppings.selectpicker").val()
          },
          success: function() {
            $(".modal").modal("hide");
            return false;
          },
          error: function(newdata) {
            $(".modalslot").empty();
            $(".modalslot").append(newdata);
            $(".modal").modal("show");
          }
        });
      });
    }
  });
});
