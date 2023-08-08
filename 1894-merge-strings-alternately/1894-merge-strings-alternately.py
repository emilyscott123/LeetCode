class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first, second = 0, 0 
        answer = ""

        while first < len(word1) and second < len(word2):
            answer += word1[first]
            answer += word2[second]
            first += 1
            second += 1
        
        while first < len(word1):
            answer += word1[first]
            first += 1
        
        while second < len(word2):
            answer += word2[second]
            second += 1

        return answer 