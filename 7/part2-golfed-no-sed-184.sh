a=`head -1|tr .S 01`;a=(${a//?/& });while read c;do IFS=+ b=(${a[@]});for((i=0;++i<${#c}-1;))do [ ${c:i:1} = ^ ]&&((b[i-1]+=b[i],b[i+1]+=b[i],b[i]=0))done;a=(${b[@]});done;bc<<<${a[*]}
