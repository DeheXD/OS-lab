def LRU(S,A):
    NewA=[]
    Check=[]
    for i in range(0,len(A),1):
        if A[i] in NewA:
            for j in range (0,len(Check),1):
                if Check[j] == A[i]:
                    Check.pop(j)
                    Check.append(A[i])
            print('hit',NewA)
            continue
        elif len(NewA) == S:
            Check.append(A[i])
            for k in range(0,len(NewA),1):
                if NewA[k]==Check[0]:
                    NewA[k]=A[i]
                    Check.pop(0)
                    break
        else:
            NewA.append(A[i])
            Check.append(A[i])
        print (NewA)

A=[7,0,1,2,0,3,0,4,2,3,0,3,2]
LRU(4,A)