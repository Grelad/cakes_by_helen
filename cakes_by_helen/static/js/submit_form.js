function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

$(document).ready(function () {
    $("#submit-order").submit(function (event) {
      $("#message").empty();
      $.ajax({
            type: "POST",
            url: "/ajax/submit_form/",
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: {
                'name' : $('#name').val(),
                'phone' : $('#phone').val(),
                'comment' : $('#comment').val(),
                'type' : 'classic_cake',
            },
            dataType: 'json',
            error: function (response) {
                $('#message').html(response.responseJSON.error);
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
