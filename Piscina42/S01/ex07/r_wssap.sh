#!/bin/sh
FT_LINE1=2
FT_LINE2=10
cat /etc/passwd | awk 'NR % 2 == 0' | cut -d: -f1 | rev | sort -r | awk "NR >= $FT_LINE1 && NR <= $FT_LINE2" | paste -sd ', '| sed 's/,/, /g; s/$/./'

