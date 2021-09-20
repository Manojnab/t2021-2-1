base=[1,2,3,4,5,6,7,8,9]
inp=[1,2,8,9,12,46,76,82,15,20,30]
dicti1={}
for ele in base:
    count=0
    for ele1 in inp:
        if ele1%ele==0:
            count+=1
    dicti1[ele]=count
print(dicti1)
