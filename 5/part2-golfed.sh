grep -|sort -n|(while IFS=- read s e;do(((s=s>p?s:p+1)>e?0:(p=e,t+=e-s+1)))done;echo $t)
