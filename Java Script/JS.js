/**
 * Created by Admin on 3/10/2017.
 */
console.log("hello java script");
//JS.js:4 hello java script


var numberOne = 7;

var numberTwo = 3;

var result = numberOne + numberTwo;

//JS.js:12 10

console.log(result);

function add(num1, num2) {
    return num1+num2;
    // JS.js:18 454
}

console.log(add(100,354));

//syntax: first item is the "function" key word, next 
// the "function name (add), next the parameters (num1,num2) and end the line with
// semicolons (;), next add curly braces "{}" 
// next create a return function with variables from the parameter and end wtih (;)
// last print to the console with following syntax: console.log(add(100,354).
// Run from your html console, right click for menu and select inspect. Select the Console
// tab and observe the print out. It should show the results of your function program