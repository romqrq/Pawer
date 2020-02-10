
$(document).ready(function() {
    $('.collapsible').collapsible();
    $('select').material_select();
    $(".button-collapse").sideNav();
    $('.parallax').parallax();
});


$('.form-trigger').click(function(){
    user_id = $(this).attr('id');
    form_type = $(this).attr('value');
    // console.log(form_type);
    // console.log($(`#${user_id}.form-box[value=${form_type}]`));
    $('.form-box').not('.hide').addClass('hide');
    $(`#${user_id}.form-box[value=${form_type}]`).removeClass('hide').get(0).scrollIntoView(false);
});
