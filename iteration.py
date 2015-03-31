# -*- coding: utf-8 -*-
#function to computer average of two numbers
def computeaverage(total,count):
    divided = total/count
    return divided

#init variables
count = 0
total = 0


while True:
    enter = raw_input('Enter number:') #user input value
    if enter == 'done':
        break #skip to print statements
    #check for valid input, give error if empty or letters
    try:        
        number = int(enter) #convert input to integer
        total = total + number #add entered numbers together
        count = count +1 #count numbers as they are entered
    except:
        print 'invalid input'

if count > 0:    #catch division by 0 error
    print 'Count:', count
    print 'Total:', total
    print 'Average:', computeaverage(total,count)
else:    
    print '0 numbers entered'