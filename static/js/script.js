//Loading functions for materialize built in features
$(document).ready(function() {
    $('.collapsible').collapsible();
    $('select').material_select();
    $(".button-collapse").sideNav();
    $('.parallax').parallax();
});

//Function to hide/show form dynamically and scroll it into view
$('.form-trigger').click(function(){
    user_id = $(this).attr('id');
    form_type = $(this).attr('value');
    $('.form-box').not('.hide').addClass('hide');
    $(`#${user_id}.form-box[value=${form_type}]`).removeClass('hide').get(0).scrollIntoView(false);
});

