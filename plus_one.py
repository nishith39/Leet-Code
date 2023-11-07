class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st=''
        for i in digits:
            st+=str(i)

        sa=str(int(st)+1)

        lis=[]
        for i in sa:
            lis.append(int(i))

        return(lis) 