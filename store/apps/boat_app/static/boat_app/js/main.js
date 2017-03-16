$(document).ready(function(){
    $("#validationform").submit(function(){
        $("#formspree").submit();
        console.log("form submitted");
        return false;
    });
});
