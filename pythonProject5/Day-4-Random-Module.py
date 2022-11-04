import random
# Python random Module Methods
# 1. seed()
#This initializes a random number generator. To generate a new random sequence, a seed must be set depending on the current system time. random.seed() sets the seed for random number generation.
#
#2. getstate()
# This returns an object containing the current state of the generator. To restore the state, pass the object to setstate().
#
#3. setstate(state_obj)
#This restores the state of the generator at the point when getstate() was called, by passing the state object.
#
#4. getrandbits(k)
#
# This returns a Python integer with k random bits. This is useful for methods like randrange() to handle arbitrary large ranges for random number generation.

random.seed(1)

#Get the state of the generator
state = random.getstate()
print('Generating a random squence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))

#Restore the state to a point before the sequence was generated
random.setstate(state)
print('Generating the same identical sequence of 3 integers...')
for i in range(4):
    print(random.randint(1, 1000))

# Generate Random Integers
#
# The random module provides some special methods for generating random integers.
# 1. randrange(start, stop, step)
#
# Returns a randomly selected integer from range(start, stop, step). This raises a ValueError if start > stop.
# 2. randint(a, b)
#
# Returns a random integer between a and b (both inclusive). This also raises a ValueError if a > b.
#
# Here is an example that illustrates both the above functions.

i = 100
j = 20e7

#Generates a random number between i and j
a = random.randrand(i, j)
try:
    b = random.randrange(j, i)
except: ValueError:
    print('ValueError on randrange() since start > stop')