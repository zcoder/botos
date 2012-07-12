#!/usr/bin/env bash

text="${*}";
var=$(curl -sd "a=sl&sl=${text}" 'http://slogen.ru/srv.php');
/usr/bin/env php get_text.php "$var"
