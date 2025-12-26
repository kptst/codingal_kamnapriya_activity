a=10
b=12
c=0
if a and b and c:
     print("All number have boolean")
else:
    print("at least one number is boolean")
    
x=10
y=-10
z=0
if x>0 or y>0:
    print("either number is greater than 0")
elif x>0 or y<0:
    print("any one number is not grater than 0")
else:
    print("no number greater than 0")
    
    
p=10
q=12
r=12

print(p!=q)
print(q!=r)

# BMI CALC""
height=input("tell me H")
weight=float(input("tell me Weight"))
BMI= weight/(height/100)**2
print("Your BMI is : ", BMI)

# PY-OPERATOR-III (ACTIVITY-1)
x=5
if(type(x) is int):
    print('true')
else:
    print("false")
    
    
if(type(x) is not int):
    print('true')
else:
    print("false")
    
    
# ACTIVITY-2
a=10
b=-10
print("a>>1", a>>1)
print("b>>1", b>>1)
print("a<<1", a<<1)
print("b<<1", b<<1)

# LOOP
# ACTIVITY-1

n= int(input("Enter the number"))
sum=0
for i in range(1, n+1):
    sum=sum+1
    print("\nSum = ", sum)
    
# ACTIVITY-2

string=input("please enter your string: ") 
string2=('')
for i in string:
    string2= i + string2
print("original string", string)
print("Reverse string", string2)

# ACTIVITY-1 (WHILE-LOOP)
n= int(input("Enter the Value: "))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("\nSum = ", sum)

# ACTIVITY-2 (WHILE-LOOP)
i=0
while i<10:
  print("I will rum forever", i)

# ACTIVITY-3 (WHILE-LOOP)
num= int(input("Enter the number: "))
sum=0
temp =num
while temp>0:
  digit=temp%10
  sum+=digit**3
  temp//=10

if num == sum:
  print(num, "is an Armstrong number")
else:
  print(num, "is not an Armstrong number")


# NESTED-LOOP-ACTIVITY-1
string=input("Please enter your string")
char=input("please enter your character")
i=0
count=0
while(i<len(string)):
    if(string[i]==char):
        count=count+1
    i=i+1
    
print("The total num of times", char,"has occured=", count)

# ACTIVITY-2
lower=int(input("Enter the lower range : "))
upper=int(input("Enter the upper range : "))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)

# activity-3
num = int(input("Enter the number: "))
t = num
numlen = 0

# Count number of digits
while t > 0:
    numlen += 1
    t //= 10

print("The number of digits in the number are:", numlen)

if numlen >= 3:
    # For even length → two middle digits
    if numlen % 2 == 0:
        mid1_index = numlen // 2 - 1
        mid2_index = numlen // 2
    else:
        # For odd length → same digit twice (to allow product logic)
        mid1_index = mid2_index = numlen // 2

    # Extract digits
    digits = []
    t = num
    while t > 0:
        digits.insert(0, t % 10)  # keep original order
        t //= 10

    midOne = digits[mid1_index]
    midTwo = digits[mid2_index]

    print("The 1st middle digit is:", midOne)
    print("The 2nd middle digit is:", midTwo)

    prod = midOne * midTwo
    print("The product of the middle digits is:", prod)

else:
    print("The number has less than 3 digits, so no middle digits.")



