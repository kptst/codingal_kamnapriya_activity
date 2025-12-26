#SDay-1

print("Welcome, I am a chatbot. How can I halp you")
name = input("What is your name: ")
print("Nice to Meet You" + name + "How can I help you?")
Querry=input("Enter your Querry: ")
print("Ok I will help in that!")
print("1. Place an order 2. Help 3.cancel the order")
option=int(input("Enter your option: "))
if option==1:
     print("Ok I will help you to place an order")
     print("1. Pizza 2. Burger 3. Pasta")
     print("Order placed successfully")
elif option==2:
     print("Ok I will help you")
     print("1. Order status 2. Delivery status 3. Cancel order")
     print("Your order is delivered")
elif option==3:
     print("Ok I will help you to cancel the order")
     print("Your order is cancelled")
else:
     print("Invalid option")