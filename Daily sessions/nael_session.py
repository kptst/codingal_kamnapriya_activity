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

print("Half pyramid patterns of (*): ")
num= int(input("Enter the number of rows: "))
for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print()
    
    