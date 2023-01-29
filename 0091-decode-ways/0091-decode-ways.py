class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0': # invalud str must return 0
            return 0
        two_p_back = 1
        one_p_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i]!='0':
                current = one_p_back # making sure 0 case count
            last_two_digit = int(s[i-1:i+1]) # taking current digit n prev digit
            # 326 -> 32(invalid) | 3,26 (valid) | 3,2,6 (valid)
            if 10<= last_two_digit <= 26 :
                current += two_p_back # as last two digits are valid, it has to add all possibilities of last two pointers back
            two_p_back = one_p_back # now this one pointer back will move, and becomes two
            one_p_back = current
        return one_p_back