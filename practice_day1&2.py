import math
Black_men = 1000
print(Black_men)
black_rating = 7.88  # thid is a float
does_black_matter = True  # this is a boolean
message = "Holy goly goob"  # this is a string


print(len(message))  # lenght of string
print(message[1])  # letter pf the string (0,1,2,3,4,5....)
# print from 0 to end or the letters indicated in the number
print(message[0:4])
test = "MAMAMIA \"HOLY GOLY\" "  # \ to add a variable inside a string
test2 = "GAGI \nPre"  # \n to make a new line
print(test2)
print(test)


first = "Mark"
second = "Angelo"
full = first + " " + second  # full is  like  cout or so
print(full)

middle = "Clemente"
last = "Panis"
full1 = f"{middle} {last}"  # f is for format and put variables inside {}
full1 = f"{len(middle)} {len(last)}"
print(full1)

gloob = " i love you"
print(gloob.upper())  # for uppercase values
print(gloob.lower())  # for lowercase value
print(gloob.title())  # Capitalize first letter of each word
print(gloob.strip())  # removes space at the start and end by lstrip or rstrip
print(gloob.replace("i", "you"))  # replace the value withthe given value
print(gloob.find("love"))  # find the index of the value
# indicates  wether the value is in the string by true or false
print("love" in gloob)
# indicates wether the value is not in the string by true or false
print("love" not in gloob)

# types of numbers
x = 5
x = 5.5
x = 4 + 5j  # a + bi or b(x) is considered (j) in python

# python math module (explore)
print(round(89.7))  # round off the number
print(abs(-90))  # absolute value
print(math.ceil(89.1))  # rounds up the number
print(math.floor(89.9))  # rounds down the number

# ----------------------------------------------
# int(x)
# float(x)
# bool(x)
# str(x)


# int(input)) to put a variable and to type a variable to the code
x = int(input("Enter your age: "))
if x >= 18:
    print("Your'e an  adult")
elif x == 17:
    # elif for mutiple statements and if both else and if are not true
    print("Youre almost an qdult")
else:
    print("Youre a minor")


# """ is for a long string"
message = """ 
hello jnffk kjfnkwenb
"""
print(message)


x = input("enter a number: ")
y = int(x) + 2
print(f"the first: {x}, the second: {y}")

# ----------------------------------------------

high_income = True
low_income = False
student = True
# (and) is for both conditions to be true. (or) is for either one condition to be true
# (not) is for the oppositeof the condition if  statement is true it becomes false vice versa

if high_income or low_income and not student:  # short  circuit
    print("Youre rich")
else:
    print("Youre poor")

# ----------------------------------------------

age = int(input("Enter your age: "))
if age >= 18 and age < 65:
    print("Youre an adult")
else:
    print("Youre a kid")
# ----------------------------------------------

for number in range(10):  # range(for) is for start of loop (in) is for the variable in range()
    print("I love you", number + 1)
