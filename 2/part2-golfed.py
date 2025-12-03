import re
a=0
for r in input().split(','):
 s,e=r.split('-')
 for n in range(int(s),int(e)+1):
  if re.search(r'^(.+)\1+$',str(n)):a+=n
print(a)
