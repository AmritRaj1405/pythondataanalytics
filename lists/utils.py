#copy,count,sort,reverse,index methods
x=[12,231,45,12,32,23,11,44,55,1,1,1,1,1,1,1,]
y=x.copy()#creates a copy of x
print(x)
print(y)
c1=x.count(1)#count the number of occurences of 1 in x
print(f'1 occur {c1} times in x')
x.sort()#sort in accending order
print(x)
x.sort(reverse=True)#sort in decending order
print(x)
y.reverse()
print(y)

i231=y.index(231)
print(f'231 is at index{i231} in y')
i12=y.index(12)#returns the index of first occurence of 12 in y
print(f'12 is at index {i12} in y')