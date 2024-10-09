list1 = [0,1,2,3,4,5,6,7,8,9,10,11]

list1.reverse()

print(list1)

#after some fiddling turns out this fn is 'in place'
#so you can only reverse it and THEN print it out

print(list1[:-2])

#- starts counting from 1?

#tripling quote '''hello''' allows sgtring to span more than one line
#also """hello"""

string = '''hello
how are you'''

print(string.capitalize())

string_german = 'counteß'

print(string_german.casefold())

#more lowercaser lowercasing function that converts other language stuff?

print(string.encode())

#cool? dont really understand this or think ill be using this

#more string stuff to do with websites or padding etc on
#https://docs.python.org/3/library/stdtypes.html#string-methods

#lots of is identifying things
#isalpha (numeric)
#isascii
#isdecimal
#isdigit ?
#isidentifier?
#islower (pretty useful thisone)
#isnumeric
#isprintable
#isspace (checks if at least one characgter + spaces (all types))
#istitle(bit confusing?)
#isupper (again useful one)

#much mroe string manipulation stuff, gonna move on to booklet agin for now

tel = {'pops':441111111111,'ali':442222222222}

print(tel['ali'])

#dictionaries, assigning keys to values, very cool
#tel.keys gives keys, tel.values gives vals ()

#TYPING , IMPORTANT

#Tuplations
#immutable lists, cant change their content once created

#2 ways of writing it

tup1 = 'hello',5,'this is a tuple'
tup2 = ('this is also a tuple', 2)

#sets, unordered unique items

s = set(('a','b','c','d'))
print(s.difference(('a','b'))) #idk whats happening here

#further stuff
#https://www.informit.com/articles/article.aspx?p=453682

#looping (control flow)

for i in range(4):
    print(i)

#usaul stuff, stops 1 before number in range (sincve it counts from 0)

for word in('hi','pullup','wembley'):
    print('ur not him %s'%word)

#% is for maths no? need to research this later

z = 1 + 1j
while abs(z) < 100:
    z = z**2 + 1
print(z)

#some mandelbrot thing supposedly, pretty neat, i think complex
#numbers will be real useful later on

#otherwise can type 'continue' or 'break'

for i in range(2):
    if i==0:
        print("hello")
        continue

for i in range(2):
    if i==0:
        print("hello one time")
        break


#

