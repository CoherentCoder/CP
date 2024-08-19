class Solution:
    def longestPalinSubseq(self, S):
        mat = [[1 for j in range(len(S))] for i in range(len(S))]
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                mat[i][i+1] = 2
    
        for j in range(2,len(S)):
            for i in range(len(S)-j):
                if S[i] == S[i+j]:
                    mat[i][i+j] = mat[i+1][i+j-1] + 2
                else:
                    mat[i][i+j] = max(mat[i][i+j-1], mat[i+1][i+j])
        
        return mat[0][-1]
