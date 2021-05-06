def count(num):
    list=[]
    for i in range(num,-1,-1):
        list.append(i)
    return list    
print(count(3))

#2
def Print_Return(list):
    print(list[0])
    return list[1]

print(Print_Return([1,2]))

#3
def First_Plus_Length(list): 
    sum=list[0]+len(list)
    return sum

print(First_Plus_Length([1,2,3]))   



#4
def Values_Greater_than_Second(list):
    if len(list) > 2:
        newlist=[]
        for i in range(0,len(list)):
            if list[i] > list[1]:
                newlist.append(list[i])
        print(len(newlist))
        return newlist
    else:
        return False
print(Values_Greater_than_Second([1,2,3,4])) 

#5
def This_Length_That_Value(size,value):
    list=[]
    for i in range(0,size):
        list.append(value)
    return list
print(This_Length_That_Value(4,7))    
    
       

