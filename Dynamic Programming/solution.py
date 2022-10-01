TC: O(nm*min(n,m))
SC: O(nm*min(n,m))

def longestCommonSubsequence(str1, str2):
    # Write your code here.
    result =  [[[] for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    for i in range(1, len(str2) +1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                res = result[i-1][j-1] + [str2[i-1]]
            else:
                res = []
                if len(result[i-1][j])> len(result[i][j-1]):
                    res = result[i-1][j]
                else:
                    res = result[i][j-1]
            result[i][j]  = res
    return result[-1][-1]

# clean code  ->
def longestCommonSubsequence(str1, str2):
    # Write your code here.
    result =  [[[] for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    for i in range(1, len(str2) +1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                result[i][j] = result[i-1][j-1] + [str2[i-1]]
            else:
                result[i][j] = max(result[i-1][j], result[i][j-1], key = len)
    return result[-1][-1]