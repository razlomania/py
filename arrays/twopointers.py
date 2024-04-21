def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

def two_sums(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        curr = left + right
        if curr == target:
            return True
        if curr > target: 
            right -= 1
        if curr < target: 
            left += 1
    return False


def isSubsequence(s: str, t: str):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)

def revers_string(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        
    return s

def combine(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
        
    return ans

def combine2(arr1, arr2):
    i = j = 0
    ans = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1    
        
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1         
    
    return ans
    
print(combine2([1,3,5,7], [2,4,6,8,9,10]))