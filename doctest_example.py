import doctest

def factorial(number):
    '''
    This function calculates the factorial of an integer, n:
    n * (n-1) * ... * 2 * 1
    
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(4)
    24
    >>> factorial(5)
    120
    '''
    assert isinstance(number,int) and number>= 0
    
    if number == 0 or number == 1:
        return 1
    else:
        results = 1
        while number>0:
         results *= number
         number -= 1
    return results
    
if __name__=='__main__':
    doctest.testmod()
