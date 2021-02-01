print('        Welcome to calculator \n')
again = 'again'
while again == 'again':
    n0 = float(input('Number : '))
    o = input('Operator : ')
    while True:
        if o != '=':
            n1 = float(input('Number : '))
            if o== '+' :
                n0= n0+n1
            elif o== '-' :
                n0= n0-n1
            elif o== '*' :
                n0= n0*n1
            elif o== '/' :
                n0= n0/n1
            o = input('Operators : ')
        else :
            print(n0)
            break
    again = input('ENTER again TO MORE OR exit TO FINISH : ')
    if again == 'exit':
        break

print('GOOD BYE')

    
    
