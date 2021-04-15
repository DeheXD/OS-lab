#example of input
ProcessSize=[212, 417, 112, 426]
MemorySize=[100, 500, 200, 300, 600, 900]

#which memory will be allocate at
allocation=[]

#which process is occupied in the memory
choose=[]

#if occupied memory size = 0
occ=0

#loop process size
for i in range(0,len(ProcessSize),1):                      
    
    #loop the memory size
    for j in range(0,len(MemorySize),1):

        #check whether process size is lower or equal to memory size,
        #TRUE(that memory will be occupied), FALSE(continue looping)
        if ProcessSize[i]<=MemorySize[j]:                  
            MemorySize[j]=occ
            allocation.append(j)
            choose.append(i)
            break


#printing output
print(" Process No.\tProcess Size\tBlock no.")
j=0 
for i in range(len(MemorySize)):
    if i>len(ProcessSize)-1 or i>len(choose)-1:
        break 
    j=choose[i]
    print(" ", j + 1, "\t\t", ProcessSize[j],"\t\t", end = " ")  
    if  len(allocation)>i and allocation[i] >=0:  
        print(allocation[i]+1)
    else: 
        print("Not Allocated") 


