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
                'type' : $('#name').val(),
            },
            dataType: 'json',
            error: function (response) {
                $('#message').html(jqXHR.responseText);
                $("#message").show();
                console.log("Error should be displayed")
                },
            success: function (response) {
                $("#submit-form").hide();
                $('#message').html(JSON.success);
                $("#message").show();
                console.log("success")
                console.log(response)
                setTimeout(function(){
                  $(".notification-block").hide();
                }, 3000);
            }
        });
        return false;
    });
});
