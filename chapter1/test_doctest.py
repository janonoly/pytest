'''
** 作者：janono QQ交流群：882873912**
'''
def multiply(a, b):
    """
    function:两个数相乘
    >>> multiply(4,3)
    12
    >>> multiply('a', 4)
    'aaa'
    """
    return a*b

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

