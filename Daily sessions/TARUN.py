# # Activity-1 (IF-ELSE Condition)
# num=3
# if num>0:
#     print("num is positive", num)

# num=-3
# if num>0:
#     print("num is  not positive", num)
    
    
# # Activity-2 (IF-ELSE Condition)
# actual_amount=100
# sales_amount=120
# if (sales_amount> actual_amount):
#     print("Profit")
# else:
#     print("Loss")

# # Activity-3(IF-ELSE Condition)
# i=10
# if(i<15):
#     print("i is smaller than 15")
# else:
#     print("i is greater than 15")

# # Activity-4(IF-ELSE Condition)

# num=12
# if (num%2)==0:
#     print("num is even")
# else:
#     print("num is odd")
    
    
    
      
# # IF-ELIF-ELSE CONDITION

# # activity-1
# a=10
# b=12
# c=0

# if a and b and c:
#     print("all the number have boolean vaue as TRUE")
# else:
#     print("all the number have boolean vaue as FALSE")
    
    
# x=10
# y=-10
# z=0
# if x>0 or y>0:
#     print("anyone number TRUE")
# else:
#     print("No num is greater")
    
    
#  # activity-2- not operator 
#  a=10
#  b=12
#  c=12
#  print(a!=b)
#  print(b!=c)
 
# if (a==10) != (b==5):
#     print("Executed")
# else:
#     print("not executed")
    
    
# # Activity-3- BMI -CHECKER
# height= float(input("enter your height"))
# weight= float(input("enter your weight"))

# BMI= weight/(height/100)**2
# print("Your BMI is: ", BMI)

# if BMI <=18.4:
#     print("underweight")
# elif BMI <=24.9:
#     print("healthy")
# elif BMI <=34.9:
#     print("overweight")
# else:
#     print("error")


  
# # Activity-1
# x=10

# if (type(x)is int) :
#     print("true") 
# else:
#     print("False")
    
# y=5.0
# if (type(y) is not float):
#     print("true")
# else:
#     print("false")
    
    
# # Activity-2
# a=5
# b=-5
# print("right shift operator for a",a>>1) #right shift operator
# print("right shift operator for b",b>>1)

#  #left shift operator
# print("left shift operator for a",a<<1) #left shift operator
# print("left shift operator for b",b<<1)

# # Activity-3
# print("Enter marks obtained in 3 subject")
# marks1=int(input("Enter marks of the first subject:"))
# marks2=int(input("Enter marks of the second subject:"))
# marks3=int(input("Enter marks of the third subject:"))
# total=marks1+marks2+marks3
# avg=total/3
# if avg>=90 and avg<=100:
#     print("Grade: A")
# elif avg>=80 and avg<90:
#     print("Grade: B")
# elif avg>=70 and avg<80:
#     print("Grade: C")
# elif avg>=60 and avg<70:
#     print("Grade: D")
# else:
#     print("Grade: F")
    
    
# # PYTHON CHALLENGES

# # 1-Activity
# v=4
# w=5
# x=4
# z=2
# z=(v+w)*x/y;
# print("value of (v+w)*x/y : ", z)


# # activity-2
# numerator=10
# denominator=2
# if numerator%denominator==0:
#     print("Number is completely divisible by 2")
# else:
#     print("Number is not completely divisible by 2")
# # Activity-3
# mean1=38
# wrong_num=36
# correct_num=56
# total_number=40
# sum = mean1*total_number
# print("sum of all numbers : ", sum)

# num2=sum-(wrong_num) - (correct_num)
# print("sum of all numbers after correction : ", num2)

# mean2=num2/total_number
# print(mean2)

# # Activity-4
# a=10
# b=20
# c=30

# sum=a+b+c
# print(sum)
# avg=sum/3
# print("  average of three numbers : ", avg)

# # ACTIVITY1-NESTING
# attndnc=int(input("enter the attendance of the student: "))
# if medical_cause == "y":
#     print("You are allowed")
# else:
#     if atten>=75:
#         print("you are allowed")
#     else:
#         print("you are Not allowed")
        
        

# # Activity-2

# unit=int(input("enter the unit: "))

# if (unit<50):
#     amount=unit * 2.60
#     fixed_charge=25.00
# elif (unit<=100):
#     amount=130+((unit-50)*3.25)
#     fixed_charge=25.00
# elif (unit<=200):
#     amount=130+162.50+((unit-100)*5.26)
#     fixed_charge=25.00
# else:
#     amount=130+162.50+526+((unit-200)*8.45)
#     fixed_charge=25.00
# total=amount+fixed_charge
# print("Electricity bill=%.2f" %total)


# # Activity-3

# print("Select your ride: ")
# print("1. Bike")
# print("2. Auto")
# print("3. Car")

# chioce=int(input("enter your choice: "))
# if chioce==1:
#     print("Bike is available")
# elif chioce==2:
#     print("Auto is available")
# elif chioce==3:
#     print("Car is available")
#     option=int(input("Do you want to book a car? (1.BMW, 2. MCD, 3.SCORPIO): "))
#     if option==1:
#         print("BMW is available")
#     elif option==2:
#         print("MCD is available")
#     elif option==3:
#         print("SCORPIO is available")
#     else:
#         print("No CAR available")
# else:
#     print("No ride available")

# # LOOP-ACTIVITY-1
# n=int(input("Enter the num : "))
# sum=0
# for i in range(1, n+1):
#     sum=sum+i
#     print("\n Sum of whole num: ")
    
# # Act-2
# string=input("enter your string : ")
# string2=('')
# for i in string:
#     string2=i+string2
    
# print("original string: ", string)
# print("the reversed string :- ", string2)
# # Activity-3
# n=int(input("Enter the num : "))
# print("number from {0} to {1} are : ".format(n,1))
# for i in range(n, 0, -1):
#     print(i)
    
    
# # ACTIVITY-1--WHILE LOOP

# n= int(input("Enter the value : "))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i= i+1
# print("\n sum : ", sum)



# # ACTIVITY-1 --NESTED LOOP


# string=input("Enter your string")
# char=input("Enter your char")
# i=0
# count=0
# while (i<len(string)):
#     if(string[i] == char):
#         count = count +1
#     i = i+1
# print("The total number of times", char , "has occured = ", count)


# TURTLE-LIBRARY

import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num_sides =6
side_length = 70
angle =360.0/num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()


# Activity-2 

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()

board.forward(100)

board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.penup()
board.rigth(150)
board.forward(50)

board.pendown()
board.rigth(90)
board.forward(100)

board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

turtle.done()


# Activity-3
my_wn = turtle.Screen()
my_wn.bgcolor("orange")
my_wn.title("Turtle")
my_pen=turtle.Turtle()
size=0
while True:
    for i in range(4):
        my_pen.fd(size+1)
        my_pen.left(90)
        size=size-5
    size = size + 1