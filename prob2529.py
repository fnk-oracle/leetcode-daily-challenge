class Solution:

    def lower_bound(self,nums):
        start, end = 0, len(nums)-1

        index = len(nums)

        while start <= end:
            mid = ( start + end ) // 2

            if nums[mid] < 0:
                start = mid+1
            else:
                end = mid-1
                index = mid
        return index
        
    def upper_bound(self, nums):
        start , end = 0, len(nums)-1
        index = len(nums)

        while start <= end:
            mid = (start + end)//2

            if nums[mid]<=0:
                start = mid+1
            else:
                end=mid-1
                index = mid
        return index


    def maximumCount(self, nums: List[int]) -> int:

        positive_count = len(nums) - self.upper_bound(nums)

        negative_count = self.lower_bound(nums)

        return max(positive_count,negative_count)

        