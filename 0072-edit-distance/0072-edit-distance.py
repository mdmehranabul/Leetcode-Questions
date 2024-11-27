class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache=[[float("infinity")]*(len(word2)+1) for _ in range(len(word1)+1)]
        
        # Filling the last column
        for i in range(len(word1)+1):
            cache[i][len(word2)]= len(word1)-i

        for j in range(len(word2)+1):
            cache[len(word1)][j]=len(word2)-j
        

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    cache[i][j]=cache[i+1][j+1]
                else:
                    cache[i][j]=1+min(cache[i][j+1],cache[i+1][j],cache[i+1][j+1])

        return cache[0][0]
        
#Time Complexity - O(length of word 1 x length of word2)
#Space Complexity - O(length of word 1 x length of word2)