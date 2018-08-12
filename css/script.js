

$('document').ready(function () {
    /* validation */
    $("#login").validate({
        rules: {
            password: {
                required: true,
            },
            user_email: {
                required: true,
                email: true
            },
        },
        messages: {
            password: {
                required: "password"
            },
            user_email: {
                required: "email"
            },
        },
        submitHandler: submitForm
    });
};
    /* validation */