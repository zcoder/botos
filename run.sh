#!/usr/bin/env bash

declare -x DISPLAY=":0"
declare -x HOME="/home/botos"
declare -x LANG="ru_RU.UTF-8"
declare -x PATH="/usr/lib/lightdm/lightdm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games"

runcheck=1;
while [ $runcheck -ne 0 ]; 
do
	echo 'run skype ..!';
	pgrep skype &>/dev/null; 
	runcheck=$?;
done;
echo "continue starting ...";

DISPLAY=":0" /usr/bin/env python botos.py

