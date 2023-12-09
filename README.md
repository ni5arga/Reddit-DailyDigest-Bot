# Reddit Daily Digest Bot

**Reddit Daily Digest Bot** is a Python bot designed to simplify the process of aggregating and sharing top posts from your favorite subreddits. It fetches the most popular posts from specified subreddits, compiles them into a neatly formatted daily digest, and automatically posts the digest to a target subreddit of your choice.

## Key Features

- Fetch top posts from multiple subreddits.
- Compile top posts into a daily digest with post titles, links and author (i'll add more stuff soon)
- Post the daily digest to a designated subreddit with ease.

## Getting Started

### Prerequisites

You'll need to have the following installed on your system:

- Python 3.x

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ni5arga/reddit-dailydigest-bot.git
   ```
2. Change the project directory

   ```bash
   cd reddit-dailydigest-bot
   ```

3. Install Dependencies
   ```bash
    pip install -r requirements.txt
   ```

### Configuration 
### Reddit API Credentials

Open the `config.py` file and replace the placeholders with your Reddit API credentials:

```python
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
USER_AGENT = 'your_user_agent'
REDDIT_USERNAME = 'your_reddit_username'
REDDIT_PASSWORD = 'your_reddit_password'
```

### Subreddits 
Modify the `SUBREDDITS` variable in `config.py` to specify the subreddits from which you want to fetch posts. Don't include r/ before the name of the subreddit.

```python
SUBREDDITS = ['science', 'technology', 'maths', 'physics']
```

### Target Subreddit 
Replace the `TARGET_SUBREDDIT` variable with the subreddit name where you want the bot to post the content:

```python
TARGET_SUBREDDIT = 'your_target_subreddit_name'
```
### Time Range
Update the `TIME_RANGE` to the time range you need for the `controversial.py` and `top.py` script
```python
TIME_RANGE = 'day' 
```
-`'day'`: Fetch top posts from the last 24 hours.
-`'week'`: Fetch top posts from the last 7 days.
-`'month'`: Fetch top posts from the last 30 days.
-`'year'`: Fetch top posts from the last 365 days.
-`'all'`: Fetch top posts from all time.

This won't affect the `main.py` script or any other script as they are intended to work on the basis of daily posts.

### Usage
After configuring it properly simply run the bot script :
```bash 
py main.py
```
The bot will fetch that day's top posts from the specified subreddits, compile them into a daily digest, and post it to the target subreddit.

### Auto-running the script

To make your Reddit Daily Digest Bot run automatically every 24 hours, you can use a scheduler like `cron` (on Unix-like systems) or Task Scheduler (on Windows). Here's how you can set up the automatic scheduling :

**Automate Script Execution Every 24 Hours**

1. **Linux/macOS (Using `cron`)**:

   - Open your terminal.
   - Open your crontab file for editing by running:

     ```bash
     crontab -e
     ```

   - Add the following line to schedule your script to run every 24 hours:

     ```bash
     0 0 * * * /usr/bin/python3 /path/to/your/reddit-dailydigest-bot/main.py
     ```

   - Save the file and exit.

2. **Windows (Using Task Scheduler)**:

   - Open the "Task Scheduler" application.
   - In the right-hand pane, click on "Create Basic Task...".
   - Follow the wizard to create a basic task, specifying the task name and description.
   - Choose "Daily" and set the recurrence to "1 days".
   - Specify the start date and time.
   - Choose "Start a program" and browse to the location of your Python executable (e.g., `C:\Python39\python.exe`).
   - In the "Add arguments" field, provide the full path to your `main.py` script (e.g., `C:\path\to\your\reddit-dailydigest-bot\main.py`).
   - Complete the wizard, review your settings, and click "Finish" to create the scheduled task.

**Ensure Proper Environment Setup**

Make sure that your Python environment and working directory are properly set within your script to avoid any issues when it runs as a scheduled task.

**Testing and Troubleshooting**

Before scheduling the script to run automatically, test it manually to ensure it works as expected. Check the logs or output to identify and fix any issues.

### Contributing

Contributions are welcome! If you'd like to contribute to this project, please open an issue or submit a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](/License) file for details.



