abc = "with three words"
stuff = abc.split()
print(stuff)

print(len(stuff))

print(stuff[1])

for w in stuff :
    print(w)



fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
