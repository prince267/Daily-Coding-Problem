def productNumbers(nums):
    n=len(nums)
    prev_mul=[1]
    next_mul=[1]
    for i in range(n-1):
        a=prev_mul[i]
        prev_mul.append(a*nums[i])
        a=next_mul[i]
        next_mul.append(a*nums[n-1-i])
    result=[]
    for i in range(n):
        result.append(prev_mul[i]*next_mul[n-1-i])
    return(result)

result=productNumbers([3,2,1])
print(result)

