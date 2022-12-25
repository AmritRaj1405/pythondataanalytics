#creating a dictionary
a={'name':'shiva','age':6,'class':'first'}
print(a)

#getting all keys from dictionary 
print(a.keys())
#getting all values from dictionary
print(a.values())                                                                                                                                     
#getting all items from the dictionary as a list of tuple 
print(a.items())
#nested dict 
b={
    'fruits':{'apple':'5kg','custard apple':'3kg'},
    'vegetables':{'cabbage':'1kg','tomato':'500g'},
    'cereals':{'rice':'1kg','wheat':'2kg'}
}
print(b)
print("keys of b=>",b.keys())
print("values of b=>",b.values())

from pprint import pp #for systametic way of data(prety print)
pp(b)

#accessing a value from a dict 
print(a['name'])
print(a['class'])
#print(a['city'])#keyerror:'city'

#accessing a value from a dict using get()
print(a.get('name'))
print(a.get('class'))
print(a.get('city'))#none 
print(a.get('city','not found')) #default value can be specified (comma(,) is uesd in the place of collan(:))
print(a.get('name','not found'))

#traversing a dict   
# style1 
for key in a: 
    print(key,a[key])
#style 2
for key , value in a.items():       
    print(key,value)

#only value
for value in a.values():
    print(value)
#only keys
for key in a.keys():
    print(key)