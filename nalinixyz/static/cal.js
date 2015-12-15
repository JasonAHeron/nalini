$('#2016-1-2').addClass('event');
$('.day-class').click(function(evt){
    console.log(evt.target.id);
    window.location.href = '/days/' + evt.target.id;
});

