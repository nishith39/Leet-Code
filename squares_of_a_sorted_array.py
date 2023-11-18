class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        lis=[]

        for i in range(0,len(nums)):
            res=nums[i]*nums[i]
            lis.append(res)
        return sorted(lis)  