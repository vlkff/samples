<?php

namespace basics\data_structures;

require_once '../conf.php';

global $app_root;
require_once $app_root . '/utils/output.php';
use function \utils\output\_echo as e;

/**
 * Compare to another languages php have only one data structure - array, but it simple,
 * flexible and powerful in use at once
 */

$arr = ['one', 'two', 'three'];
$keyed_arr = ['first' => 'one', 'second' => 'two', 'third' => 'three'];

foreach($arr as $value ) {
    $value .= $value;
}

foreach($arr as $key => $value ) {
    $value = $key.'-'.$value;
}

$first_el = $arr[0];
$first_keyed_el = $keyed_arr['first'];


// Lets try to detect a type of array

// That would throw an error as array is not an obj
//$arr_type = get_class($arr);

// that return
$is_array = is_array($arr);
e('is_array usage:') ; var_dump($is_array);

/**
 * Also in php we have iterators and generators
 */