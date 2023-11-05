class Solution:
    def convertToTitle(self,columnNumber):
        result = ''
        
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-based indexing
            remainder = columnNumber % 26  # Calculate the remainder
            result = chr(65 + remainder) + result  # Convert to character and prepend to result
            columnNumber //= 26  # Integer division
            
        return result
