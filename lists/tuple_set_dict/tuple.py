x=(1,2,3)#tuple
y=2,4,3,2,1,5 #tuple packing (when so many values)
print(x)
print(y) 
print(type(x))
print(type(y))
print(x[0]) #index 0
print(x[1]) #index 1
print(y[-1]) #index -1
z=(1,2,3,4,5,6,7,8,9,10)
print(z[:5]) #slicing
#tuple method -count , index
a=('Apple','Apple','Banana','Pine Apple','custard Apple')
print(f'len of Apple is {len(a)}')
print(f'Apple occurs {a.count("Apple")} times')
print(f'Pine Apple occurs {a.count("Pine Apple")} times')
print(f'Banana is at index {a.index("Banana")}')
# Tuple to list 
z1= list(z)
print(type(z),type(z1))
print(z,z1)
# list to tuple
zt=tuple(z1)
print(type(z1),type(zt))
print(z1,zt)
#single item tuple
s=(1,)#comma is important 
s2=2, # is also tuple 
print(type(s))
