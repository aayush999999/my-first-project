{% comment %} function func(){
    event.preventDefault();

    console.log('not refreshed!!!!')
} {% endcomment %}


formSubmit.addEventListener('click', function(event){
    event.preventDefault();
});

