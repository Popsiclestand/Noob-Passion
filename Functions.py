def reverse_me(name):
    temp = name.split()
    first, last = temp[0], temp[1]
    return 'Hello, ' + first + ' ' + last
name = raw_input('Enter Name:')
print reverse_me(name)