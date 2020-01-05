
$(document).ready(function() {
        $('.collapsible').collapsible();
        $('select').material_select();
        $(".button-collapse").sideNav();
        $('.parallax').parallax();
        $('.carousel').carousel();
    });

    $('.with-gap').click(function(acc_type=users){
        acc_type=this.value

    })
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        closeOnSelect: false // Close upon selecting a date,
    });

 

