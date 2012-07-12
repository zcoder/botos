#!/usr/bin/env bash

s="${*}"

wget -U "Mozilla/5.0" -qO - "http://translate.google.com/translate_a/t?client=t&text=${s}&sl=auto&tl=ru" | sed 's/\[\[\[\"//' | cut -d \" -f 1
