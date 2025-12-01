sed s/L/-R/|xargs -n1 sh -c 'yes -- ${0%R*}1|head -${0#*R}'|mapfile -tc1 -C'a(){((a=(${a:=50}+$2)%100))||echo;};a'|wc -l
