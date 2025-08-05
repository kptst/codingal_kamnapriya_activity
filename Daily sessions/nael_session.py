# string= input("Please enter your own words: ")
# char=input("Please enter your own words: ")
# i=0
# count=0
# while(i<len(string)):
#     if(string[i]==char):
#         count=count+1
#     i=i+1
    
    
# print("The total no. of time", char, "has occured= " , count)

#PATTERNS
# ACTIVITY-1

# print("Half pyramid patterns of (*): ")
# num= int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# INTRODUCTION TO TURTULE

# import turtle
# turtle.Screen().bgcolor("red")
# turtle.Screen().setup(300,400)
# polygon = turtle.Turtle()

# num_slides =6
# side_length =70
# angle =360.0/num_slides
# for i in range(num_slides):
#     polygon.forward(side_length)
#     polygon.right(angle)
    
# turtle.done()

# SPIRAL PATTERNS

# import turtle
# my_wn=turtle.Screen()
# my_wn.bgcolor("blue")
# my_wn.title("Turtle")
# my_pen= turtle.Turtle()
# size=0
# while True:
#     for i in range(4):
#         my_pen.fd(size+1)
#         my_pen.lef(90)
#         size=size-5
#     size = size+1

# --------FUNCTION-------------------

def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  return x/y

print("Please select any one option from below")
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")

choice= input("Please enter your choice: ")

num1= int(input("Please enter the first number: "))
num2= int(input("Please enter the second number: "))

if choice == 'A':
  print(num1, "+", num2, "=", add(num1, num2))
elif choice == 'B':
  print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == 'C':
  print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == 'D':
  print(num1, "/", num2, "=", divide(num1, num2))
else:
  print("Invalid Input")

# ARGUMENT, FUNTION TYPE, RECURSION, DOCSTRING

# ACTIVITY 1
 def total_calc(bill_amount,tip_perc):
   total=bill_amount*(1+0.01*tip_perc)
   total=round(total,2)
   print(f"Please pay the bill {total}")
   
total_calc(150,20)

# KEYWORDS

a= input("enter words:-")
for i in a:
  if(i=='A')
    print("A is found")
    break
  else:
    print("A is not found")
    
    var=10
    while var>0:
      var=var-1
      if var==5:
        comtinue
        
      print("variable value", var)

# EXCEPTIONAL HANDLING
# ACTIVITY 1

try:
  num=int(input("Enter a number"))
  print("the entered number is", num)
except ValueError as ex:
  print("Exception", ex) 
  
# ACTIVITY 2

try:
  num1, num2= eval(input("Enter two number, seperated by comma: "))
  result=num1/num2
  print("Result is", result)
except SyntaxError:
  print("comma is missing")
except ZeroDivisionError:
  print("Division by Zero is error")
except:
  print("Wrong input")
else:
  print("No Exception")
  
finally:
  print("this will execute no matter what you done")

  
  # ACTIVITY 3
valid=False
while not valid:
    try:
        n=int(input("Enter a  even number"))
        while n%2==0:
            print("Bye")
            valid=True
    except ValueError:
        print("Invalid input")