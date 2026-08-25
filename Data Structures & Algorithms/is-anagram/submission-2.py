class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts={}
        if len(s)==len(t):
            for i in range(len(s)):
                
                # --- Step 1: Add 1 for the letter in 's' ---
                if s[i] in counts:
                    counts[s[i]] += 1
                else:
                    counts[s[i]] = 1
                    
                # --- Step 2: Subtract 1 for the letter in 't' ---
                if t[i] in counts:
                    counts[t[i]] -= 1
                else:
                    counts[t[i]] = -1
            for value in counts.values():
                if value != 0:
                    return False
            return True
        return False