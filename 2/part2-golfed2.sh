tr ,- \ |xargs -n2 seq|sed -nE 's/^(.+)\1+$/&+\\/p;$a0'|bc
