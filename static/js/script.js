
$(document).ready(function() {
        $('.collapsible').collapsible();
        $('select').material_select();
        $(".button-collapse").sideNav();
        $('.parallax').parallax();
        $('.carousel').carousel();
    });

    // $('.account-type').click(function(){
    //     let type_of_account = $(this).attr('value')
    //     let breed_field = `<div class="input-field col s6">
    //                             <input id="breed" name="breed" type="text" class="validate" required>
    //                             <label for="breed">Breed</label>
    //                         </div>`
    //     let first_name_field = `<div class="input-field col s6">
    //                             <input id="first_name" name="first_name" type="text" class="validate" required>
    //                             <label for="first_name">First Name</label>
    //                         </div>`
    //     let last_name_field =`<div class="input-field col s6">
    //                         <input id="last_name" name="last_name" type="text" class="validate" required>
    //                         <label for="last_name">Last Name</label>
    //                     </div>`
    //     let password_field =`<div class="row">
    //                         <div class="input-field col s12">
    //                             <input id="password" name="password" type="password" class="validate" required>
    //                             <label for="password">Password</label>
    //                         </div>
    //                     </div>`
    //     let email_field = `<div class="row">
    //                         <div class="input-field col s12">
    //                             <input id="email" name="email" type="email" class="validate" required>
    //                             <label for="email">Email</label>
    //                         </div>
    //                     </div>`
    //     let is_staff = `<div class="row">
    //                         <div class="switch">
    //                             <label>
    //                             <input id="is_staff" name="is_staff" type="checkbox">
    //                             <span class="lever"></span>
    //                             Is Staff
    //                             </label>
    //                         </div>
    //                     </div>`
    //     let description_field = `<div class="row">
    //                                 <div class="input-field col s12">
    //                                     <textarea id="description" name="description" class="materialize-textarea"></textarea>
    //                                     <label for="icon_telephone">Short description</label>
    //                                 </div>
    //                             </div>`
    //     if (type_of_account == 'dogs') {
    //         last_name_field = '';
    //         password_field = '';
    //         email_field = '';
    //     } else {
    //         breed_field = '';

    //     }
    //     $("#add_user_form").html(`
    //     <p class="secondary-text">Please fill up the form below</p>

    //     <form action="{{ url_for('insert_${type_of_account}') }}" method="POST" class="col s12">
    //         <div class="row">
    //             ${first_name_field}
    //             ${last_name_field}
    //             ${breed_field}
    //         </div>
    //         ${password_field}
    //         ${email_field}
    //         ${is_staff}
    //         ${description_field}
    //         <div class="row">
    //             <button class="btn waves-effect waves-light" type="submit" name="action">Create Account
    //                 <i class="material-icons right">playlist_add</i>
    //             </button>
    //         </div>
    //     </form>
    //     `)

    })
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        closeOnSelect: false // Close upon selecting a date,
    });

 

