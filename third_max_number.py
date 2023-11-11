class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_=set()
        for i in range(0,len(nums)):
            if nums[i] not in set_:
                set_.add(nums[i])

        set_sorted=sorted(set_)[::-1]  

        if len(set_sorted)>=3:
            return set_sorted[2]
        return max(set_sorted)    
