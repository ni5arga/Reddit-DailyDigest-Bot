import praw 
import datetime
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, REDDIT_USERNAME, REDDIT_PASSWORD, SUBREDDITS, TARGET_SUBREDDIT

def fetch_rising_posts(reddit, subreddit):
    rising_posts = []
    for submission in reddit.subreddit(subreddit).rising(limit=10):
        rising_posts.append((submission.title, submission.url, submission.author.name))
    return rising_posts

def compile_rising_digest(reddit):
    compiled_content = ""
    for subreddit in SUBREDDITS:
        rising_posts = fetch_rising_posts(reddit, subreddit)
        subreddit_url = f"https://www.reddit.com/r/{subreddit}"  
        compiled_content += f"**[{subreddit}](https://www.reddit.com/r/{subreddit}) Rising Posts - {datetime.date.today()}**\n\n" 
        for i, (title, url, author) in enumerate(rising_posts, start=1):
            compiled_content += f"{i}. [{title}]({url}) by u/{author}\n\n"  
    return compiled_content

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT,
                     username=REDDIT_USERNAME, password=REDDIT_PASSWORD)

rising_digest = compile_rising_digest(reddit)

target_subreddit = TARGET_SUBREDDIT
subreddit = reddit.subreddit(target_subreddit)
submission = subreddit.submit(title=f"Rising Digest - {datetime.date.today()}", selftext=rising_digest)

print(f"Posted to: {submission.url}")
