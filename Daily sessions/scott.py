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


my_tuple =()
print(my_tuple)
my_tuple =(1,2,3)
print(my_tuple)

my_tuple =(1,2,3, "hi")
print(my_tuple)

my_tuple =(1,2,3, "hi", 4.5)
print(my_tuple)

my_tuple =(1,2,3, "hi")
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

print(my_tuple[0:3])

# Activity-2
my_set={1,2,3,3,3,4,4,5,6,7,7,8,9}
print("my_set", my_set)

my_set.add(10)
print("updated my_set", my_set)

set1=my_set
set2={10,1,2,3, 14,15}
print("difference : ", set1.difference(set2))

# activity-3
setun1={"green", "blue"}
setun2={"blue", "yellow"}
print("union", setun1.union(setun2))

# Activity-4
setx={"apple", "banana"}
sety={"banana", "orange"}
print("intersection", setx.intersection(sety))


# Object oriented prog-2
# Activity-1
class Employee:
  def __init__(self): #constructor
    print("Employee created")
    
  def __del__(self):  #Destructor
    print("Destructor called. employee deleted.")
obj = Employee()
del obj

# Library Management System using OOP, Loops, and Conditionals

class Library:
    def __init__(self, name):
        self.name = name
        self.books = ["Harry Potter", "Rich Dad Poor Dad", "Atomic Habits", "Python Basics"]
        self.lend_data = {}  # To track which user has borrowed which book

    def display_books(self):
        print("\n📚 Available Books in the Library:")
        for book in self.books:
            print(f" - {book}")

    def lend_book(self, user, book):
        if book not in self.books:
            print(f"❌ The book '{book}' is not available in the library.")
        elif book in self.lend_data:
            print(f"⚠️ Sorry, '{book}' is currently lent out to {self.lend_data[book]}.")
        else:
            self.lend_data[book] = user
            print(f"✅ Book '{book}' has been lent to {user}.")

    def add_book(self, book):
        if book in self.books:
            print("⚠️ This book already exists in the library.")
        else:
            self.books.append(book)
            print(f"✅ Book '{book}' has been added to the library.")

    def return_book(self, book):
        if book in self.lend_data:
            del self.lend_data[book]
            print(f"✅ Book '{book}' has been returned successfully.")
        else:
            print(f"⚠️ '{book}' was not lent out from this library.")


# --- Main Program ---

if __name__ == "__main__":
    my_library = Library("City Central Library")

    while True:
        print("\n========== Library Menu ==========")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Exit")
        print("===================================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_library.display_books()

        elif choice == '2':
            user = input("Enter your name: ")
            book = input("Enter the book name you want to borrow: ")
            my_library.lend_book(user, book)

        elif choice == '3':
            book = input("Enter the name of the book to add: ")
            my_library.add_book(book)

        elif choice == '4':
            book = input("Enter the name of the book to return: ")
            my_library.return_book(book)

        elif choice == '5':
            print("\n📘 Thank you for using the Library Management System!")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")
