function showHideTooltip()
{
    var show = $("#slideTooltip-button-text");

    if  (show.attr('data-show') === '0'){
        show.html('Убрать подсказку ←')
        show.attr('data-show', '1')
        show.removeClass('bouncing-button')
    }
    else{
        show.html('Показать подсказку →');
        show.attr('data-show', '0')
        show.addClass('bouncing-button')
    }
    $(".slideTooltip-data").animate({
      width: "toggle"
    }, 500);
    //$('.slideTooltip-data').toggle("slide", { direction: "right" }, 1000);
    //$('.slideTooltip-data').slideToggle(500);
    //$('.slideTooltip-data').toggleClass('show');
}