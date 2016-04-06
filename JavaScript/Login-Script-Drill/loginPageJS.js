$(document).ready(function () {
    //hide the p tags
    $("li").hide();

    //Click to show the p tag
    $(".dropdown").mouseenter(function () {
        $("li").show(500);
        $(".dropbtn").css({
            "background-color": "#0ca3d2",
            "border-radius": "25px 25px 0px 0px"
        });
    });
    $(".dropdown").mouseleave(function () {
        $("li").hide(500);
        $(".dropbtn").css({
            "background-color": "initial",
            "border-radius": "25px"
        });
    });
    $("li").mouseenter(function () {
        $(this).css({
            "background-color": "initial",
        });
    });
    $("li").mouseleave(function () {
        $(this).css({
            "background-color": "#0ca3d2",
        });
    });

    lightbox.option({
        'resizeDuration': 200,
        'wrapAround': true,
    })
});
