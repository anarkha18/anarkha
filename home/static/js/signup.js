$(document).ready(function () {
    $('#fninvalid').hide();
    $('#lninvalid').hide();
    $('#pasinvalid').hide();
    $('#cpasinvalid').hide();
    $('#eminvalid').hide();

    var fn_error = true;
    var ln_error = true;
    var pass_error = true;
    var cpaSss_error = true;
    var em_error = true;

    $('#fn').keyup(function () {
        fn_check();
    });
    function fn_check() {

        var fn_val = $('#fn').val();
        if (fn_val.trim() == "") {
            $('#fninvalid').show();
            $('#fninvalid').html('Name Cannot be Empty');
            $('#fninvalid').focus();
            $('#fninvalid').css("color", "red");
            fn_error = false;
            return false;
        } else {
            $('#fninvalid').hide();
        }

        if (fn_val.length < 3) {
            $('#fninvalid').show();
            $('#fninvalid').html('Name is too Short');
            $('#fninvalid').focus();
            $('#fninvalid').css("color", "red");
            fn_error = false;
            return false;
        } else {
            $('#fninvalid').hide();
        }
    }
    $('#ln').keyup(function () {
        ln_check();
    });
    function ln_check() {

        var ln_val = $('#ln').val();
        if (ln_val.trim() == "") {
            $('#lninvalid').show();
            $('#lninvalid').html('Name Cannot be Empty');
            $('#lninvalid').focus();
            $('#lninvalid').css("color", "red");
            ln_error = false;
            return false;
        } else {
            $('#lninvalid').hide();
        }
        if (ln_val.length < 3) {
            $('#lninvalid').show();
            $('#lninvalid').focus();
            $('#lninvalid').html('Name is too Short');
            $('#lninvalid').css("color", "red");
            ln_error = false;
            return false;
        } else {
            $('#lninvalid').hide();
        } l


    }

    $('#pas').keyup(function () {
        pas_check();
    });
    function pas_check() {
        var pas_val = $('#pas').val();
        if (pas_val.trim() == "") {
            $('#pasinvalid').show();
            $('#pasinvalid').html('Password Cannot be Empty');
            $('#pasinvalid').focus();
            $('#pasinvalid').css("color", "red");
            pas_error = false;
            return false;
        } else {
            $('#pasinvalid').hide();
        }

        if ((pas_val.length < 3) || (pas_val.length > 20)) {
            $('#pasinvalid').show();
            $('#pasinvalid').focus();
            $('#pasinvalid').html('Password Must be Between 3-20 Characters');
            $('#pasinvalid').css("color", "red");
            pas_error = false;
            return false;
        } else {
            $('#pasinvalid').hide();
        }

    }
    $('#cpas').keyup(function () {
        cpas_check();
    });
    function cpas_check() {
        var cpas_val = $('#cpas').val();
        var pas_val = $('#pas').val();

        if (cpas_val.trim() == "") {
            $('#cpasinvalid').show();
            $('#cpasinvalid').html('This Fiesld Cannot be Empty');
            $('#cpasinvalid').focus();
            $('#cpasinvalid').css("color", "red");
            cpas_error = false;
            return false;
        } else {
            $('#cpasinvalid').hide();
        }

        if (pas_val != cpas_val) {
            $('#cpasinvalid').show();
            $('#cpasinvalid').focus();
            $('#cpasinvalid').html('Passwords are not Matching');
            $('#cpasinvalid').css("color", "red");
            cpas_error = false;
            return false;
        } else {
            $('#cpasinvalid').hide();
        } l
    }

    $('#em').keyup(function () {
        em_check();
    });
    function em_check() {
        var em_val = $('#em').val();
        var pattern = /^[A-Za-z._]{3,}@[A_Za-z]{3,}[.]{1}[A-Za-z.]{2,6}$/;

        if (em_val.trim() == "") {
            $('#eminvalid').show();
            $('#eminvalid').html('Email Cannot be Empty');
            $('#eminvalid').focus();
            $('#eminvalid').css("color", "red");
            em_error = false;
            return false;
        } else {
            $('#eminvalid').hide();
        }

        if (!pattern.test(em_val)) {
            // alert("Sdfdf");
            $('#eminvalid').show();
            $('#eminvalid').html('Your email must be a valid email');
            $('#eminvalid').focus();
            $('#eminvalid').css("color", "red");
            em_error = false;
            return false;
        } else {
            $('#eminvalid').hide();
        }
    }

    $('#submitbtn').click(function () {
        fn_error = true;
        ln_error = true;
        pass_error = true;
        cpass_error = true;
        em_error = true;

        fn_check();
        ln_check();
        pas_check();
        cpas_check();
        em_check();

        if ((fn_check == true) && (ln_check == true) && (pas_check == true)
            && (cpas_check == true) && (em_check == true)) {
            return true;
        }
        else {
            return false;
        }

    });

});