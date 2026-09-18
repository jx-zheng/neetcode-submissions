import heapq

class Twitter:
    MAX_RECENT_TWEETS = 10

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append( (self.time, tweetId) )
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        relevant_tweets = []

        for followed in self.following[userId]:
            relevant_tweets.append(self.tweets[followed])
        relevant_tweets.append(self.tweets[userId])

        total_relevant_tweets = 0
        for relevant_tweet in relevant_tweets:
            total_relevant_tweets += len(relevant_tweet)

        if not total_relevant_tweets:
            return []

        feed_tweet_ids = []
        offsets = [0 for _ in range(len(relevant_tweets))]

        while len(feed_tweet_ids) < min(Twitter.MAX_RECENT_TWEETS, total_relevant_tweets):
            most_recent_tweet = (-1, 0, 0)
            for i, relevant_tweet in enumerate(relevant_tweets):
                if offsets[i] >= len(relevant_tweet):
                    continue
                if relevant_tweet[-1 - offsets[i]][0] > most_recent_tweet[0]:
                    most_recent_tweet = relevant_tweet[-1 - offsets[i]] + (i,)
            feed_tweet_ids.append(most_recent_tweet[1])
            offsets[most_recent_tweet[2]] += 1
        

        return feed_tweet_ids

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
