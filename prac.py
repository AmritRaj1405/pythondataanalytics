data=" "
while True:
    line=input(">>>>")
    data +=line+" "
    if line ==0:
        break
        print(data)
    with open (redbook.txt, 'w') as file:
        file.write(data)