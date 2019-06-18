# -*- coding: utf-8 -*-
data=[2,4,1,47,38]
r=0
for i in range(0,5):
        r=r+data[i]
print(r)




#maximumelement
data=[2,4,1,47,38]

for i in range(0,4):
    if(data[i]>data[i+1]):
        num=data[i]
print(num)

#minimumelement
data=[2,4,1,47,38]

for i in range(0,4):
    if(data[i]<data[i+1]):
        num=data[i]
print(num)


#average

data=[2,4,1,47,38]
r=0
no=len(data)
for i in range(0,5):
    r=r+data[i]/no
print(r)

#search
data=[2,4,1,47,38]
flag=0
key=int(input('enter the key to be searched'))
for i in range(0,5):
    if(data[i]==key):
        flag=1
        break
if(flag==1):
    print('key found',data[i])
else:
    print('key not found')

