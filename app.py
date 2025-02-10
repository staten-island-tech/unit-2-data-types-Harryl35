""" # Strings represent characters, names, words    
name = "Kammy"
#intergers for WHOLE numbers    
age = 14
#boolean is True or False used for evalutations 
graduated = False
#Floats for decimal 
money = 4.50 """

""" def add(x,y):
    print(round(x + y))
# add(54,"11")
#input seeks user response and outputs that into the variable 
#bill value will be equal to the response of the user
bill = float(input("How much was the bill?"))
print(bill)
add(15,bill) """

""" #Lists which store lists of data
students = ["kammy", "Rachel", "Denis", "Ian"]
#similar for i in range(4)
money = [1,2,3,4,5,6]
#scalable
for students in students:
    print(students) """
""" x = 0
for money in moneys 
    x = x + money
    print(x) """

""" #determine if number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
 """
""" #tip and total calculator
def add(x,y):
    print(round(x + y))
bill= float(input("how much was the bill"))
print(bill)
tip = int(bill * 0.15)
print(round(tip))
print(add(tip,bill)) """

""" sentence = input("Make a sentence")
y = sentence.split()
total = len(y)
print(total) """

""" #madlib project
verb1 = input("verb1")
verb2 = input("verb2")
noun1 = input("noun1")
number1 = input("number1")
famous = input("famous person")

madlib = (f"One day I met {famous}. Then they signed {number1} {noun1} and I was {verb1} and {verb2}.")
print(madlib) """

""" #tip depending on service
bill = float(input("how much was the bill?"))
service = input("how good was the servive?")
if service == "okay":
    tip = bill * 0.15
elif service == "good":
    tip = bill * 0.20
elif service == "great":
    tip = bill * 0.25
else: 
    tip=0
print(f"your tip will be {tip}") """

""" number = int(input("Give me a number"))
factors = []
x = 0
for i in range (1,number):
    x = x + 1
    if number % x == 0:
        factors.append(i)
print(factors) """

number = int(input("Give me a number"))
factors = []
x = 0
for i in range (1,number):
    x = x + 1
    if number % x == 0:
        factors.append(i)
print(factors)
number = int(input("Give me a number"))
factors = []
x = 0
for i in range (1,number):
    x = x + 1
    if number % x == 0:
        factors.append(i)
print(factors)
common_items = set(factors) & set(factors)
if common_items:
    greatest_common = max(common_items)
    print("The greatest common number (GCF) is", greatest_common)
else:
    print("There are no common factors.")


