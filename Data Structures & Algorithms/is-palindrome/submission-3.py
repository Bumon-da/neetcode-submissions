class Solution:
    def isPalindrome(self, s: str) -> bool:
        all_lowercase=""

        for c in s:
            if c.isalnum():
                all_lowercase+=c.lower()
        
        n = len(all_lowercase)

        for i in range(0, n//2):
            if all_lowercase[i]!= all_lowercase[n-1-i]:
                return False
        
        return True