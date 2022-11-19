class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                candy[i] = candy[i-1]+1
        for i in reversed(range(len(ratings)-1)):
            if ratings[i]>ratings[i+1]:
                candy[i] = max(candy[i+1]+1, candy[i])
        return sum(candy)