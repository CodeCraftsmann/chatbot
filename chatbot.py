import datetime
import time
import random

joke_list=['My wife told me to stop impersonating a flamingo. I had to put my foot down.',
' I went to buy some camo pants but couldnt find any.',
' I failed math so many times at school, I cant even count.',
'I used to have a handle on life, but then it broke.',
'I was wondering why the frisbee kept getting bigger and bigger, but then it hit me.'
]

greetings=['hi', 'hello', 'good morning', 'good afternoon', 'good evening']
weathers=['weather', 'climate']
times=['date',  'day', 'year']
farewells=['bye', 'good bye', 'gtg', 'see you later', 'exit']
jokes=['joke', 'laugh', 'jokes']
smalls=['how are you', 'how do you do', ]

def greeting(x):
    if x == 'hi' or x=='hello':
        print('hello. i am a an chatbot in development. what would you like me to do')
        #print(greeting(x))
    elif x == 'good morning' or x== 'good afternoon' or x == 'good evening':
        print(x,'pleasant day innit!, what would you like me to do!')
        #print(greeting(x))
    #elif user == 'How are you?':
        return 'i am fine. what would you like me to do!'

def chat():

    while True:
        user=input('enter')
        
        if user in greetings:
            greeting(user)

        elif user in times:
            samayam(user)

        elif user in weathers:
            weather()

        elif user in farewells:
            print("Goodbye! Have a great day.")
            break  # Exit the loop

        elif user in jokes:
            joke()

        elif user in smalls:
            small()

        else:
            unknown()

        #while True:
        

def samayam(x):
    now = datetime.now()
    
    if x == 'date':
        print(now.strftime("%Y-%m-%d"))  

    elif x == 'year':
        print(now.year)  

    elif x == 'day':
        print(now.strftime("%A"))  

    elif x == 'time':
        print(now.strftime("%I:%M %p"))  

def weather():
    print('sorry still learning how to code that! prompt again in few weeks')


def joke():
    selected=random.choice(joke_list)
    print(selected)

def small():
    print('i am a samrt chat bot. what would you like me to do')

def unknown():
    print('sorry i didnt quite catch that. could you say again')


chat()


