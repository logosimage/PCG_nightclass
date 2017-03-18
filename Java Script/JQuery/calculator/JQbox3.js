/**
 * Created by Admin on 3/13/2017.
 */

$(document).ready(function () {


    $("#buttonOne").on("click", function () {
        var fieldOneText = $("#fieldOne").val();
        var fieldTwoText = $("#fieldTwo").val();
        add(fieldOneText, fieldTwoText);

    });

    $("#buttonTwo").on("click",function(){
        var fieldOneText = $("#fieldOne").val();
        var fieldTwoText = $("#fieldTwo").val();
        subtract(fieldOneText, fieldTwoText);
    });


    $("#buttonThree").on("click", function(){
        var fieldOneText = $("#fieldOne").val();
        var fieldTwoText = $("#fieldTwo").val();
        multiply(fieldOneText, fieldTwoText);

    });
    $("#buttonFour").on("click", function () {
        var fieldOneText = $("#fieldOne").val();
        var fieldTwoText = $("#fieldTwo").val();
        divide(fieldOneText, fieldTwoText);

    });
function add(numOne, numTwo) {
        var one = parseFloat(numOne);
        var two = parseFloat(numTwo);
        console.log(one + two)
    }



    function subtract(numOne, numTwo){
        var one = parseFloat(numOne);
        var two = parseFloat(numTwo);
        console.log(one - two)
    }


    function multiply(numOne, numTwo){
        var one = parseFloat(numOne);
        var two = parseFloat(numTwo);
        console.log(one * two)

    }
    function divide(numOne, numTwo){
        var one = parseFloat(numOne);
        var two = parseFloat(numTwo);
        console.log(one / two)
    }




});


