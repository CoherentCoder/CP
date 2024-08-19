class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = len(nums)-1
        l = 0
        while l <= h:
            mid = (h+l)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    h = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] < target <= nums[h]:
                    l = mid+1
                else:
                    h = mid-1
        return -1
