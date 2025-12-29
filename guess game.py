secret=5
user=input('guess number: ')
trials=0
User=int(user)
while User!=secret:
    User=int(input('try again: '))
    trials=trials+1
    if trials==3:
        print('you fail')
        break
else:
    print('you won')