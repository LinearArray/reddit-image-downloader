# Reddit Image Downloader

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/LinearArray/reddit-image-downloader/blob/main/LICENSE)

## Description

Reddit Image Downloader is a Python script that allows you to fetch and download images from a specified subreddit. It utilizes the PRAW library for accessing the Reddit API and supports downloading images from posts with previews, including both Reddit-hosted and Imgur images.

## Features

- Fetches images from a specified subreddit, processing posts from new to old.
- Downloads images from posts with previews.
- Supports both Reddit-hosted and Imgur images.
- Provides a progress bar during image downloads.
- Generates clean filenames for downloaded images.

## Getting Started

### Prerequisites

- Python 3.x
- Install required dependencies using:

  ```bash
  pip install -r requirements.txt
  ```

### Usage

1. Replace the placeholder values in `main.py` with your Reddit API credentials.
2. Customize the `subreddit_name` variable with the subreddit from which you want to download images.
3. Run the script:

   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PRAW - Python Reddit API Wrapper](https://praw.readthedocs.io/)
- [Requests Library](https://docs.python-requests.org/en/latest/)
- [tqdm - Fast, Extensible Progress Bar](https://tqdm.github.io/)
