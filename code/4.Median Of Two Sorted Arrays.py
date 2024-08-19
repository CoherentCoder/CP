class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m>n:
            return self.findMedianSortedArrays(nums2, nums1)
        MID = (m+n)//2      # grand middle
        start = 0
        end = m
        while start <= end:
            mid = (start+end)//2
            leftAsize = mid
            leftBsize = MID-mid
            leftA = nums1[leftAsize-1] if leftAsize>0 else float('-inf')
            leftB = nums2[leftBsize-1] if leftBsize>0 else float('-inf')
            rightA = nums1[leftAsize] if leftAsize < m else float('inf')
            rightB = nums2[leftBsize] if leftBsize < n else float('inf')
            if leftA <= rightB and leftB <= rightA:
                if (m+n)%2==0:
                    return (max(leftA, leftB)+min(rightA, rightB))/2
                else:
                    return min(rightA, rightB)
            elif leftA > rightB:
                end = mid-1
            else:
                start = mid+1
