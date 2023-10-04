import praw 
import datetime

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
user_agent = 'YOUR_USER_AGENT'
reddit_username = 'REDDIT_USERNAME'
reddit_password = 'REDDIT_PASSWORD'

subreddits = ['subreddit1', 'subreddit2']  # The subreddits you want to fetch posts from, don't include r/ before the subreddit name.

# example : subreddits = ['science', 'technology', 'maths', 'physics']


def fetch_top_posts(reddit, subreddit):
    top_posts = []
    for submission in reddit.subreddit(subreddit).top('day', limit=10):
        top_posts.append((submission.title, submission.url, submission.author.name))  # Store title, URL, and author's username
    return top_posts

def compile_digest(reddit, subreddits):
    compiled_content = ""
    for subreddit in subreddits:
        top_posts = fetch_top_posts(reddit, subreddit)
        subreddit_url = f"https://www.reddit.com/r/{subreddit}"  
        compiled_content += f"**[{subreddit}](https://www.reddit.com/r/{subreddit}) Top Posts - {datetime.date.today()}**\n\n" 
        for i, (title, url, author) in enumerate(top_posts, start=1):
            compiled_content += f"{i}. [{title}]({url}) by u/{author}\n\n"  
    return compiled_content

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent,
                     username=reddit_username, password=reddit_password)

daily_digest = compile_digest(reddit, subreddits)

subreddit_name = "subreddit_name" # replace with the name of the subreddit the bot will post the digested content to
subreddit = reddit.subreddit(subreddit_name)
submission = subreddit.submit(title=f"Daily Digest - {datetime.date.today()}", selftext=daily_digest)

print(f"Posted to: {submission.url}")
