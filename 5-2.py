# -*- coding: utf-8 -*-
maximum = None
minimum = None


while True:
    enter = raw_input('Enter number:') #user input value
    if enter == 'done':
        break #skip to print statements
    #check for valid input, give error if empty or letters
    try:        
        number = int(enter) #convert input to integer
        if maximum is None or number > maximum:
            maximum = number
        if minimum is None or number < minimum:
            minimum = number
    except:
        print 'invalid input'

print 'Max:', maximum
print 'Min:', minimum
