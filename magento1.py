an_array = [0,1,2,3,4,5,-5,-100000,100000,-200000]

def my_max(a,b):
    return a if (a > b) else b

def get_max(a):
    val = -1
    for i in a:
        val = my_max(i, val)
    return val

def get_max2(a):
    val = -1
    for i in a:
        val = max(i, val)
    return val


if (__name__ == '__main__'):
    print get_max(an_array)
    print get_max2(an_array)
