import praw
import requests
import os
import re
import time
from tqdm import tqdm
from urllib.parse import urlparse

reddit_username = 'your_reddit_username'
reddit_password = 'your_reddit_password'
reddit_client_id = 'your_client_id'
reddit_client_secret = 'your_client_secret'
reddit_user_agent = 'your_user_agent'

subreddit_name = 'your_subreddit_name'

def download_image(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

        with open(filename, 'wb') as file:
            for data in response.iter_content(chunk_size=block_size):
                progress_bar.update(len(data))
                file.write(data)

        progress_bar.close()

    except Exception as e:
        print(f"Error downloading image: {url}\nError message: {str(e)}")

def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '_', filename)

reddit = praw.Reddit(
    username=reddit_username,
    password=reddit_password,
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent=reddit_user_agent
)

subreddit = reddit.subreddit(subreddit_name)

if not os.path.exists(subreddit_name):
    os.makedirs(subreddit_name)

for submission in subreddit.new(limit=None):
    try:
        if submission.url.endswith(('.jpg', '.jpeg', '.png')):
            img_url = submission.url
            img_extension = os.path.splitext(urlparse(img_url).path)[1]

            if img_extension.lower() not in ['.jpg', '.jpeg', '.png']:
                img_extension = '.jpg'

            img_filename = f"{subreddit_name}_{submission.id}_{submission.title}{img_extension}"
            img_filename = sanitize_filename(img_filename)
            img_path = os.path.join(subreddit_name, img_filename)

            print(f"Downloading image: {img_url}")
            download_image(img_url, img_path)

        time.sleep(2)

    except Exception as e:
        print(f"Error processing submission: {submission.id}\nError message: {str(e)}")

print("Images downloaded successfully.")
