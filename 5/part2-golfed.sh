grep -|sort -n|(while IFS=- read s e;do((s=s<=p?p+1:s,s>e?0:(p=e,t+=e-s+1)));done;echo $t)
