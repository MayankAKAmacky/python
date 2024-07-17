
a = int(input('your number please: '))
b = int(input('your second number please: '))
c = a + b
print(f'Your first number is {a} and second number is {b} and the solution is {c}')


name = 'harry'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])


names = ['harry', 'ron', 'hermione']
print(names[1])


# this is called tupple
# tuple always written in the parenthesis
cordinateX = 10.0
cordinateY = 20.0
cordinates = (10.0, 20.0)

# dict is just like object in javascript

# lists in python
# defined a list here
names = ['Harry', 'ron', 'hermione', 'ginny']
print(names)

names.append("draco")
print(names)
    
names.sort()
print(names)

# creats an empty set 
# set has unique elements mostly 

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
print(s)

s.remove(2)
print(s)

print(f'The set has {len(s)} elements ')

# lopps are here in python
# the range means the till that digit
for i in range(10):
    print(i)


# this print every name in the list as you can see in the resut if you run the code 
# nmacky is show that in that we can aything as we want 
names = ['Harry', 'ron', 'hermione', 'ginny']
for nmacky in names:
    print(nmacky)


#thi prints the every character in the word or name in this case 
# macky is show that in that we can aything as we want 
name = "Mayank"
for macky in name:
    print(macky)

# dictionsry is here
house = {'harry': 'gryfitdender', }
print(house)

for i in range(10):
    print(i)
# this is the way to give the value to the variable as you can see

# you can give the value to the variable at same time as written herejj
x, y, z= 'orange', 'banana', 'cherry'
print(x)
print(y)
print(z)

# in this thing you can give the same value to the different variables
xa=ya=za='orange'
print(xa)
print(ya)
print(za)

# this the way to print the things in different ways as you want you can do it like below
the = 'Python is awesome'
t = 'Python '
h = 'is '
e = 'awesome '
print(the)
print(t,h,e) # these two method done same thing
print(t+h+e)   

# the data types are here 
a = 5 # this is the int 
b = 'macky' # this is the string 
c = 1j # this is the complex complex always have the j element end of the number

d = ['vdszv', 'dfgzdgv', 'faergagrfa'] # this is the list
e = {'vdszv', 'dfgzdgv', 'faergagrfa'} # this is the set
f = ('vdszv', 'dfgzdgv', 'faergagrfa') # this is the tuple

# now its time for random number in python
# the python do not have the random function but python uses the random module 
# which we have to import like below in this we can type the range in the given parenhesis
# the random method will only work when the random command is given under the import random command

import random
print(random.randrange(1, 10))
print(random.randrange(10, 20))

string =  'Hello, World!'

print(string[2:5]) # this just the index in python
print(string.strip()) # this function strips the first and last gaps in string like:- '  string  '
print(string.replace('Hello', 'Helloww')) # as word says this replace the given word with given word
print(string) # this is show that this print command dont do anything to original string
print(string.upper()) # this function transform the every alphabet into uppercase 
print(string.lower()) # this function do the opposite of upper function
print(string.split(",")) # this function split the string from the comma in the string
print(string)

# if you want to see the result you have to run these commands

# concatination in python is differnt from JavaScript

strFirst = 'Hello'
strSecond = 'World!'
concat = strFirst + strSecond
print(concat) # in this method the two string just joined together without any space between the words
concatt = strFirst + " " + strSecond
print(concatt) # in this we added the spaces by the space given in the double qoute in between the formula

# we can't concatinate the integer wit string by + sign
# we have to use the formatting method like given below 

age = 18 
txtx = 'my name is mayank and my age is ' + age
print(txtx) # the error was shown and the command was rejected 
txt = f'my name is mayank and my age is {age}'
print(txt)


# now whats coming is called placeholder not in input text but in string or we can say that formatted string  

price = 59
order = f"you order price is {price} rupees"
orderr = f"you order price is {price:.2f} rupees"

print(order) # this is standard looking, normal, looking, not good looking and adopted
print(orderr) # in this function you can see the decimal price.00

# we can also do maths in the brakets as you want
maths = f"your order price is {10 * price:.2f} rupees"
print(maths) # we can say that 10 means 10 same products

# escape character are useless mostly but some are usefull like:-
n = "Hello\nWorld!"
t = "Hello\tWorld"
print(n)
print(t)

# this is the list and the motive to print the sec, third, fourth, fifth items in this list 
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


list = ['banana', 'apple', 'mango'] # list have block brackets for itself.
tuple = ('banana', 'apple', 'mango') # tuples have parenthesis for itself.
set = {'banana', 'apple', 'mango'} # set have curly brackets for itself.
print(list)
print(tuple)
print(set)

# now this is the time dictionary as same as objects in JavaScript 

dict = {
    'name': 'mayank',
    'age': 17,
    'profession': 'web devloper',
    'learning': 'JavaScript , Python'
}
print(dict)

print(dict)
print(len(dict))
print(dict.get('name'))

# these noth method are great for accessing the items in the dict
# and we can give the value to another variable like in this case
x = dict['name']
y = dict.get('age')
print(x)
print(y)

