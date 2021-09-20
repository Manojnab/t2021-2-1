a=int(input())
i=0
x=1
li=[]
if a%2==0:
    a-=1
while i<a:
    li.append(x)
    x+=2
    i+=1
#li=",".join(map(int,li))
print(*li,sep=",")
