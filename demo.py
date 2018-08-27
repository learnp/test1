'''
num = 0
mylist = []
while num < 10:
    num = num + 1
    mylist.append(num)
print(mylist)
'''
'''
l=[1,2,5,7,8,9]
print(l[:])
print(l[2:])
print(l[1:3:])
print(l[1:3:-1])
print(l[::2])
print(l[::-1])
'''

#from functools import reduce
l=[1,2,3,4,5,6]
#print(list(map(lambda x:x%2==0,l)))
def even(num):
    if num%2==0:
        return num
    
b=list(map(even,l))
l2=[]
for x in b:
    if x==None:
        pass
    else:
        l2.append(x)
print(l2)
#print(b)
	
#r =  list(filter(even, [1,2,3,4]))
#print(r)

    
    
#print(list(map(cube,l)))

'''class hari(a,b):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        return self.a+self.b
    
aa=hari(3,2)
s=aa.display()
print(s)
'''
'''l=[1,3,5,6,7,0,8,10,2,4]
for x in range(1,11):
    if x in l:
        pass
    else:
        print(x)
        
'''
'''
l=[1,3,5,6,7,0,8,10,2,4]
for x in range(1,11):
    if x not in l:
        print(x)
   
'''
'''

from collections import OrderedDict
thisdict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red",
  1: 'apple', 
  2: 'ball'
}

print(OrderedDict(thisdict))
'''



'''
l=["u","e","a","i","o"]
l.sort()
print(l)
'''
'''
a='werders'
b=sorted(a)
a='werders'
b=sorted(a)
for x in b:
    print(x,end="")
print(str(b))
print(a[::-1])
'''
'''from functools import reduce
l=[1,2,3,4,5]
print(reduce(lambda x,y:x+y,l))
'''   
'''
x = [2, 8, 1, 4, 6, 3, 7]
x.sort()
print(x)
print(sorted(x))
'''
'''
import re
l=[]
f=open("hari1.txt")
x=f.read()
res=re.findall("\d",x)
for x in res:
    y=int(x)
    l.append(y)
print(sum(l))
    
 '''   


'''
for x in l3:
    z=''.join(l3)
    print(z)
'''
'''
l=['hari@gmail.com','mouni@abc.com','ram@xyz.com','krishna@bac.com']
l.sort(key=lambda x:x.split('@')[1])
print(l)
'''
'''   
class hari:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a, '+',self.b)
        
hari(2,3).display()



a='Werders'
b=sorted(a.lower())
print(b)

'''

        
hungry=input("eat something")
if hungry=="yes":
    print("eat samosa")
else:
    print("do homw work")
        
        
        
    
    


 
 



    

        
    
    
    
    
    
    
    
    


    
    
    
    
    
    
    
    

    

        
        
        
 
    
    
    
    
    


        











            
    
    
    


