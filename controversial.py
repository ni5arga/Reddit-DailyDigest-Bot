import praw 
import datetime
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, REDDIT_USERNAME, REDDIT_PASSWORD, SUBREDDITS, TARGET_SUBREDDIT, TIME_RANGE

def fetch_controversial_posts(reddit, subreddit):
    controversial_posts = []
    for submission in reddit.subreddit(subreddit).controversial(time_filter=TIME_RANGE, limit=10):
        controversial_posts.append((submission.title, submission.url, submission.author.name))
    return controversial_posts

def compile_controversial_digest(reddit):
    compiled_content = ""
    for subreddit in SUBREDDITS:
        controversial_posts = fetch_controversial_posts(reddit, subreddit)
        subreddit_url = f"https://www.reddit.com/r/{subreddit}"  
        compiled_content += f"**[{subreddit}](https://www.reddit.com/r/{subreddit}) Controversial Posts ({TIME_RANGE.capitalize()} range) - {datetime.date.today()}**\n\n" 
        for i, (title, url, author) in enumerate(controversial_posts, start=1):
            compiled_content += f"{i}. [{title}]({url}) by u/{author}\n\n"  
    return compiled_content

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT,
                     username=REDDIT_USERNAME, password=REDDIT_PASSWORD)

controversial_digest = compile_controversial_digest(reddit)

target_subreddit = TARGET_SUBREDDIT
subreddit = reddit.subreddit(target_subreddit)
submission = subreddit.submit(title=f"Controversial Digest - {datetime.date.today()}", selftext=controversial_digest)

print(f"Posted to: {submission.url}")
