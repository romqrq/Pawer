
$(document).ready(function() {
        $('.collapsible').collapsible();
        $('select').material_select();
        $(".button-collapse").sideNav();
        $('.parallax').parallax();
        $('.carousel').carousel();
    });

    $('.account-type').click(function(){
        form_type = $(this).attr('value')
        $(`#${form_type}`).removeClass('hide')
        
        console.log($(`#${form_type}`).siblings().not('.hide').addClass('hide'))
    })
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        closeOnSelect: false // Close upon selecting a date,
    });

 

