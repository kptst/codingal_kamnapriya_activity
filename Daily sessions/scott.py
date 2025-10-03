number=int(input("ENTER ANY NUMBER: "))
if number%2==0:
    print("this is even number")
else:
    print("this is odd number")
    
    
# ACTIVITY-2-BMI CLC
height=19.5
weight=26
BMI = weight/(height/100)**2
print("the BMI IS :")
if BMI<=18.5:
    print("under weight")
elif BMI<=24.9:
    print("normal weight")
elif BMI<=29.9:
    print("over weight")
else:
    print("obesity")
    
# Activity-3
num=int(input("Enter number to check:"))

if num>50:
    print("number is greater")
    if num%2==0:
        print("num is even")
    else:
        print("num is odd")
else:
    print("number is less then 50")
    
# Activity-4

import datetime

current_time = datetime.datetime.now().time()
print("Current Time is: ", current_time)


# ACT-TABLE OF 23
for i in range(1, 11):
  print(f"23 X {i} = {23 * i}")

# ACT-STAR PATTERN
n= int(input("Enter the number of rows: "))
for i in range (1 , n+1):
  for j in range(i):
    print("*", end=" ")
  print()

# ACT-NATURAL NUM SUM
total_sum=sum(range(1,10))
print("Sum of natural numbers from 1 to 10 is:", total_sum)

# ACT-PRIME NUM
num= int(input("Enter a number: "))
if num>1:
  for i in range(2, int(num/2)+1):
    if(num%i)==0:
      print(num, "is not a prime number")
      break

  else:
    print(num, "is a prime number")
else:
  print(num, "is not a prime number")

# FUNCTION- ACTIVITY-1

def intro(name):
  print("Hello, I am ", name)
user_name=input("Enter your name")
intro(user_name)
# ACTIVITY-2
def recr_fact(n):
  if n==1:
    return n
  else:
    return n*recr_fact(n-1)

num = int(input("Enter a number : "))
if num<0:
  print("Sorry, factorial does not exist for negative numbers")
elif num==0:
  print("The factorial of 0 is 1")
else:
  print("The factorial of",num,"is",recr_fact(num))


# ACTIVITY-3
def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  return x/y

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))

print("sum : ",add(num1,num2))
print("difference : ",subtract(num1,num2))
print("product : ",multiply(num1,num2))
print("quotient : ", divide(num1,num2))
