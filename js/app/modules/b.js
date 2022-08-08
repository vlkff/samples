console.log('module b.js included');

function demo_bf() {
    console.log('b/demo_f() called');
}

var b = new Object();
b.demo_bf = demo_bf;

export {b};