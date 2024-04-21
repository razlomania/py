def find_length(nums, k):
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans

def find_length1(s: str):
    left = curr = ans = 0 
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans

def numSubarrayProductLessThanK(nums, k):
    if k < 1:
        return 0
    
    left = ans = 0
    curr = 1
    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1
        ans += right - left + 1    
    return ans

def find_largerst_sub_array(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(curr, ans)
        
    return ans

def max_avarage(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
        curr / k
    
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        
        ans = max(ans, curr / k)
    return ans  

# anlternative 
# def findMaxAverage(self, nums: List[int], k: int) -> float:
#     curr = sum(nums[:k])
#     max_avg = curr / k

#     for i in range(k, len(nums)):
#         curr += nums[i] - nums[i - k]
#         max_avg = max(max_avg, curr / k)

#     return max_avg
          

print(max_avarage([10, -5, 5 ,2, 6, -4], 3))