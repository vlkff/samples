<?php

/**
 * But there exists also an old-way to use include/require.
 *
 * It plays with os path and 'include_path' php-option.
 *
 * It might be working, but it has a huge drawback:
 * it include all contents of included file just into a global space
 * and unlike in JS, we have no in php tricks to isolate it in any local closure.
 */

$current_include_path = ini_get('include_path');
echo "Current include path is: PHP_EOL $current_include_path";

// Lets add to the include path some dir from local project
// and include a file from it
// @ToDo