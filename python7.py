word ="hello"

print(word[::-1])

if word == word[::-1]:
    print (True)
else:
    print (False)

#second option
word = "read"
if word[0] == word[-1]:
    print("true")
else:
    print("false")