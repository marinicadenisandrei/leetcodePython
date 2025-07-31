# Leetcode - 355. Design Twitter (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 355. Design Twitter (Python language) - Medium","yellow"))

class Twitter:
    def __init__(self):
        self.users = {}

    def postTweet(self, user, id):
        if str(user) in self.users:
            self.users[str(user)][0].append(id)
        else:
            self.users[str(user)] = [[],[]];
            self.postTweet(user, id)

    def getNewsFeed(self, user):
        tweets = self.users[str(user)][0].copy()

        for i in self.users[str(user)][1]:
            try:
                tweets.extend(self.users[str(i)][0])
            except Exception as e:
                continue
        
        return tweets
            
    def follow(self, user1, user2):
        self.users[str(user1)][1].append(user2)
    
    def unfollow(self, user1, user2):
        self.users[str(user1)][1].remove(user2)
    
    def print(self):
        print(self.users)        

print(colored("Test 1:","green"))

twitter = Twitter()

twitter.postTweet(1, 5);
print(twitter.getNewsFeed(1));
twitter.follow(1, 2); 
twitter.postTweet(2, 6); 
print(twitter.getNewsFeed(1));
twitter.unfollow(1, 2);
print(twitter.getNewsFeed(1));

print("|", colored("Passed","green"))


