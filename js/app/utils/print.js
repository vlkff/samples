console.log('print.js imported');

// A shortcut for console.log
function log(label, variable = "") {
    if(variable == "") {
        console.log(label);
    } else {
        console.log(label + ': '+ variable);
    }
    console.log('\n');
}

export {log}
