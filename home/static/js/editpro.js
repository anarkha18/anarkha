$(document).ready(function () {
    $('#fninvalid').hide();
    $('#lninvalid').hide();
    $('#eminvalid').hide();

    var fn_error = true;
    var ln_error = true;
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


    }
    $('#em').keyup(function () {
        em_check();
    });
    function em_check() {
        var em_val = $('#em').val();
        var pattern = /^[A-Za-z0-9._]{3,}@[A_Za-z]{3,}[.]{1}[A-Za-z.]{2,6}$/;

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
        em_error = true;

        fn_check();
        ln_check();
        em_check();

        if ((fn_check == true) && (ln_check == true) && (em_check == true)) {
            return true;
        }
        else {
            return false;
        }

    });

});