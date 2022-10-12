class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        lptr = 0
        longest_sub =0
        for rptr in range(len(s)):
            char = s[rptr]
            freq[char] = freq.get(char,0) +1
            cells_count = rptr - lptr +1
            if cells_count  - max(freq.values())<=k:
                longest_sub = max(longest_sub, cells_count)
            else:
                freq[s[lptr]] -=1
                # if not freq[s[lptr]]:
                #     freq.pop(s[lptr])
                lptr+=1
        return longest_sub
