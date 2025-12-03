(tr -d '\n';echo ,)|while read -d, r;do IFS=- read s e<<<$r;while ((s++<=e));do grep -E '^(.+)\1+$'<<<$((s-1));done;done|xargs|tr \  +|bc
