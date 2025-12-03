# Credit goes to bashcop. Only here for quick reference.
# 4 bytes shorter than my version with sed.
tr ,- \ |xargs -n2 seq|egrep '^(.+)\1+$'|paste -sd+|bc
