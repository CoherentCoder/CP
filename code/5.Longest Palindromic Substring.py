# Problem Statement: https://leetcode.com/problems/longest-palindromic-substring/
# Reference: https://youtu.be/UflHuQj6MVA

class Solution(object):
    def longestPalindrome(self, s):
        mat = [[False for _ in range(len(s))] for _ in range(len(s))]
        start, end, k = 0, 0, 0
        for i in range(len(s)):
            for j in range(len(s)-i):
                if j == j+k or (j == j+k-1 and s[j] == s[j+k]):
                    mat[j][j+k] = True
                    if end-start < k:
                        start = j
                        end = j+k
                elif s[j] == s[j+k] and mat[j+1][j+k-1]==True:
                    mat[j][j+k] = True
                    if end-start < k:
                        start = j
                        end = j+k
            k+=1
        return s[start:end+1]
