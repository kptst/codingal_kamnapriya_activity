This recursive function will take 

 

T(n) = T(n/2) +T(n/2)  for 2 recursive calls and for rest code our function will take constant time.

 

def prints(n):
    if(n<=0):
        return
    print("Codingal")
    prints(n/2)
    prints(n/2)
 

So, our recurrence relation will be:

 

T(n) = T(n/2) + T(n/2) + θ(1) when n>0 

T(n) = θ(1) when n<=0

The recurrence tree for  T(n) = T(n/2) + T(n/2) + θ(1) 