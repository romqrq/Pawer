
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
});

//Event triggered by click to show "edit form" and hide the "delete form" any forms
//belonging to other user_id's are being displayed.
$('.edit-button').click(function(){
    // Get user id from card attribute id
    user_id = $(this).attr('id')
    // Removes class "hide" from the element                                        
    $(`#${user_id}.edit-form-box`).removeClass('hide');
    // Adds class "hide" to any other form that doens't have this id
    $('.edit-form-box').not(`#${user_id}`).addClass('hide');
    // Adds class "hide" to delete form in case it is not hidden yet
    $('.delete-form-box').not('.hide').addClass('hide');
    // Scrolls and aligns the bottom of the form with the bottom of the screen
    $('.edit-form-box').not('.hide').get(0).scrollIntoView(false)
});

//Event triggered by click to show "delete form" and hide the "edit form" or any forms
//belonging to other user_id's are being displayed.
$('.delete-button').click(function(){
    // Get user id from card attribute id
    user_id = $(this).attr('id');
    // Removes class "hide" from the element
    $(`#${user_id}.delete-form-box`).removeClass('hide');
    // Adds class "hide" to any other form that doens't have this id
    $('.delete-form-box').not(`#${user_id}`).addClass('hide');
    // Adds class "hide" to delete form in case it is not hidden yet
    $('.edit-form-box').not('.hide').addClass('hide');
    // Scrolls and aligns the bottom of the form with the bottom of the screen
    $('.delete-form-box').not('.hide').get(0).scrollIntoView(false)


});

$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
});

 

