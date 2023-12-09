import praw 
import datetime
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, REDDIT_USERNAME, REDDIT_PASSWORD, SUBREDDITS, TARGET_SUBREDDIT

def fetch_hot_posts(reddit, subreddit):
    hot_posts = []
    for submission in reddit.subreddit(subreddit).hot(limit=10):
        hot_posts.append((submission.title, submission.url, submission.author.name))
    return hot_posts

def compile_hot_digest(reddit):
    compiled_content = ""
    for subreddit in SUBREDDITS:
        hot_posts = fetch_hot_posts(reddit, subreddit)
        subreddit_url = f"https://www.reddit.com/r/{subreddit}"  
        compiled_content += f"**[{subreddit}](https://www.reddit.com/r/{subreddit}) Hot Posts - {datetime.date.today()}**\n\n" 
        for i, (title, url, author) in enumerate(hot_posts, start=1):
            compiled_content += f"{i}. [{title}]({url}) by u/{author}\n\n"  
    return compiled_content

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT,
                     username=REDDIT_USERNAME, password=REDDIT_PASSWORD)

hot_digest = compile_hot_digest(reddit)

target_subreddit = TARGET_SUBREDDIT
subreddit = reddit.subreddit(target_subreddit)
submission = subreddit.submit(title=f"Hot Digest - {datetime.date.today()}", selftext=hot_digest)

print(f"Posted to: {submission.url}")
