# config.py (for configuring the daily digest bot)

CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
USER_AGENT = 'your_user_agent'
REDDIT_USERNAME = 'your_reddit_username'
REDDIT_PASSWORD = 'your_reddit_password'

SUBREDDITS = ['subreddit1', 'subreddit2'] # Subreddits to fetch from, don't include r/ before the subreddit name. Example: ['science', 'technology', 'maths', 'physics']
TARGET_SUBREDDIT = 'your_target_subreddit_name' # Name of the subreddit to the bot will post the digested content to
TIME_RANGE = 'day' # 'day', 'week', 'month', 'year', 'all'
# TIME_RANGE only works for the top.py, controversial.py script.