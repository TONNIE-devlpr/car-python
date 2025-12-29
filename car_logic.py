user=input('> ')
while user.lower()=='help':
    print('''
    start- to start the car
    stop- to stop the car
    quit- to exit 
    ''')
    choice=input('> ')
    if choice.lower()!='quit':
        if choice.lower()=='start':
            print('car has started...ready to go!')

        elif choice.lower()=="stop":
            print('car has stopped')

        else:
            print('i did not understand!')

    elif choice.lower()=='quit':
        print('you exit!')

else:
    print('i did not understand')
