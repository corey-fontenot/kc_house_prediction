/*
    Allows item to be clicked, loading a new page identified by "href"
 */
$(document).ready(function() {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});

$("#img-select").change(function() {
    $(".vis-img").css("display", "none");

    let selected_option = $(this).children("option:selected").val();

    $("#" + selected_option).css("display", "block");
});

$("#data-select").change(function() {
    $(".data-div").css("display", "none");

    let selected_option = $(this).children("option:selected").val();

    $("#" + selected_option).css("display", "block");
});

