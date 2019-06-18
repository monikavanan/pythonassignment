# -*- coding: utf-8 -*-
ravi={'sub1':67,'sub2':87,'sub3':78,'sub4':56,'sub5':87,'sub6':90}
rashmi={'sub1':89,'sub2':98,'sub3':78,'sub4':56,'sub5':87,'sub6':45}
lokesh={'sub1':78,'sub2':75,'sub3':68,'sub4':84,'sub5':95,'sub6':93}
temp=0
for i in ravi.values():
    temp=sum(ravi.values())
print(temp)
temp1=0
for i in rashmi.values():
    temp1=sum(rashmi.values())
print(temp1)
temp2=0
for i in lokesh.values():
    temp2=sum(lokesh.values())
print(temp2)
        
print((max(temp,temp1,temp2)))

#x=ravi['sub1']
#y=rashmi['sub1']
#z=lokesh['sub1']
#print(max(x,y,z),'highest')
  
sub1={'ravi':67,'rashmi':89,'lokesh':78}
sub2={'ravi':87,'rashmi':98,'lokesh':75}
sub3={'ravi':78,'rashmi':78,'lokesh':68}
sub4={'ravi':56,'rashmi':56,'lokesh':84}
sub5={'ravi':87,'rashmi':87,'lokesh':95}
sub6={'ravi':90,'rashmi':45,'lokesh':93}
print("highest score in sub1",max(zip(sub1.values(),sub1.keys())))
print("highest score in sub2",max(zip(sub2.values(),sub2.keys())))
print("highest score in sub3",max(zip(sub3.values(),sub3.keys())))
print("highest score in sub4",max(zip(sub4.values(),sub4.keys())))
print("highest score in sub5",max(zip(sub5.values(),sub5.keys())))
print("highest score in sub1",max(zip(sub6.values(),sub6.keys())))

print("lowest score in sub1",min(zip(sub1.values(),sub1.keys())))
print("lowest score in sub2",min(zip(sub2.values(),sub2.keys())))
print("lowest score in sub3",min(zip(sub3.values(),sub3.keys())))
print("lowest score in sub4",min(zip(sub4.values(),sub4.keys())))
print("lowest score in sub5",min(zip(sub5.values(),sub5.keys())))
print("lowest score in sub1",min(zip(sub6.values(),sub6.keys())))
