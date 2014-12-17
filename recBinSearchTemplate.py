def recBinSearch(x, nums, low, high):
    if low > high:
        return -1
    mid = (high + low)//2
    if x == nums[mid]:
        return mid
    elif nums[mid] > x:
        return recBinSearch(x, nums, low, mid-1)
    else:
        return recBinSearch(x, nums, mid+1, high)
            
def recBinarySearch (x, nums):
    low = 0
    high = len (nums) - 1
    print("recBinSearch({}, {})".format(low, high))
    return recBinSearch(x, nums, low, high)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def iterFib(n):
    if n==0 or n==1:
        return 1
    count=1
    prev1,prev2=1,1
    while count < n:
        prev1, prev2 = prev1+prev2, prev1
##        num=prev1+prev2
##        prev1=num
##        prev2=prev1
        count+=1
    return prev1
