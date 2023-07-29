// Get produits by categorie_id using ajax

$(function () {
    $("#id_categorie").on("change", function () {
        var categorie_id = $(this).val();
        $.get(
            "/get_produits_by_categorie/",
            {"categorie_id": categorie_id},
            function (data) {
                var options = '<option value="">---------</option>';
                data.forEach(function (produit) {
                    options += '<option value="' + produit.id + '">' + produit.nom + '</option>';
                });
                $("#id_produit").html(options);
            }
        );
    });
});

  // Get unit_price by id_produit
  $(function () {
    $("#id_produit").on("change", function () {
      id_produit = $(this).val();
      // alert(id_produit);
      $.get(
        "/details_commande/getUnitPrice",
        {
          id_produit: id_produit,
        },
        function (data) {
          $("#prix").val(data);
        }
      );
    });
  });
  
  $('#id_quantite').on('keyup', function () {
    var id_quantite = $(this).val();
    // alert(id_quantite)
    var prix = $('#prix').val();
    var total = id_quantite * prix;
    $('#id_total').val(total);
  });