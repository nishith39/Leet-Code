class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_=0
        lis=[]
        for i in nums:
            sum_+=i
            lis.append(sum_)
        return lis    