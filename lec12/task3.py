def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1): # 4, 3, 2, 1
        for i in range(passnum): # 0, 4 ::: 0,3:: 0,2:: 0:1
            if nlist[i]<nlist[i+1]: #[5,4,3,2,1]  -> [4,5,3,2,1] ->[4,3,5,2,1]
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    return nlist


a = [5,4,3,2,1]
print(bubbleSort(a))