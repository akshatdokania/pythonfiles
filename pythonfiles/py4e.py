fname = input("Enter file name: ")
fh = open(fname)
count = 0
s1 = 0.00
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
         continue
    count = count + 1
    pos = line.find(' ')
    a = float(line[pos + 1:])
    s1 = s1 + a

avg = s1 / count
print("Average spam confidence:  ",avg)
