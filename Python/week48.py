"""
This application receives a date and determines 
whether or not you are in time to receive a gift 
for an event from 12/1 to 12/24.
"""

import datetime as dt


present_list = [
    'Pragmatic programmer(book)',
    'while True: learn()',
    'Learn JS - Nicolas Schuman',
    'Design Patterns - H. Leon',
    'Learn Python',
    'iOS programming with Swift',
    'Popsy licence',
    'JS from Scratch - Azaustre',
    'Inteligencia Matemática - Cabezon',
    'Flutter - Herrera',
    'Que puede salir mal? - Herrera',
    'Figma para developers',
    'Dominios.dev',
    'MasterMind',
    'El bolson de higgs no te va a hacer la cama',
    'T-Shirt',
    'Hack4u',
    'Codigo sostenible',
    'GeeksHubs Academy',
    'La artesania del codigo limpio',
    'Codely.com courses',
    'Atomic Habits',
    'Programming book'
]
presents_dict = {}
for num, present in zip(range(1, 25), present_list):
    presents_dict[dt.date(2022, 12, num)] = present

def get_date() -> dt.date:
    """
    Gets and validates a date entered by the user    
    """
    while True:
        try:
            date = []
            for var in ['year', 'month', 'day']:
                print(f"Insert {var}: ", end="")
                date.append(int(input()))
            new_date = dt.date(date[0],date[1],date[2])
        except ValueError:
            print("Try again")
        else:
            return new_date

def find_prize(date:dt.date):
    if date in presents_dict:
        print(f'Congrats! Your prize is "{presents_dict[date]}"')
    else:
        ans = abs(dt.date(2022, 12, 24) - date) / dt.timedelta(days=1)
        print(f"You're {ans} days late")


date = get_date()
find_prize(date)