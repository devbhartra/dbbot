import praw
import json

def get_keys(path):
    with open(path) as f:
        return json.load(f)

keys = get_keys("/home/dev/.secret/reddit_creds.json")
# Create the Reddit instance 
reddit = praw.Reddit(
    client_id = keys['client_id'],
    client_secret =  keys['client_secret'],
    username = keys['username'],
    password = keys['password'],
    user_agent = keys['user_agent'])  #not readonly

# print("pass =", keys['password'])

subreddit = reddit.subreddit('TIFU')

hot_sub = subreddit.hot(limit = 1)

for post in hot_sub:
    if not post.stickied:
        print(print(post.title))
        post.comments.replace_more(limit=0) # flatten tree
        comments = post.comments
        for comment in comments:
            print(20*'-')
            print("Parent Comment: ",comment.body,"\n")
            if len(comment.replies) > 0:
                for reply in comment.replies:
                    print('REPLY: ', reply.body)