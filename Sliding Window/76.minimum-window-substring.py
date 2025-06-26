#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map_t={}
        len_of_shortest_substring = float('inf')
        start_index = 0
        for char in t:
            hash_map_t[char]=1+hash_map_t.get(char,0)

        l=0
        r=0
        hash_map_s={}
        for r in range(len(s)):
            hash_map_s[s[r]]=1+hash_map_s.get(s[r],0)
            while all(hash_map_s.get(c, 0) >= hash_map_t[c] for c in hash_map_t):
                if r - l + 1 < len_of_shortest_substring:
                    len_of_shortest_substring = r - l + 1
                    start_index = l
                hash_map_s[s[l]] -= 1
                if hash_map_s[s[l]] == 0:
                    del hash_map_s[s[l]]
                l += 1

        return "" if len_of_shortest_substring == float('inf') else s[start_index:start_index + len_of_shortest_substring]
# @lc code=end

