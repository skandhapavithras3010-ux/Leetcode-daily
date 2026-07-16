class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        
        final = clean[::-1]
        if clean == final:
            return True
        return False                