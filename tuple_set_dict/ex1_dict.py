contacts={
    'emergency':'112',
    'office':'9838142453'
}
 
while True:
    print('--> call 📞📞🙎‍♂️')
    print('--> add')
    print('--> exit')
    print('-'*10)
    cnt= input("enter your choise: ")
    if cnt== 'call':
        name=input("enter name of contact:")
        if name in contacts:
            print(f'calling{name} at {contacts[name]}')
        else:
            print(f'{name}  not found')
    elif cnt == 'exit':
        break
    elif cnt == 'add':
        name=input("enter name of contact:")
        number=input("enter number of contact:")
        contacts[name]=number 
        print(f'{name} added sucessfully')
    else:
        print('invalid choice')
    print('-'*10)



