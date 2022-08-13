<?php
/**
 * Namespaces is a common modern way to organize modularity of the app and components.
 */
namespace namespaces\demo;

echo 'File ' . __FILE__. ' included ' . PHP_EOL;
echo 'The namespace is '. __NAMESPACE__.PHP_EOL;

function demo_func() {
    echo 'Function ' . __FUNCTION__ . '() been called'.PHP_EOL;
}

require_once 'a.php';
use namespaces\a;
a\demo_func();

use namespaces\c;
c\demo_func();

use function namespaces\a\another_demo_func;
another_demo_func();

require_once 'b.php';
use function namespaces\b\demo_func as b_demo_func;
b_demo_func();

__NAMESPACE__\demo_func();


