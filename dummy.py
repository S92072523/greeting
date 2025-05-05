words = "Hello, Every , One"

"""#Convert as a list
lists = [word.strip() for word in words.split(",")]

print(lists)"""

#Convert as a Dictionary
dect = {}

key = 1
for word in words.split(","):
    dect[key] = word.strip()
    key += 1

print(dect)