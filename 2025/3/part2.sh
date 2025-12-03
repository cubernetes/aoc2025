xargs -L1 bash -c 'for i in {-11..0};do c=$b;read b a< <(grep -o .<<<${0:b:${#0}-b+i}|nl|sort -sk2|uniq -f1|tail -1);d+=$a;((b+=c));done;echo $d'|paste -sd+|bc
