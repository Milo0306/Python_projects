greet = "    Siema   Miłosz     "
print (greet.lstrip())
print (greet.rstrip())
print (greet.strip ())
print (greet.replace (" ", ""))


text = "X-DSPAM-Confidence:    0.8475"
pos = text.find (":")
slice = text[pos + 1:].strip()
value = float(slice)
print (slice)


text = "X-DSPAM-Confidence:    0.8475"
pos = text.find (":")
print (pos)
