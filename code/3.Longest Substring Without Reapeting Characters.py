class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxlen, start, end = 0, 0, 0
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                start = max(hashmap[s[i]]+1, start)
            end = i                         # end index
            hashmap[s[i]] = i   # point to the last character index
            maxlen = max(maxlen, end-start+1)   # updated maxlength
        return maxlen
