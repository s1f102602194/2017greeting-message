<<<<<<< HEAD
from datetime import datetime

def greet():
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
def greet(name):
    message = 'Hello, ' + name + '-san!'
>>>>>>> main
    print(message)


greet('Inoue')
