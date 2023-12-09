import praw 
import datetime
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, REDDIT_USERNAME, REDDIT_PASSWORD, SUBREDDITS, TARGET_SUBREDDIT, TIME_RANGE

def fetch_top_posts(reddit, subreddit):
    top_posts = []
    for submission in reddit.subreddit(subreddit).top(TIME_RANGE, limit=10):
        top_posts.append((submission.title, submission.url, submission.author.name))
    return top_posts

def compile_digest(reddit):
    compiled_content = ""
    for subreddit in SUBREDDITS:
        top_posts = fetch_top_posts(reddit, subreddit)
        subreddit_url = f"https://www.reddit.com/r/{subreddit}"  
        compiled_content += f"**[{subreddit}](https://www.reddit.com/r/{subreddit}) Top Posts - {datetime.date.today()}**\n\n" 
        for i, (title, url, author) in enumerate(top_posts, start=1):
            compiled_content += f"{i}. [{title}]({url}) by u/{author}\n\n"  
    return compiled_content

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT,
                     username=REDDIT_USERNAME, password=REDDIT_PASSWORD)

daily_digest = compile_digest(reddit)

target_subreddit = TARGET_SUBREDDIT
subreddit = reddit.subreddit(target_subreddit)
submission = subreddit.submit(title=f"Top Digest - {datetime.date.today()} ({TIME_RANGE} range)", selftext=daily_digest)

print(f"Posted to: {submission.url}")
