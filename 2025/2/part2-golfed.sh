# Credit to bashcop, alternative version by me using sed
tr ,- \ |xargs -n2 seq|sed -nE 's/^(.+)\1+$/&+\\/p;$a0'|bc

exit
# bashcop's version
tr ,- \ |xargs -n2 seq|egrep '^(.+)\1+$'|paste -sd+|bc
