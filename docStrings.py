"""
docstrings: 
           If string with triple quote is placed immediately after function or class or top of module,
           then they turn into docstrings
"""

def addNumbers():
    '''
    this function adds numbers 10 and 20
    '''
    number1 = 10
    number2 = 20
    result = number1 + number2
    print(result)

print(addNumbers.__doc__)    
addNumbers()    
