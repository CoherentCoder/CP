# Time Limit Exceeded (leetcode)
# optimization needed

class Solution:
    def twosum(self, nums, target):
        hashtable = dict()
        result = set()
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hashtable:
                result.add(tuple(sorted([nums[i], diff])))
            else:
                hashtable[nums[i]] = i
        return [list(a) for a in result]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashtable = dict()
        result = set()
        for i in range(len(nums)-2):
            target = -nums[i]
            if target in hashtable:
                for a in list(hashtable[target]):
                    result.add(tuple(sorted(a+[nums[i]])))
            else:
                twosum = self.twosum(nums[i+1:], target)
                hashtable[target] = twosum
                for res in twosum:
                    result.add(tuple(sorted([nums[i]]+res)))
        return list(result)
