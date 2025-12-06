d=`cat`
while((++i))
rev<<<$d|sed ':x
s/ \([+*]\)/\1\1/g
tx
$s/.$//'|cut -c$i|tr -d \\n|grep .
do :
done|sed -Ez 's/\n *[+*]/+/g
s/([+*])\n/\1/g
s/[+*]\+/+/g'|bc
