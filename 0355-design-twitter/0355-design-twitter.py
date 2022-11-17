class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count =0        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -=1
    def getNewsFeed(self, userId: int) -> List[int]:
        
        minHeap = []
        res = []
        self.followers[userId].add(userId)
        for followeeid in self.followers[userId]:
            if followeeid in self.tweets:
                index = len(self.tweets[followeeid]) -1
                count, tweetid = self.tweets[followeeid][index]
                heapq.heappush(minHeap,[count, tweetid ,followeeid,index-1])
        # heapq.heapify(minHeap)
        while minHeap and len(res)<10:
            count, tweetid,followeeid, index = heapq.heappop(minHeap)
            res.append(tweetid)
            if index>=0:
                count, tweetid = self.tweets[followeeid][index]
                heapq.heappush(minHeap,[count, tweetid, followeeid, index-1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)