$('.day-class').click(function(evt){
    console.log(evt.target.id);
    window.location.href = '/days/?day=' + evt.target.id;
});
