// ToDo: How to get current file name ?
// ToDo: Create a shortcut for console.log
// ToDo: how to define an app root-dir ?

console.log('basic_types.js imported');

import {log} from '../utils/print.js';

log("yo");

// * * * * * * * * * * * * Basic types * * * * * * * * *
// Everything is object
log('.toUpperCase() usage', "Abc".toUpperCase());

var thetype = typeof 5;
log('typeof for 5', thetype);
// 5.somethig() but that doesn't work


// Basic types are

// Strings
var thetype = typeof 'Abc';
log('typeof for "Abc"', thetype);
var thetype = typeof '5';
log('typeof for "5"', thetype);

// Boolean
var thetype = typeof false;
log('typeof for "false"', thetype);

// Numbers

// Integers
var thetype = typeof 5;
log('typeof for 5', thetype);

// Long integers
var bigInt = 1234567890123456789012345678901234567890n;
var thetype = typeof bigInt;
log('typeof for bigInt', thetype);

// Floats
var thetype = typeof 5.1;
log('typeof for 5.1', thetype);

// NaN, Infinity, -Infinity
var thetype = typeof NaN;
log('typeof for "NaN"', thetype);

var thetype = typeof Infinity;
log('typeof for "Infinity"', thetype);

var thetype = typeof -Infinity;
log('typeof for "-Infinity"', thetype);



// Array is a build-in object
// array is ordered, indexed by numbers sequence of elements
// and recognized as 'object'
var theArray = ['one', 'two']
var theArray = new Array('one', 'two');

var thetype = typeof theArray;
log('typeof for array', thetype);

// for keyed arrays, use objects
var indexedArray = {'one': 'one', 'two': 'two'};
log('indexedArray', indexedArray);
// Objects




// Symbols - not sure how to use it
var thetype =  typeof Symbol("id") // "symbol"
log('typeof for Symbol', thetype);

// Function is a build-in object,
// and recognized as 'function'
var func = ()=>{};
var thetype = typeof func;
log('typeof for function', thetype);

// undefined, null
var thetype = typeof undefined;
log('typeof for "undefined"', thetype);

// NaN - not a number ? or this is a number ?
var thetype = typeof null;
log('typeof for "null"', thetype);




// let, var, const
var someVar = 'Abc' // - obsolete method, use let instead
// var has obsolete variable declaration and engine processing behaviour

let someVar = 'Abc';
// let someVar = 'Abc', someNum = 1; - that would

let someVar2 = 'Abc',
    someNum2 = 1;

const someVar = 'Abc';
// someVar = 'Yo'; - that would cause an error