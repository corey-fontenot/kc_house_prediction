/*
    Allows item to be clicked, loading a new page identified by "href"
 */
jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});