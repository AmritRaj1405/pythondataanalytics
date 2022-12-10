a=input("enter a number")
b=input("enter another number")
if a.isnumeric() and b.isnumeric():
    a,b=int(a),int(b)
    c=a+b
    print("the sum of the number is:",c)
else:
    print("please enter numbers only")