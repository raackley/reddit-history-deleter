import praw
import time
import os

# Read credentials from environment
username = os.environ['RHD_USERNAME']
password = os.environ['RHD_PASSWORD']
client_id = os.environ['RHD_CLIENT_ID']
client_secret = os.environ['RHD_CLIENT_SECRET']

# Get age threshold from environment and convert to seconds
expiration_days = os.environ.get('RHD_EXPIRATION_DAYS', 365) # input age threshold in days, default to a year (365)
expiration_seconds = int(expiration_days) * 60 * 60 * 24  # convert days to seconds

# calculate age threshold in UNIX_TIME
time_now = time.time()
time_threshold = time_now - expiration_seconds

# Log in to Reddit
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent="Python PRAW",
                     username=username)

# Find all comments for user
for comment in reddit.redditor(username).comments.new(limit=None):
    if comment.created_utc < time_threshold:
        comment.delete() # If the created date is less than the threshold, delete it