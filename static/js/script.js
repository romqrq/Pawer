
$(document).ready(function() {
    $('.collapsible').collapsible();
    $('select').material_select();
    $(".button-collapse").sideNav();
    $('.parallax').parallax();
});

//On click it shows the form related to the account type being created while hiding 
//the other forms
$('.account-type').click(function(){
    form_type = $(this).attr('value')
    $(`#${form_type}`).removeClass('hide')
    
    console.log($(`#${form_type}`).siblings().not('.hide').addClass('hide'))
});

//Event triggered by click to show "edit form" and hide the "delete form" any forms
//belonging to other user_id's are being displayed.
$('.edit-button').click(function(){
    user_id = $(this).attr('id')
    // $(`.edit-form-box, #${user_id}`).not('.delete-form-box').removeClass('hide')
    // $(`.edit-form-box, .delete-form-box` ).not(`#${user_id}`).addClass('hide')
    // $(`.delete-form-box`).not('.hide').addClass('hide')
    // $(`.edit-form-box, #${user_id}`).scrollIntoView();
    $(`#${user_id}.edit-form-box`).removeClass('hide');
    $('.edit-form-box').not(`#${user_id}`).addClass('hide');
    $('.delete-form-box').not('.hide').addClass('hide');

});

//Event triggered by click to show "delete form" and hide the "edit form" or any forms
//belonging to other user_id's that are being displayed.
$('.delete-button').click(function(){
    user_id = $(this).attr('id');
    $(`#${user_id}.delete-form-box`).removeClass('hide');
    $('.delete-form-box').not(`#${user_id}`).addClass('hide');
    $('.edit-form-box').not('.hide').addClass('hide');
    // $(`.delete-form-box#${user_id}`).scrollIntoView();
    // elTarget = $(`#${user_id}.delete-form-box`);
    // setTimeout(scrollDown(elTarget), 1000);

});

/**
 * Function to scroll down and bring form to view
 */
// function scrollDown(elTarget) {
// console.log(elTarget);
// elTarget.scrollIntoView(false);
// console.log(elTarget);

// }

$('#is_staff').click(function(){
    console.log(this)
});
$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
});

 

