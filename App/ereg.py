k=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
up=""
for i in k:
 up+="".join(str(i))
s=""

for i in range(len(up)):
 s+="*"
print s
s=list(s)
res=""
for i in range(0,len(s),2):
 s[i:i+2]=up[i:i+2]
 print "".join(s)
res+="".join(s)
#print res
