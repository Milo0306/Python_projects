fname = input ("Enter file name: ")
try:
    fhand = open (fname)
except:
    print ("There is no such file in thar directory", fname)
    quit ()
count = 0
for line in fhand:
    if line.startswith("Subject:") :
        count = count + 1
print ("there were", count, "subject lines in",  fname)