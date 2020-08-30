/*
    Allows item to be clicked, loading a new page identified by "href"
 */
$(document).ready(function() {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});

$("#img-select").change(function() {
    $(".hideable").css("display", "none");

    selected_option = $(this).children("option:selected").val();

    $("#" + selected_option).css("display", "block");
});

