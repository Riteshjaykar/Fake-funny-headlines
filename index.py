import random #imported random file to choose a randome words from a list
sub=[
    'Pratik',
    'Siddhesh ',
    'Varad ',
    'Rikshaw Driver',
    'Car Driver',
    'Corporate man'
]
act=[
    'dance on a car',
    'got a bag ',
    'falls in a toilet',
    'is bankrupt',
    'launched new book',
    'lost'
]
place=[
    'in the space',
    'with bottle in hand',
    'at taj mahal',
    'while doing workout'
]
while True:
    user_input =input(
        '\nDo you want to create new fake and funny News by using your choice Name !!!'
        '\n If yes then type yes '
        '\n if you want to continue default Generator then print no : '
        '\n Do you want to Exit ? type exit : ').strip().lower()
    if user_input=='yes':
        s=input("Enter A name for e.g. --> Friend/family member/anyone = ")
        while True:
            subject = random.choice(sub)
            action = random.choice(act)
            places = random.choice(place)
            news = f' BREAKING NEWS : {s} {action} {places}'
            print('\n ' + news)
            break

    elif user_input=='no':
        while True:
            subject = random.choice(sub)
            action = random.choice(act)
            places = random.choice(place)
            news = f' BREAKING NEWS : {subject} {action} {places}'
            print('\n ' + news)
            break
    elif user_input=='exit':
        print("\n Thanks for using fake headline news Generator")
        break
    else:
        print('invalid Input ')
