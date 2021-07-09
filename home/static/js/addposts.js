$(document).ready(function () {
    $('#titleer').hide();
    $('#authorer').hide();
    $('#contenter').hide();
    $('#slger').hide();

    var title_error = true;
    var aut_error = true;
    var slg_error = true;
    var content_error = true;

    $('#title').keyup(function () {
        title_check();
    });
    function title_check() {

        var title_val = $('#title').val();
        if (title_val.trim() == "") {
            $('#titleer').show();
            $('#titleer').html('Title Cannot be Empty');
            $('#titleer').focus();
            $('#titleer').css("color", "red");
            title_error = false;
            return false;
        } else {
            $('#titleer').hide();
        }

        if (title_val.length < 10) {
            $('#titleer').show();
            $('#titleer').html('Title is too Short');
            $('#titleer').focus();
            $('#titleer').css("color", "red");
            title_error = false;
            return false;
        } else {
            $('#titleer').hide();
        }
    }
    $('#author').keyup(function () {
        aut_check();
    });
    function aut_check() {

        var aut_val = $('#author').val();
        if (aut_val.trim() == "") {
            $('#authorer').show();
            $('#authorer').html('Author Cannot be Empty');
            $('#authorer').focus();
            $('#authorer').css("color", "red");
            aut_error = false;
            return false;
        } else {
            $('#authorer').hide();
        }

        if (aut_val.length < 4) {
            $('#authorer').show();
            $('#authorer').html('Author Name is too Short');
            $('#authorer').focus();
            $('#authorer').css("color", "red");
            aut_error = false;
            return false;
        } else {
            $('#authorer').hide();
        }
    }

    $('#slgs').keyup(function () {
        slg_check();
    });
    function slg_check() {

        var slg_val = $('#slgs').val();
        if (slg_val.trim() == "") {
            $('#slger').show();
            $('#slger').html('Title Cannot be Empty');
            $('#slger').focus();
            $('#slger').css("color", "red");
            slg_error = false;
            return false;
        } else {
            $('#slger').hide();
        }

        if (slg_val.length < 5) {
            $('#slger').show();
            $('#slger').html('Slug is too Short');
            $('#slger').focus();
            $('#slger').css("color", "red");
            slg_error = false;
            return false;
        } else {
            $('#slger').hide();
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

        if (content_val.length < 20) {
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

    $('#sub').click(function () {

        title_error = true;
        aut_error = true;
        slg_error = true;
        content_error = true;

        title_check();
        aut_check();
        slg_check();
        content_check();

        if ((title_error == true) && (aut_error == true) && (slg_error == true) && (content_error == true)) {
            return true;
        }
        else {
            return false;
        }

    });
});