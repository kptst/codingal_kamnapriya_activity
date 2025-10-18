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