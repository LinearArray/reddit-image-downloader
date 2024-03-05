import praw
import requests
import os
import re
from tqdm import tqdm
from urllib.parse import urlparse, parse_qs

reddit_client_id = 'your_client_id'
reddit_client_secret = 'your_client_secret'
reddit_user_agent = 'your_user_agent'

subreddit_name = 'your_subreddit_name'

def download_image(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

    with open(filename, 'wb') as file:
        for data in response.iter_content(chunk_size=block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()

def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '_', filename)

reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent=reddit_user_agent
)

subreddit = reddit.subreddit(subreddit_name)

if not os.path.exists(subreddit_name):
    os.makedirs(subreddit_name)

for submission in subreddit.new(limit=None):
    if hasattr(submission, 'preview') and submission.preview:
        images = submission.preview['images']
        for i, image in enumerate(images):
            img_url = image['source']['url']
            img_extension = os.path.splitext(urlparse(img_url).path)[1]
            
            # Ensure the extension is a common image format
            if img_extension.lower() not in ['.jpg', '.jpeg', '.png']:
                img_extension = '.jpg'  # Default to jpg if not recognized
            
            img_filename = f"{subreddit_name}_{submission.id}_{i+1}{img_extension}"
            img_filename = sanitize_filename(img_filename)
            img_path = os.path.join(subreddit_name, img_filename)
            print(f"Downloading image: {img_url}")
            download_image(img_url, img_path)

print("Images downloaded successfully.")
