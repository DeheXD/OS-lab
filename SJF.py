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
    wt=0
    tt=0
    twt=0
    ttt=0
    for i in range (0,len(J)):
        tt+=JS[i]
        print(J[i],'\t',JS[i],'\t\t',wt,'\t\t',tt)
        twt+=wt
        ttt+=tt
        if i == len(J)-1:
            break
        wt+=JS[i]
    print(wt,tt)
    print('Avg waiting time = ',twt/len(J))
    print('Avg turnaround time = ',ttt/len(J))

SJF(job, jobSize)