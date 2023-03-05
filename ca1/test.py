num=1010001111010
base=3
list1=[]
maximum=0
count=0
while (num>0):
    rem=num%base
    list1.append(rem)
    num=num//base
for i in list1:
    if i==0:
        count+=1
        if count>maximum:
            maximum=count
    else:
        count=0
print(maximum)
print(list1)