


def firstOccurrence(nums, element, i) :
    # Base case
    if i == len(nums) :
        return -1 
    if nums[i] == element :
        return i
    return firstOccurrence(nums, element, i + 1)

def lastOccurrence(nums, element, i) :
    if i == len(nums) :
        return -1
    if nums[i] == element :
        ans = lastOccurrence(nums, element, i + 1)
        if ans == -1 :
            return i
        else :
            return ans
    else :
        return lastOccurrence(nums, element, i + 1)
    

print(2 ** 43)

# nums = [10, 20, 25, 40, 20]
# element = 100
# print("last occurrence of ", element, " is : ", lastOccurrence(nums, element, 0))

# print(element , " present at : ", firstOccurrence(nums, element, 0))

'''
def printN(n) :
    if n == 0 :
        return
    print(n , end = " ") 
    printN(n - 1) 
    
n = 4
printN(n)

def fact(n) :
    if n == 1 :
        return n
    smallAns = fact(n - 1) 
    return n * smallAns


# print(fact(n))
'''