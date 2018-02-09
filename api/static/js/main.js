$(document).ready(function () {

    $('#text').submit(function (e) {
        e.preventDefault();

        if ($.trim($("#id_string").val()) !== '') {

            $.ajax({
                data: $(this).serialize(),
                type: 'GET',
                url: '/api/uploadText/',
                dataType: 'json',
                async: false,
                complete: function (response) {
                    data = response.responseJSON;
                }
            });
            $("#id_string").val('');
            $("#message").text(data['message']);
        }
        else {
            $("#message").text('Введите данные!');
        }

    });

});