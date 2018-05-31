def new_string(s1, s2):
    val = ''.join(set(s1+s2))
    return val

print new_string('abbcd', 'effgh')
