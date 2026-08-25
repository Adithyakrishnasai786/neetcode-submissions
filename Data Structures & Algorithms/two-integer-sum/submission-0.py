class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     dict={}
     for i in range(len(nums)):
        curr=nums[i]
        diff=target-curr
        if diff in dict:
            return [dict[diff],i]
        else:
            dict[curr]=i
     return None
        