# we can also access to only keys of the dict 
# like in this case 
print(dict.keys())

# and values to 
# like in this case
print(dict.values())

# to change the values of dictionary 
dict['age'] = 18
print(dict['age']) 
print(dict)

# this is to showcase the items in the dictionary
print(dict.items())

# we can also use the if methods in the dict like in this case

if "'name':'mayank'" in dict:
    print('yes the mayank is the name of the student')
else:
    print('this named student is not in our list')

# this is the method to update the key in the dictionary 
dict.update({'age':20})
print(dict)

# this is the way to add the new key int  the dictionary
print(len(dict))
dict['goal'] ='rich'
print(dict)


dict.pop('learning')
print(dict)

# to poping out the last element we can do the popitem() function use 

dict.popitem()
print(dict)

dict['goal'] = 'rich'
dict['learning'] = 'JavaScript , Python'
print(dict)
print(dict.items())



# this is like the loop not like the loop but this is the loop 
# in this the loop prints the key and value simulateneusly 

# this prints the key of dictionary
for x in dict:
  print(x)
  
for xy in dict.keys():
    print(xy)

  
# this prints down the values of keys in the dictionary
for y in dict:
  print(dict[y])
  
for z in dict.values():
    print(z)
  
# to print the keys and the values together we have to do this

for xyz, zyx in dict.items():
    print(xyz , zyx)
    
# if we just wanna copy the whole dictionary we can do this 

newDict = dict

print(newDict)
print(newDict == dict)
  
nestedDict = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(nestedDict)

# we can make the big dictionary by adding three sub dictionary like in this case

big1 = {
    'name': 'mayank',
    'age': 17
}
big2 = {
    'name': 'macky',
    'age': 18 
}
big3 = {
    'name':'mack', 
    'age': 19
}    

print(big1)
print(big2)
print(big3)

bigOne = {
    'bigOne1':big1,
    'bigTwo2':big2,
    'bigThir3':big3
}

print(bigOne)
print(bigOne.keys())
print(bigOne.values())
print(bigOne.items())

# rock paper scissors game is here in python version so be happy 

import random
chances = random.randrange(1, 9)
move = 'scissors'

if chances > 0 and chances < 4 :
    computerMove = "rock"
elif chances > 3 and chances < 7 :
    computerMove = 'paper'
elif chances > 6 and chances < 10 : 
    computerMove = 'scissors'

print(f'Your move is {move}')
print(f'Computer Move is {computerMove}')
    
if move == 'rock' : 
    if computerMove == 'rock':
        print('Tie!')
    elif computerMove == 'paper' :
        print('You Loose!')
    elif computerMove == 'scissors' :
        print('You win!')
elif move == 'paper' :
    if computerMove == 'rock':
        print('You win!')
    elif computerMove == 'paper' :
        print('Tie!')
    elif computerMove == 'scissors' :
        print('You loose!')
elif move == 'scissors' :
    if computerMove == 'rock':
        print('You loose!')
    elif computerMove == 'paper' :
        print('You win!')
    elif computerMove == 'scissors' :
        print('Tie!')

# now its time for faulty calcultor
# this is the faulty calculator which performs the correct calculation only 25 times in 100 tries 
import random
firstNumber = int(input('you first nuber please:'))
secondNumber = int(input('your second number please:'))
opretor = input('please enter your oprend sir:')
chance = random.randrange(1,4)

if opretor == '+' :
    if chance == 1 :
        print(f'your answer is: {firstNumber + secondNumber} ')
    elif chance == 2 :
        print(f'your answer is: {firstNumber - secondNumber}')
    elif chance == 3 :
        print(f'your answer is: {firstNumber * secondNumber}')
    elif chance == 4 : 
        print(f'your answer is: {firstNumber / secondNumber}')
elif opretor == '-' :
    if chance == 1 :
        print(f'your answer is: {firstNumber + secondNumber}')
    elif chance == 2 :
        print(f'your answer is: {firstNumber - secondNumber}' )
    elif chance == 3 :
        print(f'your answer is: {firstNumber * secondNumber}')
    elif chance == 4 : 
        print(f'your answer is: {firstNumber / secondNumber}')
elif opretor == '*' :
    if chance == 1 :
        print(f'your answer is: {firstNumber + secondNumber}')
    elif chance == 2 :
        print(f'your answer is: {firstNumber - secondNumber}' )
    elif chance == 3 :
        print(f'your answer is: {firstNumber * secondNumber}')
    elif chance == 4 : 
        print(f'your answer is: {firstNumber / secondNumber}')
elif opretor == '/' :
    if chance == 1 :
        print(f'your answer is: {firstNumber + secondNumber}')
    elif chance == 2 :
        print(f'your answer is: {firstNumber - secondNumber}' )
    elif chance == 3 :
        print(f'your answer is: {firstNumber * secondNumber}')
    elif chance == 4 : 
        print(f'your answer is: {firstNumber / secondNumber}')
        
        
# now what happens in the faulty calculator 
# first we give the computer a move which he plays on and the if esle helps computer to configure 
# whose the winner is and what move computer and player choose 



























































