sort -n|while IFS=- read s e;do echo $[(s=s>p?s:p+1)>e?0:e?(p=e,t+=e-s+1):0];done
