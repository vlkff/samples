//
// Most handy, clean and readable way to create a module if we don't follow the pattern where we always
// use return constructor from module and use 'new' at requested side.
//

console.log('module g.js included');

// Just create ready-to use empty object on the start
var Module = new Object();

// Declare some local object
function demo_gf () {
    console.log('g/demo_f() called');
}

// Those which need to be exported, append to Module object
Module.demo_gf = demo_gf;

// And export all appended at once in the end
export default Module;