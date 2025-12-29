weight=input('please enter your weight!: ')
unit=input('weight is in kg or pound '
           'enter K for kg and P for pound: ')
if unit.lower()=='k':
    weight=int(weight)/0.454
    print(f'{weight} lbs')
elif unit.lower()=='p':
    weight=int(weight)*0.454
    print(f'{weight} kg')
else:
    print('out of range')

