import random 
print("random number generator")
print("enter y to generate new random number")
while input('generate [y/n]:')=='y':
    number =random.randint(1000,9999)
    print(f'lucky number:{number}')
print("thanks for using")