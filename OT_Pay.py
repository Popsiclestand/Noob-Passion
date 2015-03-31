#function that multiplies two variables
def computepay(x,y):
    multiplied = x * y
    return multiplied

#function that converts any variable into currency
def convertdollars(x):
    converted = "$" + format(x, ',.2f')
    return converted

#user enters hours worked and payrate as string
hrs = raw_input("Enter hours worked: ")
rate = raw_input("Enter pay rate: ")

#try to convert the strings to float, error message if invalid
try:
    hrs = float(hrs)
except:
    print "Please enter a numerical value for hours worked"
    print "Invalid hours"
try:
    rate = float(rate)
except: 
    print "Please enter a numerical value for pay rate"
    print "Invalid Rate"

#compute and print pay
else:
    othours = hrs-40 #calculate OT hours
    otrate = rate*1.5 #calculate OT payrate
    if hrs > 40:
        hrs = 40
        regularpay = computepay(hrs,rate)
        otpay = computepay(othours,otrate)
        print convertdollars(regularpay) + " in Standard Pay"
        print convertdollars(otpay) + " in Overtime Pay"
        print convertdollars(regularpay+otpay) + " Total Pay"
    else:
         regularpay = computepay(hrs,rate)
         print convertdollars(regularpay) + " in Standard Pay"
       
    