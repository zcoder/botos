<?php

$s = $argv[1];
$b=json_decode($s);
if ($b) print($b->sl."\n");
else print "Нет рекламы...\n";

?>