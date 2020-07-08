import pickle
import os
from config import data

data['date'] = input('enter date: ')
pickleFile = 'LDP_' + data['date'] + '.pickle'

if os.path.isfile(pickleFile):
    with open(pickleFile, 'rb') as handle:
       data = pickle.load(handle)
print(data)
print('\n')

while True:
    response = input('\nCHOOSE ONE:\nwake\nsleep\nexercise\ndream\nmood\nfood\ncognition\nhealth\nprint\nEXIT\n')
    if response == 'EXIT':
        break
    elif response == 'print':
        print(data)
    elif response == 'exercise':
        response = input('please enter:\nwalk\nrun\npushups\nsitups\nstretch\nplank\n')
        if response == 'stretch' or response == 'plank':
            data['exercise'][response] = bool(input('enter True or False: '))
        else:
            data['exercise'][response] = float(input('enter amount: '))
    elif response == 'dream':
        while True:
            response = input('enter a dream element ("end" to end): ')
            if response == 'end':
                break
            else:
                data['dream'].append(response)
    elif response == 'food':
        meal = input('please enter:\nbreakfast, lunch, or dinner: ')
        while True:
            response = input('enter food item ("end" to end): ')
            if response == 'end':
                break
            else:
                data['food'][meal].append(response)
    else:
        value = float(input('enter value: '))
        data[response] = value

with open(pickleFile, 'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
