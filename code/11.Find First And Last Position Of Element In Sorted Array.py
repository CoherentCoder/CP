class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lindex, rindex = -1, -1
        low, high = 0, len(nums)-1
        pin = -1

        while low <= high:  # binary search O(log.n)
            mid = (high+low)//2
            if nums[mid] == target:
                pin = mid
                break
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1

        if pin != -1:   # index found O(2.log.n/2)
            ll, lh, rl, rh = low, pin, pin, high
            rindex, lindex = pin, pin

            # for left index
            while ll <= lh:
                lm = (ll+lh)//2
                if nums[lm] == target:
                    lindex = lm
                    lh = lm-1
                else:
                    ll = lm+1
            
            # for right index
            while rl <= rh:
                rm = (rl+rh)//2
                if nums[rm] == target:
                    rindex = rm
                    rl = rm+1
                else:
                    rh = rm-1

        return [lindex, rindex]
