console.log('module e.js included');

//
// A good-practise example if we want to return constructor from module and use 'new' at requested side.
//

export default function () {
    console.log('e module object constructor called');

    this.module_name = 'e';

    this.demo_ef = function () {
        console.log('e/demo_f() called');
    }
};
