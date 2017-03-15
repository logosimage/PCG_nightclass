/**
 * Created by Admin on 3/14/2017.
 */

$(document).ready(function(){
/*
    when roundButton is clicked
    change BG-color gray
    change into a circle
    change paragraph text to say  "I'm circle"

     */

    /* SYNTAX FOR ANIMATE FUNCTION
        .animate({
        }, speed, easing,callback function);

     */
    /*
    $("#roundButton").on("click",function(){
$('#square').css({
        backgroundColor: "gray",
        borderRadius: "50%"});
    $("#insideText").html("I'm a circle");
    });




});*/

//     $('#roundButton').on("click",function() {
//         $("#square").animate({
//             borderRadius: "50%"
//
//
//         },500, function () {
//            $(this).css(background-color", "red");
//         });
//     });
// });

    $("#roundButton").on("click", function () {
        changeBackgroundColor("gold", "square");
    });

    });
function changeBackgroundColor(color, id) {
    $("#" + id).css("background-color",color);

}