# ARGUMENTS--Activity-1
def total_calc(bill_amount, tip_perc):
    total = bill_amount*(1+0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")
    
total_calc(150.20)

# Activity-2
def cube(number):
    return number*number*number
def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False

print(by_three(9))
print(by_three(5))

# Activity-3
def factorial(x):
    '''this is recursive function to find the factorial of an integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

print(factorial.__doc__)
print("the factorial of 0: ", factorial(0))
print("the factorial of 1: ", factorial(1))
print("the factorial of 2: ", factorial(2))
print("the factorial of 3: ", factorial(3))
print("the factorial of 4: ", factorial(4))


# KEYWORDS-Activity-1
a=input("enter a word : ")
for i in a:
    if(i=='A'):
        print("A is found")
        break
    else:
        print("A not found")

# Activity-2
for x in range (10):
    if x%20==0:
        print("twist")
    elif x%15==0:
        pass
    elif x%5==0:
        print("fizz")
    elif x%3==0:
        print("buzz")
    else:
        print(x)

# Activity-3
var=10
while var>0:
     var=var-1
     if var==5:
         continue
     print("current variable value : ", var)
print("good bye!")


# RANDOM & MATH MODULE
import random
playing = True
number= str(random.randint(1,100))

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
print("You have 5 attempts to guess the number.")
print("Let's start the game!")
while playing:
    guess=  input("Enter your guess: ")
    if guess == number:
        print("Congratulations! You guessed the number!")
        playing = False
        break
    elif guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
    print("You have 4 attempts left.")


# Activity-3
import math
x=10
y=-15
print("x+y = ", x+y)
print('absolute value of -96 and 56 are: ', str(math.fabs(-96)), str(math.fabs(56)))
print('the value of 2**3 is: ', math.pow(2,3))
    
    
gulvisha=['apple', 'banana', 'fig', 'grape' , 'cherry']
print(gulvisha)
print(len(gulvisha))
print(gulvisha[2])
print(gulvisha[-3])
print(gulvisha[1:4])
print(gulvisha[:4])
print(gulvisha[2:])
print(gulvisha[0:5:2])
# append
gulvisha.append('kiwi')
print(gulvisha)
# nested listing
gulvisha1=[[23,45], [21,54]]
print(gulvisha1)
# reverse
gulvisha.reverse()
print(gulvisha)


gulvisha=['apple', 'banana', 'fig', 'grape' , 'cherry']
print(gulvisha)
print(len(gulvisha))
print(gulvisha[2])
print(gulvisha[-3])
print(gulvisha[1:4])
print(gulvisha[:4])
print(gulvisha[2:])
print(gulvisha[0:5:2])
# append
gulvisha.append('kiwi')
print(gulvisha)
# nested listing
gulvisha1=[[23,45], [21,54]]
print(gulvisha1)
# reverse
gulvisha.reverse()
print(gulvisha)


# Activity-2
def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("number of words with same first and last letter: ", lst)
    return ctr
count=match_words(['abc', 'xyz', 'aba', '1221'])
print("count: ", count)


# Activity-3
L= [1,2,3,4,5,6,7,8,9,10]
print("original list: ", L)
count=0
for i in L:
    count+=i
average=count/len(L)
print("average: ", average)
print("sum: ", count)

# activity-1 tuples
tuplex=("w", 3, "r", 2.5, "s", "o", "u", "r",False, "e")
print(tuplex)
print(len(tuplex))
print(tuplex.count("r"))
print(tuplex[3:5])
print(tuplex[0:9:2])

# activity-2
tupley=("fruits", "vegetables", "meat", "dairy", "bread")
print("tuple 1: ", tupley)
tuplez=("apple", "banana", "fig", "grape" , "cherry")
print("tuple 2: ", tuplez)
tuplex=tupley+tuplez
print("tuple 3: ", tuplex)
# flip-flop
temp=tupley
tupley=tuplez
tuplez=temp
print("tuple 1: ", tupley)
print("tuple 2: ", tuplez)


# activity-3
weather=(1,0,0,1,0,1,0,0,1,1,0,1)
sunny=0
rainy=0
for i in range(0,12):
    if (weather[i]==0):
         rainy+=1
    else:
        sunny+=1
if (sunny>rainy):
     print("Good weather")
else:
     print("Bad weather")

# Activity-1
numers1= [1,2,3,4,5]
numbers2= [6,7,8,9,10]
result=map(lambda x,y: x+y, numers1, numbers2)
print(list(result))

nums= [1,2,3,4,5,6,7,8,9,10]
def sq(n):
    return n*n
square = list(map(sq, nums))
print(square)
print(list(map(lambda x: x*x, nums)))

# Activity-2
s1={2,3,1}
s2={'b', 'a', 'c'}
s3=list(zip(s1,s2))
print(s3, "\n")
print(sorted(s3))


list1= [10,20.30]
list2= [100,200,300]
for x, y in zip(list1, list2[::-1]):
     print(x, y)

# Activity-3
for i in range(10):
    if i==5:
        print(exit)
        exit()
    print(i)
    


# # Activity-1
# ----- TIC TAC TOE GAME -----

# Initialize the board
# theBoard = {
#     '7': ' ', '8': ' ', '9': ' ',
#     '4': ' ', '5': ' ', '6': ' ',
#     '1': ' ', '2': ' ', '3': ' '
# }

# board_keys = list(theBoard.keys())

# # Function to print the board
# def printBoard(board):
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])
#     print()

# # Main game function
# def game():
#     turn = 'X'
#     count = 0
#     game_over = False

#     for i in range(9):  # Maximum 9 moves
#         printBoard(theBoard)
#         print("It's your turn, " + turn + ". Move to which place? (1-9)")
#         move = input()

#         # Validate input
#         if move not in theBoard:
#             print("Invalid move! Please choose a number between 1-9.\n")
#             continue

#         # Check if the spot is empty
#         if theBoard[move] == ' ':
#             theBoard[move] = turn
#             count += 1
#         else:
#             print("That place is already filled. Try again.\n")
#             continue

#         # Check for a win after 5 moves
#         if count >= 5:
#             if (theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ' or
#                 theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ' or
#                 theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ' or
#                 theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ' or
#                 theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ' or
#                 theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ' or
#                 theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ' or
#                 theBoard['1'] == theBoard['5'] == theBoard['9'] != ' '):

#                 printBoard(theBoard)
#                 print("Game Over.\n")
#                 print("**** " + turn + " won! ****\n")
#                 game_over = True
#                 break

#         # If all 9 moves done and no winner → Tie
#         if count == 9 and not game_over:
#             printBoard(theBoard)
#             print("Game Over.\nIt's a Tie!\n")

#         # Switch turn
#         turn = 'O' if turn == 'X' else 'X'

#     # Ask for restart
#     restart = input("Do you want to play again? (y/n): ")
#     if restart.lower() == 'y':
#         for key in board_keys:
#             theBoard[key] = ' '
#         game()

# # Run the game
# if __name__ == "__main__":
#     game()

# print("above game - tic tac toe")


import random

num = random.randint(1, 100)
print("Guess the number (1–100)")

while True:
    guess = int(input("Your guess: "))
    if guess < num:
        print("Too low! Try a bigger number.")
    elif guess > num:
        print("Too high! Try a smaller number.")
    else:
        print("🎉 Correct! You guessed it!")
        break

    # extra hint
    if abs(num - guess) <= 10:
        print("🔥 You're very close!")


# # Activity-1
class student:
  grade = 10
  print("My grade is : ", grade)
obj=student()

# Activity-2
class Vehicle:
  def __init__(self,max_speed, mileage):
     self.max_speed=max_speed
     self.mileage=mileage

modelX=Vehicle(200,18)
print("Model Max speed : ", modelX.max_speed)
print("Model Mileage : ", modelX.mileage)
    
  

class Dog:
  # Class variable: Shared by all instances of the Dog class
  species = "Canine" 

  def __init__(self, name, breed):
      # Instance variables: Unique to each instance of the Dog class
      self.name = name
      self.breed = breed

  def display_details(self):
      """Displays the details of the dog."""
      print(f"Name: {self.name}")
      print(f"Breed: {self.breed}")
      print(f"Species: {Dog.species}\n") # Accessing the class variable

# Create instances of the Dog class for two different breeds
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Charlie", "Bulldog")

# Display the details of each dog
print("Details of Dog 1:")
dog1.display_details()

print("Details of Dog 2:")
dog2.display_details()



# Activity-1- inheritance
class Vehicle:
   def __init__(self, name, max_speed, mileage):
      self.name=name
      self.max_speed=max_speed
      self.mileage=mileage
class Bus(Vehicle):
   pass

School_bus=Bus("School Volvo", 180, 12)
print("Vehicle Name: ", School_bus.name, "\nSpeed: ", School_bus.max_speed, "\nMileage: ", School_bus.mileage)

# Activity-2

class Person(object):
  def __init__(self,name, idnumber):
     self.name=name
     self.idnumber= idnumber
  def display(self):
     print(self.name)
     print(self.idnumber)
class Employee(Person):
   def __init__(self, name, idnumber, salary, post):
      self.salary=salary
      self.post=post
      Person.__init__(self, name, idnumber)
a = Employee('Rahul', 886012, 200000, "Intern")
a.display()

