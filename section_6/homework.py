# Problem 1
def vol(rad):
    '''
    Write a function that computes the volume of a sphere given its radius.
    '''
    pass

vol(2)

'''
output:
33.493333333
'''

# Problem 2
def ran_check(num,low,high):
    pass

ran_check(5, 2, 7)

'''
output:
5 is in the range between 2 and 7
'''

# Boolean
def ran_bool(num,low,high):
    '''
    Write a function that checks whether a number is in a given range (inclusive of high and low)
    '''
    pass

ran_bool(3,1,10) # True

'''
output: 
True
'''

# Problem 3
def up_low(s):
    '''
    Write a Python function that accepts astring and calculates the
    number of upper case letters and lower case letters.
    '''
    pass

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

'''
output:
Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
No. of Upper case characters :  4
No. of Lower case Characters :  33
'''

# Problem 4
def unique_list(lst):
    '''
    Write a Python function that takes a list and returns a new list
    with unique elements of the first list.
    '''
    pass

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

'''
output:
[1, 2, 3, 4, 5]
'''

# Problem 5
def multiply(numbers):
    '''
    Write a Python function to multiply all the numbers in a list.
    ''' 
    pass

multiply([1,2,3,-4])

'''
output:
-24
'''

# Problem 6
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def palindrome(s):
    '''
    Write a Python function that checks whether a passed in string is palindrome or not.
    '''
    pass

palindrome('helleh')

'''
output:
True
'''
# Problem 7
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    '''
    Write a Python function to check whether a string is pangram or not.
    '''
    pass

ispangram("The quick brown fox jumps over the lazy dog")

'''
output:
True
'''