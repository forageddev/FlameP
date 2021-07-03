def format(x):
    if (x == "F"):
        return "Friend"
    if (x == "L"):
        return "Love"
    if (x == "A"):
        return "Affection"
    if (x == "M"):
        return "Marry"
    if (x == "E"):
        return "Enemy"
    return "Error"

print("---------------------------------------------")
print("Flame recreation for Python made by Foraged at 11 pm.")
print("---------------------------------------------")

print("Enter the first name.")
firstName = str(input()).lower()
print("Enter the second name.")
secondName = str(input()).lower()

for c in firstName: 
   if ((c in firstName) & (c in secondName)):
       firstName = firstName.replace(c, "")
       secondName = secondName.replace(c, "")

chars = ["F", "L", "A", "M", "E"]
  
charAmount = len(firstName + secondName)

for z in range(0, 4):
    f = 0;

    for i in range (charAmount - 1):
        f = f + 1
        if f == len(chars):
           f = 0
    chars.pop(f)

print("---------------------------------------------")
print("The result is " + format(chars[0]))
print("---------------------------------------------")