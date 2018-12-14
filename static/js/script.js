$(document).ready(function() {
    function background_change(color1, color2, element) {
        // Change background to a lighter shade when element click on
        $(element).on({
            mousedown: function(){
                $(this).css("background-color", color1);
            },
            touchstart: function(){
                $(this).css("background-color", color1);
            }, 
            mouseup: function(){
                $(this).css("background-color", color2);
            },
            mouseleave: function(){
                $(this).css("background-color", color2);
            },
            touchend: function(){
                $(this).css("background-color", color2);
            }
        });
    }
    
    background_change("#72AFD9", "#3e92cc", ".input_button, .play_again, .continue, .submit");
    background_change("#F2A56B", "#ee8434", ".button_back");
    background_change("#F46F79", "#F03A47", ".give_up");
    background_change("#A2CC82", "#80b954", ".skip");
    

    $(".answer_field").keypress(
        // prevent the default(first type of submit inside a form) from firing when 
        // enter has been pressed, instead activate the submit answer button
        function(event){
         if (event.which == '13') {
            event.preventDefault();
            $(".submit_answer").click();
          }
    });
});
