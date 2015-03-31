# Use the file name mbox-short.txt as the file name
fname = ("/home/goldfinger59/Desktop/mbox-short.txt")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count+1    
    line = float(line[20:])
    total = total+line
#print total/count
print "Average spam confidence: ",total/count
