'''
Programming Challenge Description: 
Write 4 functions based on the following requirements
Write a function that accepts an integer and returns True if the input is between 4 and 10, inclusive; otherwise, return False
Write a function to test if a list contains any items. Return 'EMPTY' if it does not contain any items and 'NOT EMPTY' if it does.
Write a function that accepts a file name and a string and writes the string to the file with the given file name.
Write a function that accepts a list and doubles each value in the list. When no input parameter is provided, return an empty list.
Input: 
N/A
Output: 
N/A
'''

def func1(val):
    '''
    Write a function that accepts an integer and returns True if the input is between 4 and 10, inclusive; otherwise, return False

    '''
    return True if ( (val >= 4) and (val <= 10) ) else False


def func2(a_list, items):
    '''
    Write a function to test if a list contains any items. Return 'EMPTY' if it does not contain any items and 'NOT EMPTY' if it does.
    '''
    has_items = False
    for item in items:
        has_items = item in list(a_list)
        if (has_items):
            break
    return 'EMPTY' if (not has_items) else 'NOT EMPTY'


def func3(fname, a_str):
    '''
    Write a function that accepts a file name and a string and writes the string to the file with the given file name.

    '''
    fOut = open(fname, 'w')
    print >> fOut, a_str
    fOut.flush()
    fOut.close()


if (__name__ == '__main__'):
    print func1(3)
    print func1(4)
    print func1(10)
    print func1(11)
    print
    
    print func2([1,2,3,4,5], [2,3])
    print func2([1,2,3,4,5], [6,7])
    print
    
    