# INTRO-PY CODE
# ACTIVITY-1
print("Hello World\n")
print(10)
print("Kabilan age is ", 20)

#Activity-2

x=5
print(x)

y="Kabilan"
print(y)

codingal="codingal1"
print(codingal)

name=input("Enter your name:")
print(name)

# Activity-3
import keyword

print("All the keywords in python are: ")
print(keyword.kwlist)

# Activity-1-datatype
a=5
print("type of a: ", type(a))

b=5.5
print("type of a: ", type(b))

c="Kabi"
print("type of a: ", type(c))

# Activity-2
weight=19.6
print("weight", weight)
print("typecasting into integer: ", int(weight))

is_student=True 
print("is_student: ", is_student)
print("is_student: ", type(is_student))

# Activity-3
text=str(input("enter your message here: "))
revText = text [::-1]
text = revText

print("Reverse of Given String is: ")
print(text)

# ACTIVITY-OPERATOR
tree1=98
tree2=94
tree3=41
tree4=95
tree5=11

sum=tree1+tree2+tree3+tree4+tree5
print("sum of trees is",sum)
average=sum/5
print("average of trees is",average)


# Activity-2

amount=int(input("enter the amount"))
note_1=amount/100
note_2=(amount%100)/50
note_3=((amount%100)%50)/10

print("note of 100 is",note_1)
print("note of 50 is",note_2)
print("note of 10 is",note_3)


# Activity-3
math=int(input("enter the math marks"))
english=int(input("enter the english marks"))
science=int(input("enter the science marks"))
hindi=int(input("enter the hindi marks"))
sum=math+english+science+hindi
print("sum of marks is",sum)

avrg=sum/4
print("average of marks is",avrg)


