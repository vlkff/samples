console.log('module f.js included');

var Module = function () {
    console.log('e module object constructor called');

    this.module_name = 'e';

    this.demo_ff = function () {
        console.log('f/demo_f() called');
    }
};

var module = new Module();
export default module;
