$(document).ready(function () {

    $.ajax({
        data: $(this).serialize(),
        type: 'GET',
        url: '/api/getText/',
        dataType: 'json',
        async: false,
        complete: function (response) {
            data = response.responseJSON;
        }
    });

    $("#message").text(data['list']);

});