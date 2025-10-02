class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        visited = {}
        max_len = 0
        
        for i in range(len(s)):
            if s[i] in visited:
                start = max(visited[s[i]] + 1, start)
            visited[s[i]] = i
            max_len = max(max_len, i - start + 1)

        return max_len
            
        