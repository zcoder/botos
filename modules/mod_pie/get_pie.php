#!/usr/bin/env php

<?php

	set_time_limit(0);
$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin - канал, из которого дочерний процесс будет читать
   1 => array("pipe", "w"),  // stdout - канал, в который дочерний процесс будет записывать 
   2 => array("pipe", "w")   // stderr - файл для записи
);

$cwd = NULL;
$env = NULL;

$process = proc_open('curl -b "userconfirmation=true" http://www.perashki.ru/piro/random/', $descriptorspec, $pipes, $cwd, $env);

if (is_resource($process)) {

	$search_pattern='/<div id="pir\d*.*\d*\/">(.*)<\/div>/';
	$matches=array();
	$handle = $pipes[1];
	while (($buffer = fgets($handle, 4096)) !== false) {
		$buffer = trim($buffer);
		if ( preg_match_all($search_pattern,$buffer,$matches) != 0) {
			$perashki=str_replace("<br/>","\n",$matches[1][0])."\n";
			echo(str_replace("</a></h2>","",$perashki));
			break;			
		}
	}
    $return = fclose($handle);
	$status = proc_get_status($process);
	proc_terminate($process);
    $return_value = proc_close($process);
}

?>
