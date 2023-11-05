from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find the shortest string in the list
        min_len = min(len(s) for s in strs)
        
        for i in range(min_len):
            # Check if the character at the current position is the same in all strings
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return s[:i]
        
        return strs[0][:min_len]
