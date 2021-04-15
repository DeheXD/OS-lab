job=['A','B','C','D']
jobSize=[5,2,6,4]

def SJF(J,JS):
    temp=0
    print ('SJF')
    for i in range (0,len(J)):
        for j in range (0,len(J)):
            if JS[i]<JS[j]:
                temp = JS[j]
                JS[j] = JS[i]
                JS[i] = temp
                temp = J[j]
                J[j] = J[i]
                J[i] = temp
    #print(J,JS)
    print('Job\tJob Size\tWaiting Time\tTurnaround time')
    WaitingTime=0
    TurnaroundTime=0
    TotalWaitingTime=0
    TotalTurnaroundTime=0
    for i in range (0,len(J)):
        TurnaroundTime+=JS[i]
        print(J[i],'\t',JS[i],'\t\t',WaitingTime,'\t\t',TurnaroundTime)
        TotalWaitingTime+=WaitingTime
        TotalTurnaroundTime+=TurnaroundTime
        if i == len(J)-1:
            break
        WaitingTime+=JS[i]
    print(WaitingTime,TurnaroundTime)
    print('Avg waiting time = ',TotalWaitingTime/len(J))
    print('Avg turnaround time = ',TotalTurnaroundTime/len(J))

SJF(job, jobSize)