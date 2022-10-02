var page = document.currentScript.getAttribute('page');
var block = document.currentScript.getAttribute('block');
$.ajax({
    url: page,
    method: 'get',
    success: function(data){
        $(block).html(data);
    },
    async: false
})