<?php

namespace namespaces\a;

echo __FILE__. " included " . PHP_EOL;

echo 'The namespace is '. __NAMESPACE__.PHP_EOL;

function demo_func() {
    echo __FUNCTION__ . '() been called'.PHP_EOL;
}

function another_demo_func() {
    echo __FUNCTION__ . '() been called'.PHP_EOL;
}

namespace namespaces\c;
function demo_func() {
    echo __FUNCTION__ . '() been called'.PHP_EOL;
}