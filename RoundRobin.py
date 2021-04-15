job = ['A','B','C','D']
jobSize = [8,4,9,5]

def RoundRobin(Job,JobSize,StorageSize):
    TJob = len(Job)
    print("Round Robin")
    end = False
    i = 0
    WaitTime = 0
    TurnaroundTime = 0
    TotalWaitTime = 0
    TotalTurnaroundTime = 0
    print('Job\tJob executed\tCurrent job size\tWaiting\t\tTurnaround')
    while i < len(JobSize):
        if JobSize[i]>StorageSize:
            TurnaroundTime += StorageSize
            print(Job[i],"\t",StorageSize,"\t\t",JobSize[i]-StorageSize,"\t\t\t",WaitTime,"\t\t",TurnaroundTime)
            WaitTime += StorageSize
            TotalWaitTime += WaitTime
            JobSize.append(JobSize[i]-StorageSize)

            if JobSize[i]-StorageSize>0:
                Job.append(Job[i])
                
        else:
            TurnaroundTime+=JobSize[i]
            print(Job[i],"\t",JobSize[i],"\t\t",0,"\t\t\t",WaitTime,"\t\t",TurnaroundTime,Job[i])
            WaitTime += JobSize[i]
            TotalWaitTime += WaitTime
            TotalTurnaroundTime += TurnaroundTime
        i+=1
    print("Avg waiting time =",TotalWaitTime/TJob)
    print("Avg turnaround time =",TotalTurnaroundTime/TJob)
                
RoundRobin(job, jobSize, 4)