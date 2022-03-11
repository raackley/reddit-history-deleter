import praw
import time
import os

# Read credentials from environment
username = os.environ['RHD_USERNAME']
password = os.environ['RHD_PASSWORD']
client_id = os.environ['RHD_CLIENT_ID']
client_secret = os.environ['RHD_CLIENT_SECRET']

# read and set delete mode, default to True
rhd_mode = os.environ.get('RHD_MODE', "delete")

# read and set the overwrite message, default to "DELETED"
overwite_message = os.environ.get('RHD_OVERWRITE_MESSAGE', "DELETED")

# Get age threshold from environment and convert to seconds
# input age threshold in days, default to a year (365)
expiration_days = os.environ.get('RHD_EXPIRATION_DAYS', 365)
# convert days to seconds
expiration_seconds = int(expiration_days) * 60 * 60 * 24

# calculate age threshold in UNIX_TIME
time_now = time.time()
time_threshold = time_now - expiration_seconds

# Log in to Reddit
try:
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         password=password,
                         user_agent="Python PRAW",
                         username=username)
    print("Logged in as: ", reddit.user.me())
    reddit.validate_on_submit = True
except Exception:
    print("ERROR: Could not log in.")
    exit(1)

# Find all comments for user
for comment in reddit.redditor(username).comments.new(limit=None):
    time.sleep(1)  # sleep to avoid rate limiting
    # If the created date is less than the threshold, delete it
    if comment.created_utc < time_threshold:
        if (rhd_mode == "delete"):
            comment.delete()
            print("Deleted comment.")
        elif (rhd_mode == "overwrite"):
            comment.edit(overwite_message)
            print("Overwrote comment.")

# Find all submissions for user
for submission in reddit.redditor(username).submissions.new(limit=None):
    time.sleep(1)  # sleep to avoid rate limiting
    # If the created date is less than the threshold, delete it
    if submission.created_utc < time_threshold:
        if (rhd_mode == "delete"):
            submission.delete()
            print("Deleted submission.")
        elif (rhd_mode == "overwrite"):
            submission.edit(overwite_message)
            print("Overwrote submission.")
