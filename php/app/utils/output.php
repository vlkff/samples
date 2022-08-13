<?php

namespace utils\output;

/**
 * As I bored all the time add EOL and didn't found nothing in standard lib
 */
function e($text, $var = '') {
    echo nl2br($text . PHP_EOL);
    if(!empty($var)) {
        echo nl2br($var . PHP_EOL);
    }
}
