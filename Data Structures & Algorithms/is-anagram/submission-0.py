class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts={}
        if len(s)==len(t):
            for i in s:
                if i in counts:
                    counts[i]+=1
                else:
                    counts[i]=1
            for j in t:
                if j in counts:
                    counts[j]-=1
                else:
                    return False
            for value in counts.values():
                if value !=0:
                    return False
            return True
            
        return False