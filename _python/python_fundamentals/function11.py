import random
def randInt(min=0   , max= 100  ):
   n = random.random()*(max-min)+min
   num=round(n)
   return num
print(randInt(10,30))
print(randInt(10))
print(randInt())
print(randInt(max=30))
