#1
def Biggie_Size(list):
    for i in range(0,len(list)):
        if list[i] > 0:
            list[i]="big"
    return list        
    
print(Biggie_Size([-1, 3, 5, -5]))

#2
def Count_Positives(list):
    count=0;
    for i in range(0,len(list)):
        if list[i] > 0:
            count=count+1
    list[-1] = count
    return list
print(Count_Positives([1,6,-4,-2,-7,-2]))

#3
def Sum_Total(list):
    sum=0
    for i in range(0,len(list)):
        sum=sum+list[i]
    return sum
print(Sum_Total([1,2,3,4]))    

#4 
def Average(list):
    sum=0
    for i in range(0,len(list)):
        sum=sum+list[i]
    avg=sum/len(list) 
    return avg
print(Average([1,2,3,4]))

#5
def length(list):
     l = len(list)
     return l
print(length([]))

#6
def minum(list):
   
    if len(list) > 0:
        min=list[0]
        for i in range(0,len(list)):
            if min > list[i]:
                min=list[i]
    elif len(list) == 0:
        return False
    return min
print(minum([37,2,1,-9]))
print(minum([]))

#7
def maxum(list):
   
    if len(list) > 0:
        max=list[0]
        for i in range(0,len(list)):
            if max < list[i]:
                max=list[i]
    elif len(list) == 0:
                return False
    return max
print(maxum([37,2,1,-9]))
print(maxum([]))  

def ultimate_Analysis(list):
    min=list[0]
    max=list[0]
    sum=0
    length=len(list)
    dic={
        
    }
    for i in range(0,len(list)):
        sum=sum+list[i]
        if(min> list[i]):
            min=list[i]
        elif max < list[i]:
            max=list[i]
    avg=sum/len(list)
    dic["sum"]=sum
    dic["average"]=avg
    dic["min"]=min
    dic["max"]=max
    dic["length"]=length
   
    return dic
print(ultimate_Analysis([37,2,1,-9]))

#9
def reverse_List(list):
    i=0
    end = len(list)-1
    j=end
    while(i<j):
        temp=list[i]
        list[i]=list[j]
        list[j]=temp
        i=i+1
        j=j-1
    return list
print(reverse_List([37,2,1,-9]))    
    
    
            
                
    
    
  
            
        
   


   
    