class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            sorted_word="".join(sorted(i))
            if sorted_word not in dict:
                dict[sorted_word]=[i]
            else:
                dict[sorted_word].append(i)
        return list(dict.values())
        