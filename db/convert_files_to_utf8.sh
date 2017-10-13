#!/bin/bash
#description	:To convert all the files in the current directory from Western (Windows 1252) encoding to UTF-8
#author			:Murali Ravivarma


prefix="utf8_"
for entry in *
do
  iconv -f WINDOWS-1252 -t UTF-8  $entry > $prefix$entry
done
