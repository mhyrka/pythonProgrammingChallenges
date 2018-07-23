"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""

# def multiples_of_seven_not_five():
#    numbers = []
#    for num in range(2000, 3200):
#        if num % 7 == 0 and num % 5 != 0:
#            numbers.append(num)
#    print(numbers)

#multiples_of_seven_not_five()
"""
def factorial(x):
    fact = 1
    for num in range(1, x+1):
        fact = fact * num

    print(fact)

number = (raw_input("Factorial number: "))

factorial(int(number))
"""
"""
def make_dictionary(number):
    new_dictionary = dict()

    for num in range(1, number + 1):
        new_dictionary[num] = num * num

    print(new_dictionary)

make_dictionary(8)
"""
"""
numbers = "34,67,55,33,12,98"

def return_list_and_tuple(x):
    print(tuple(x.split(',')))
    print(list(x.split(',')))


return_list_and_tuple(numbers)
"""
"""
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input("What String: ")

    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()
"""

"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value
(for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
import math
"""
D = [raw_input("Value of D: ")]

c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)
"""

"""
Write a program that accepts a comma separated sequence of words as input and prints the words in a
comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""
"""
letters = raw_input("Words: ")
words = letters.split(',')
print(sorted(words))
"""

# items=[x for x in raw_input().split(',')] <-- SUPER USEFUL PATTERN FOR SEPARATING COMMA SEPARTED INPUT

"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters
in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
lines = []

while True:
    line = raw_input("Sentences: ")
    if line:
        lines.append(line)
    else:
        break

for word in lines:
    print(word.upper())
"""

"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words
after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
"""
"""
items=[x for x in raw_input("Words: ").split(' ')]
print(" ".join(sorted(set(items))))
"""

"""
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
items=[int(x, 2) for x in raw_input().split(',')]

for num in items:
    if num % 5 == 0:
        print(bin(num)[2:])
"""
"""
import random

class dice(object):
    def __init__(self):
        self.dice_one = 1
        self.dice_two = 1

    def roll_dice(self):
        self.dice_one = random.randint(1, 6)
        self.dice_two = random.randint(1, 6)
        print(self.dice_one)
        print(self.dice_two)


player = dice()

player.roll_dice()

"""

"""

create class int_bag
add int to int_bag
remove int from int_bag
get random number from int bag

"""





class int_bag(object):
    def __init__(self):
        self.bag = dict()
        self.index = 0

    def add_int(self, number): # <- constant
        self.index += 1
        self.bag[self.index] = number
        #print(self.bag)


    def remove_int(self, number): # <- len(list)
        print(self.bag)


    def get_random(): # <- len(list) // probably constant -- look into
        return self.bag[random.randint(0, len(self.bag))]

my_bag = int_bag()
my_bag.add_int(5)
my_bag.add_int(5)
my_bag.add_int(5)
my_bag.add_int(10)
my_bag.add_int(10)
my_bag.remove_int(5)
#my_bag.get_random()
