class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for item in s:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        for values in (freq.keys()):
            if freq[values] == 1 :
                key = values
                return s.index(key)
        return -1
