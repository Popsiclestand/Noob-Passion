#a program to convert integers into 8-bit binary

#user enters value
number_to_convert_string = raw_input('Enter a number that does not excede 8 bits:')
number_to_convert_print = int(number_to_convert_string)
try:
    number_to_convert = int(number_to_convert_string)
except:
    print 'Please enter a valid integer'
    exit()

if number_to_convert >= 256:
    print 'Data Overflow Error. Integer exceeds 8 bits.'
    exit()

if number_to_convert > 128 and number_to_convert < 256:
    eight_bit_binary = 1
    number_to_convert = number_to_convert-128
elif number_to_convert == 128:
	eight_bit_binary = 1
	number_to_convert = 0
else:
    eight_bit_binary = 0

#print eight_bit_binary

if number_to_convert > 64 and number_to_convert < 128:
    seven_bit_binary = 1
    number_to_convert = number_to_convert - 64
elif number_to_convert == 64:
	seven_bit_binary = 1
	number_to_convert = 0   
else:
    seven_bit_binary = 0

#print seven_bit_binary

if number_to_convert >32 and number_to_convert <64:
    six_bit_binary = 1
    number_to_convert = number_to_convert - 32
elif number_to_convert == 32:
	six_bit_binary = 1
	number_to_convert = 0    
else:
    six_bit_binary = 0

#print six_bit_binary

if number_to_convert > 16 and number_to_convert < 32:
    five_bit_binary = 1
    number_to_convert = number_to_convert - 16
elif number_to_convert == 16:
	five_bit_binary = 1
	number_to_convert = 0
else:
    five_bit_binary = 0

#print five_bit_binary

if number_to_convert > 8 and number_to_convert < 16:
    four_bit_binary = 1
    number_to_convert = number_to_convert - 8
elif number_to_convert == 8:
	four_bit_binary = 1
	number_to_convert = 0   
else:
    four_bit_binary = 0
    number_to_convert = number_to_convert

#print four_bit_binary

if number_to_convert > 4 and number_to_convert < 8:
    three_bit_binary = 1
    number_to_convert = number_to_convert - 4
elif number_to_convert == 4:
	three_bit_binary = 1
	number_to_convert = 0   
else:
	three_bit_binary = 0
	number_to_convert = number_to_convert   

#print three_bit_binary

if number_to_convert > 2 and number_to_convert < 4:
    two_bit_binary = 1
    number_to_convert = number_to_convert - 2
elif number_to_convert == 2:
	two_bit_binary = 1
	number_to_convert = 0    
else:
    two_bit_binary = 0

#print two_bit_binary

if number_to_convert == 1:
	one_bit_binary = 1
	number_to_convert = 0
elif number_to_convert <1:
	one_bit_binary = 0
	number_to_convert = number_to_convert   
    
if number_to_convert_print < 16:
    print number_to_convert_string, '=', four_bit_binary,three_bit_binary,two_bit_binary,one_bit_binary
else:
    print number_to_convert_string, '=',eight_bit_binary,seven_bit_binary,six_bit_binary,five_bit_binary,four_bit_binary,three_bit_binary,two_bit_binary,one_bit_binary