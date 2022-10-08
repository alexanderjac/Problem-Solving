
# for loop based backtrack
        
        def backtrack(curr, start):
            if sum(curr)>= target or start>= n:
                if sum(curr) == target :
                    print(curr)
                    res.append(curr[:])
                return
            for i in range(start,n):
                # print(curr)
                curr+=[candidates[i]]
                backtrack(curr, i)
                curr.pop(-1)
        res = []
        n = len(candidates)
        backtrack([], 0)
        return res
# for loop based backtrack without popping
        
        def backtrack(curr, start):
            if sum(curr)>= target or start>= n:
                if sum(curr) == target :
                    res.append(curr[:])
                return
            for i in range(start,n):
                # curr+=[candidates[i]]
                backtrack(curr + [candidates[i]], i)
                # curr.pop(-1)
        res = []
        n = len(candidates)
        backtrack([], 0)
        return res
        
            
        
        # backtrack using recursion
        def helper(curr, index):
            if sum(curr) >=target or index>=n:
                if sum(curr) == target :
                    res.append(curr[::])
                return
            curr += [candidates[index]]
            helper(curr, index)
            if curr: curr.pop(-1)
            helper(curr, index+1)
        n =len(candidates)
        res =[]
        helper(curr = [], index =0)
        return res
			TC: O(N^T/M+1)
			SC: O(T/M)

# Let NN be the number of candidates, TT be the target value, and MM be the minimal value among the candidates.
# •	Time Complexity: O(N^T/M+1)
# o	As we illustrated before, the execution of the backtracking is unfolded as a DFS traversal in a n-ary tree. The total number of steps during the backtracking would be the number of nodes in the tree.
# o	At each node, it takes a constant time to process, except the leaf nodes which could take a linear time to make a copy of combination. So we can say that the time complexity is linear to the number of nodes of the execution tree.
# o	Here we provide a loose upper bound on the number of nodes.
# 	First of all, the fan-out of each node would be bounded to NN, i.e. the total number of candidates.
# 	The maximal depth of the tree, would be \frac{T}{M}MT, where we keep on adding the smallest element to the combination.
# 	As we know, the maximal number of nodes in N-ary tree of \frac{T}{M}MT height would be N^{\frac{T}{M}+1}NMT+1.
# o	Note that, the actual number of nodes in the execution tree would be much smaller than the upper bound, since the fan-out of the nodes are decreasing level by level.
# •	Space Complexity: O(T/M)
# o	We implement the algorithm in recursion, which consumes some additional memory in the function call stack.
# o	The number of recursive calls can pile up to \frac{T}{M}MT, where we keep on adding the smallest element to the combination. As a result, the space overhead of the recursion is \mathcal{O}(\frac{T}{M})O(MT).
# o	In addition, we keep a combination of numbers during the execution, which requires at most \mathcal{O}(\frac{T}{M})O(MT) space as well.
# o	To sum up, the total space complexity of the algorithm would be \mathcal{O}(\frac{T}{M})O(MT).
# o	Note that, we did not take into the account the space used to hold the final results for the space complexity.