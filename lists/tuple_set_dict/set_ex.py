a={2,1,4,5}
b={2,3,4,6,5,4,1,2,2,2,4,4,4,3,1,5,7,8}
print(a)
print(b)
# list to set 
c=[1,5,3,2,1,21,12,2,5,1,2,2,5]
cs=set(c)
print(c)
print(cs)
# empty set
d=set()
print(d)
d.add('appleseed')
d.add('Banana')
d.add('Pine Apple')
d.add('custard apple')     
d.add('Apple')
print(d)
d.discard('Apple')# the better way to remove an item 
print(d)
d.remove('Banana')# the dangerous way to remove an item 
print(d)
d.clear()
print(d)
x={1,2,3,4,5,6}
y={1,2,3,8,9,10}
ans=x.difference(y)
print(ans)