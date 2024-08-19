class Solution(object):
    def twoSum(self, nums, target):
        numMap = {}	  # hashmap {difference: index}
        n = len(nums)	# total NO. of available sequences
        for i in range(n):
            diff = target - nums[i]
            if diff in numMap:
                return [numMap[diff], i]
            numMap[nums[i]] = i
        return []	    # no solution found
