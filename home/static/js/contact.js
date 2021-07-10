$(document).ready(function () {
    $('#nmer').hide();
    $('#emer').hide();
    // $('#pher').hide();
    $('#contenter').hide();

    var nm_error = true;
    var em_error = true;
    // var ph_error = true;
    var content_error = true;

    $('#name').keyup(function () {
        name_check();
    });
    function name_check() {

        var name_val = $('#name').val();
        if (name_val.trim() == "") {
            $('#nmer').show();
            $('#nmer').html('Name Cannot be Empty');
            $('#nmer').focus();
            $('#nmer').css("color", "red");
            nm_error = false;
            return false;
        } else {
            $('#nmer').hide();
        }

        if (name_val.length < 4) {
            $('#nmer').show();
            $('#nmer').html('Name is too Short');
            $('#nmer').focus();
            $('#nmer').css("color", "red");
            nm_error = false;
            return false;
        } else {
            $('#nmer').hide();
        }
    }
    $('#email').keyup(function () {
        em_check();
    });
    function em_check() {
        var em_val = $('#email').val();
        var pattern = /^[A-Za-z._]{3,}@[A_Za-z]{3,}[.]{1}[A-Za-z.]{2,6}$/;

        if (em_val.trim() == "") {
            $('#emer').show();
            $('#emer').html('Email Cannot be Empty');
            $('#emer').focus();
            $('#emer').css("color", "red");
            em_error = false;
            return false;
        } else {
            $('#emer').hide();
        }

        if (!pattern.test(em_val)) {
            $('#emer').show();
            $('#emer').html('Your email must be a valid email');
            $('#emer').focus();
            $('#emer').css("color", "red");
            em_error = false;
            return false;
        } else {
            $('#emer').hide();
        }
    }
    $('#content').keyup(function () {
        content_check();
    });
    function content_check() {

        var content_val = $('#content').val();
        if (content_val.trim() == "") {
            $('#contenter').show();
            $('#contenter').html('This Field Cannot be Empty');
            $('#contenter').focus();
            $('#contenter').css("color", "red");
            content_error = false;
            return false;
        } else {
            $('#contenter').hide();
        }

        if (content_val.length < 10) {
            $('#contenter').show();
            $('#contenter').html('Your message is too Short');
            $('#contenter').focus();
            $('#contenter').css("color", "red");
            content_error = false;
            return false;
        } else {
            $('#contenter').hide();
        }
    }
    // $('#phone').keyup(function () {
    //     phone_check();
    // });
    // function phone_check() {

    //     var ph_val = $('#phone').val();
    //     var pattern = /^(\+\d{1,3}[- ]?)?\d{10}$/
    //     if (ph_val.trim() == "") {
    //         $('#pher').show();
    //         $('#pher').html('This Field Cannot be Empty');
    //         $('#pher').focus();
    //         $('#pher').css("color", "red");
    //         ph_error = false;
    //         return false;
    //     } else {
    //         $('#pher').hide();
    //     }

    //     if (!pattern.test(ph_val)) {
    //         $('#pher').show();
    //         $('#pher').html('Please Enter a Valid Phone Number');
    //         $('#pher').focus();
    //         $('#pher').css("color", "red");
    //         ph_error = false;
    //         return false;
    //     } else {
    //         $('#pher').hide();
    //     }
    // }
    $('#sub').click(function () {
        nm_error = true;
        em_error = true;
        // ph_error = true;
        content_error = true;

        name_check();
        em_check();
        content_check();
        // phone_check();

        if ((nm_error == true) && (em_error == true)
            && (content_error == true)) {
            return true;
        }
        else {
            return false;
        }

    });
});