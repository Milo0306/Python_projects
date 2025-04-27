fhand = open ("C:/Users/milos/Desktop/IT stuff/Python_projects/mbox.txt")
count = 0
for line in fhand:
    count = count + 1
print("Line Count: ", count)

#this shows how many characters are in a file

fhand = open ("C:/Users/milos/Desktop/IT stuff/Python_projects/mbox.txt")
inp = fhand.read ()
print (len(inp))

# this count signs

print (inp[:20])

# this works as a serach engine (until "from" is found)

fhand = open ("C:/Users/milos/Desktop/IT stuff/Python_projects/mbox.txt")
for line in fhand:
    if line.startswith("From:") :
        print (line)

# rstip() can throw out unwanted double white spaces


fhand = open ("C:/Users/milos/Desktop/IT stuff/Python_projects/mbox.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith ("From:"):
        continue
    print (line)



