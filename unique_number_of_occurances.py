class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr2=list(set(arr))
        lis=[]
        for i in range(0,len(arr2)):
            counts_=arr.count(arr2[i])
            lis.append(counts_)

        if len(lis)==len(set(lis)):
            return True    
        return False    