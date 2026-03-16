'''
MODULES IN PYTHON
Modules are reusable pieces of code that can be imported and used in other Python programs. 
They help organize code and promote code reusability. 
Python has a rich standard library of modules, and you can also create your own custom modules.

1- MATH MODULE
The math module provides various mathematical functions and constants.
To use the math module, you need to import it first:    
import math
Here are some commonly used functions and constants in the math module:
- math.sqrt(x): Returns the square root of x.
- math.pow(x, y): Returns x raised to the power of y.
- math.sin(x): Returns the sine of x (x is in radians).
- math.cos(x): Returns the cosine of x (x is in radians).
- math.tan(x): Returns the tangent of x (x is in radians).
- math.pi: A constant representing the value of π (approximately 3.14159).
- math.e: A constant representing the value of e (approximately 2.71828).
- math.factorial(n): Returns the factorial of n (n must be a non-negative integer).


2- RANDOM MODULE
The random module provides functions for generating random numbers and performing random operations.
To use the random module, you need to import it first:
import random
Here are some commonly used functions in the random module:
- random.random(): Returns a random float between 0.0 and 1.0.
- random.randint(a, b): Returns a random integer N such that a <= N <= b.
- random.choice(seq): Returns a random element from the non-empty sequence seq.
- random.shuffle(seq): Shuffles the sequence seq in place.
- random.sample(population, k): Returns a list of k unique elements chosen from the population sequence.
- random.seed(a): Initializes the random number generator with
a seed value a. This can be used to produce reproducible random numbers.
- random.uniform(a, b): Returns a random float N such that a <= N <= b.
- random.randrange(start, stop[, step]): Returns a randomly selected element from the range created by start, stop, and step.


3-KEYSWORD MODULE
The keyword module provides a list of reserved keywords in Python.
To use the keyword module, you need to import it first:
import keyword
Here are some commonly used functions in the keyword module:
- keyword.iskeyword(s): Returns True if s is a reserved keyword in Python, otherwise returns False.
- keyword.kwlist: A list of all reserved keywords in Python.
- keyword.__doc__: A string containing the documentation for the keyword module.


4-CONSTANTS MODULE
The constants module provides a collection of mathematical and physical constants.
To use the constants module, you need to import it first:
import constants
Here are some commonly used constants in the constants module:
- constants.pi: A constant representing the value of π (approximately 3.14159).
- constants.e: A constant representing the value of e (approximately 2.71828).
- constants.c: The speed of light in vacuum (approximately 299,792,458 meters per second).
- constants.g: The acceleration due to gravity on Earth (approximately 9.80665 meters per second squared).
- constants.h: Planck's constant (approximately 6.62607015 × 10^-34 joule seconds).
- constants.k: Boltzmann's constant (approximately 1.380649 × 10^-23 joule per kelvin).
- constants.N_A: Avogadro's number (approximately 6.02214076 × 10^23 mol^-1).
'''



'''MATH MODULE
The math module provides various mathematical functions and constants.'''
import math
#  math.   show all the functions and constants in math module
print(math.floor(3.7)) # it return the largest integer less than or equal to 3.7

import keyword
print(keyword.kwlist)  

import random
print(random.random())  # it return random number between 0.0 and 1.0
print(random.randint(1, 100))  # it return random integer between 1 and 100


import datetime
print(datetime.datetime.now())  # it return current date and time



help('modules') # to know about modules in python