class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        for i in range(len(nums)):
            sub=target-nums[i]
            if sub in map1:
                return map1[sub],i
            else:
                map1[nums[i]]=i   