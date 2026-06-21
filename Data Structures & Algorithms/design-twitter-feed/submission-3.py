class Twitter:

    def __init__(self):
        self.twitter = defaultdict(list)
        self.time = 0
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.twitter[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = self.follows[userId]
        follows.add(userId)

        news_feed = []
        res = []
        
        for user in follows:
            idx = len(self.twitter[user]) - 1
            if idx >= 0:
                time_neg, news = self.twitter[user][idx]
                heapq.heappush(news_feed, (time_neg, news, user, idx - 1))

        while news_feed and len(res) < 10:
            _, news, user, idx = heapq.heappop(news_feed)
            res.append(news)
            if idx >= 0:
                time_neg, news = self.twitter[user][idx]
                heapq.heappush(news_feed, (time_neg, news, user, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
