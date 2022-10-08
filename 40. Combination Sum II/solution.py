#for loop based with counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(comb, remain, curr, counter):
            if remain == 0:
                result.append(list(comb))
            elif remain<0:
                return
            for next_curr in range(curr, len(counter)):
                candidate , freq = counter[next_curr]
                if freq<=0:
                    continue
                comb.append(candidate)
                counter[next_curr]= (candidate, freq -1)
                backtrack(comb, remain -candidate, next_curr, counter)
                counter[next_curr] = (candidate, freq)
                comb.pop()
        counter =Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        backtrack([],target, 0, counter)
        return result

#     TC: O(2^N) 
# 	In the worst case our algorithm will exhaust all possible combinations from the input array. Again, in the worst case, let us assume that each number is unique. Additionally it takes O(N) time to build a counter table out of the input array.
# SC: O(N
#   We first build a counter table which consume O(N) space. comb consume again O(N)

#for loop based
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack( index, curr):
            if sum(curr) == target:
                result.append(curr[::])
                return
            if sum(curr)>target:
                return
            for next_index in range(index, len(candidates)):
                if next_index>index and candidates[next_index]== candidates[next_index -1]:
                    continue
                else:
                    backtrack(next_index+1, curr+[candidates[next_index]])
        backtrack( 0, [])
        return result


TC: O(2^N)
In the worst case it would exhaust all possible combinations from the input array that would be O(N)
The sorting would be O(NlogN)
SC: O(N)


# without forloop
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def helper(curr, index):
            if sum(curr) >= target or index >= n:
                if sum(curr) == target: res.append(curr[:])
                return
            curr += [candidates[index] ]
            helper(curr, index+1)
            curr.pop(-1)
            while index +1 < n and candidates[index] == candidates[index+1]:
                index+=1
            helper(curr, index+1)
        n = len(candidates)
        helper([] , 0)
        return res