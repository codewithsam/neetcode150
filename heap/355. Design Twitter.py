from collections import deque
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.user_tweets:dict[int, deque] = {} 
        self.user_followers:dict[int, set] = {}
        self.count = 0
        self.limit = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        if userId not in self.user_tweets:
            self.user_tweets[userId] = deque()
        self.user_tweets[userId].append((-1*self.count, tweetId))
        if len(self.user_tweets[userId]) > self.limit:
            self.user_tweets[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []
        users = [userId]
        if userId in self.user_followers:
            users.extend(self.user_followers[userId])
        for user in users:
            if user in self.user_tweets and self.user_tweets[user]:
                tweet = self.user_tweets[user][-1]
                heapq.heappush(max_heap, (tweet[0], tweet[1], user, -1))
        while len(res) < self.limit and max_heap:
            _,tweetId,userId,idx = heapq.heappop(max_heap)
            tweetQ = self.user_tweets[userId]
            res.append(tweetId)
            if (-1*idx) < len(tweetQ):
                next = tweetQ[idx-1]
                heapq.heappush(max_heap, (next[0], next[1], userId, idx-1))
        return res
            

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId not in self.user_followers:
            self.user_followers[followerId] = set()
        if followeeId not in self.user_followers[followerId]:
            self.user_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_followers and followeeId in self.user_followers[followerId]:
            self.user_followers[followerId].remove(followeeId)

twitter = Twitter()

twitter.postTweet(1,11)
twitter.postTweet(1,12)
twitter.postTweet(3,31)
twitter.postTweet(1,13)
twitter.postTweet(2,21)
twitter.postTweet(3,32)
twitter.postTweet(1,14)
twitter.postTweet(3,33)
twitter.postTweet(1,15)
twitter.postTweet(3,34)
twitter.postTweet(3,35)
twitter.postTweet(3,36)
twitter.postTweet(2,23)
twitter.postTweet(3,37)
twitter.postTweet(1,16)
twitter.postTweet(2,22)
twitter.postTweet(3,38)
twitter.postTweet(3,39)
twitter.follow(1,2) 
print(twitter.getNewsFeed(1)) # 22,16,23,15,14,21,13,12,11
twitter.follow(1,3)
print(twitter.getNewsFeed(1)) # 39,38,22,16,37,23,36,35,34,15
twitter.postTweet(2,28)
twitter.postTweet(1,19)

twitter.unfollow(1,3)
print(twitter.getNewsFeed(1)) # 19,28,16,23,15,14,21,13,12,11,


