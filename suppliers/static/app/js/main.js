// Get produits by categorie_id using ajax

$(function () {
    $("#id_categorie").on("change", function () {
        id_categorie = $(this).val();
        alert(id_categorie);
        $.get(
            "/details_commandes/getPrducts",
            {id_categorie: id_categorie},
            function (data) {
                $("#id_produit").html(data);
            }
        );
    });
});

  // Get unit_price by id_produit
  $(function () {
    $("#id_produit").on("change", function () {
      id_produit = $(this).val();
      alert(id_produit);
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
    id_quantite = $(this).val();
    alert(id_quantite)
    var prix = $('#prix').val();
    var total = id_quantite * prix;
    $('#id_total').val(total);
  });