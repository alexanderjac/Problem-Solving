# backtracking solution
TC: O(n*2^n)
SC: O(n)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()
        def backtrack(index, subset):
            if index ==n:
                res.append(subset[::])
                return
            subset +=[nums[index]]
            backtrack(index+1, subset)
            subset.pop()
            while index+1<n and nums[index]== nums[index+1]:
                index+=1
            backtrack(index+1, subset)
        n = len(nums)
        backtrack(0,[])
        return res


# •	Time complexity: O(n*2 ^ n)
# As we can see in the diagram above, this approach does not generate any duplicate subsets. Thus, in the worst case (array consists of nn distinct elements), the 
# total number of recursive function calls will be 2 ^ n2n. Also, at each function 
# call, a deep copy of the subset currentSubset generated so far is created and 
# added to the subsets list. This will incur an additional O(n)O(n) time (as the 
# maximum number of elements in the currentSubset will be nn). So overall, the time complexity of this approach will be O(n⋅2n).
# •	Space complexity: O(n)
# The space complexity of the sorting algorithm depends on the implementation of 
# each programming language. For instance, in Java, the Arrays.sort() for primitives is implemented as a variant of quicksort algorithm whose space complexity is 
# O(logn). In C++ sort() function provided by STL is a hybrid of Quick Sort,
#  Heap Sort and Insertion Sort with the worst case space complexity of O(logn). 
# Thus the use of inbuilt sort() function adds O(\log n)O(logn) to space complexity. The recursion call stack occupies at most O(n)O(n) space. The output list of subsets is not considered while analyzing space complexity. So, the space complexity of this approach is O(n).



# for loop based recursion
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]
        self.helper(sorted(nums), [],res)
        return res
    def helper(self,nums,curr, res):
        res.append(curr)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                self.helper(nums[i+1:], curr+[nums[i]],res)





# TC: O(n*2^n)
# Here nn is the number of elements present in the given array.
# •	Time complexity: O(n \cdot 2 ^ n)O(n⋅2n)
# At first, we need to sort the given array which adds O(n \log n)O(nlogn) to the 
# time complexity. Next, we use two for loops to create all possible subsets. In 
# the worst case, i.e., with an array of n distinct integers, we will have a total 
# of 2 ^ n2n subsets. Thus the two for loops will add O(2 ^ n)O(2n) to time 
# complexity. Also in the inner loop, we deep copy the previously generated subset 
# before adding the current integer (to create a new subset). This in turn requires 
# the time of order nn as the maximum number of elements in the currentSubset will 
# be at most nn. Thus, the time complexity in the subset generation step using two 
# loops is O(n \cdot 2 ^ n)O(n⋅2n). Thereby, the overall time complexity is
#  O(nlogn+n⋅2n) = O(n . (log n + 2 ^ n)) ~ O(n. 2 ^ n)
# •	Space complexity: O(\log n)O(logn)
# The space complexity of the sorting algorithm depends on the implementation of 
# each programming language. For instance, in Java, the Arrays.sort() for primitives
#  is implemented as a variant of quicksort algorithm whose space complexity is 
# O(\log n)O(logn). In C++ sort() function provided by STL is a hybrid of Quick Sort, 
# Heap Sort and Insertion Sort with the worst case space complexity of O(\log n)O(logn). 
# Thus the use of inbuilt sort() function adds O(\log n)O(logn) to space complexity.
# The space required for the output list is not considered while analyzing space complexity. 
# Thus the overall space complexity in Big O Notation is O(\log n)O(logn).
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        powerset =[[]]
        for i in range(len(nums)):
            if i!=0 and nums[i] == nums[i-1]:
                new_set =[subset + [nums[i]] for subset in new_set ]
            else:
                new_set = [subset +[nums[i]] for subset in powerset]
            powerset+= new_set
        return powerset

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets =[[]]
        for num in nums:
            for i in range(len(subsets)):
                subsets +=[subsets[i]+[num]]
        ans=[]
        for subset in subsets:
            subset = sorted(subset)
            if subset not in ans:
                ans+=[subset]
        return ans