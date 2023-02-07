from typing import List

def two_sum(nums:List[int], target:int):
    result = []

    for i, num in enumerate(nums):
        temp = target - num

        if temp in nums[i+1:]:
            # result.append(i)
            result.append(nums.index(num))
            result.append(nums[i+1:].index(temp) + (i+1))
    #print(result)
    return(result)

two_sum([3,3], 6)