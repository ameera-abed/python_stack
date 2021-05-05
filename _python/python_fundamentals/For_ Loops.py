for i in range(0,151):
    print(i)

#Multiples of Five
for i in range(5,1000):
    if i%5 == 0:
        print(i)

 #Counting, the Dojo Way 
for i in range(1,101):
     if i%5 == 0:
         print("coding")
     if i%10 == 0:
         print("coding dojo")  

#Whoa. That Sucker's Huge
sum=0
for i in range(0,500001):
    if i%2 !=0:
        sum=sum+i
print(sum)        

#Countdown by Fours
for i in range(2018,0,-4):
    print(i)

#Flexible Counter
high=6
low=2
multi=2
for i in range(low,high+1):
    if(i%multi == 0):
        print(i) 
    