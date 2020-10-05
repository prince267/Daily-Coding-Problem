def findPairs(nums:list,k:int)->bool:
    counter={}
    for num in nums:
        if(num in counter):
            counter[num]+=1
        else:
            counter[num]=1
    for j in counter:
        b=j+k
        if(b in counter):
            if(k==0):
                return(counter[b]>=2)
            return True
    return False