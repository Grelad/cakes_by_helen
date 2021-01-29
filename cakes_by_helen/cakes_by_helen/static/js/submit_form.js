$(document).ready(function () {
    $("#submit-order").submit(function (event) {
      $("#message").empty();
      $.ajax({
            type: "POST",
            url: "/ajax/submit_form/",
            data: {
                'name' : $('#name').val(),
                'phone' : $('#phone').val(),
                'comment' : $('#comment').val(),
                'type' : 'classic_cake',
            },
            dataType: 'json',
            success: function (response) {
                $("#submit-form").hide();
                $('#message').html(JSON.success);
                $("#message").show();
                console.log("Success")
                setTimeout(function(){
                  $(".notification-block").hide();
                }, 3000);
            },
            error: function (response) {
                $('#message').html(response.error);
                $("#message").show();
                console.log("Error should be displayed")
            },
        });
        return false;
    });
});
