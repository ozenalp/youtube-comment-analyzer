from comment_downloader import get_comments
import pandas as pd

from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Initialize the YouTube API client
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

video_id = "tLgmrUyfcd4"

def get_video_comments(datafile):
    output = get_comments(youtube, part="snippet", videoId=video_id, textFormat="plainText",maxResults=100,order="relevance")
    print(1)
    df = pd.DataFrame(output)
    df.to_csv(datafile)

def get_video_comments_only(datafile):
    output = get_video_comments_only(youtube, part="snippet", videoId=video_id, textFormat="plainText",maxResults=100,order="relevance")
    print(1)
    df = pd.DataFrame(output)
    df.to_csv(datafile)

# get_video_comments("runereader.csv")
get_video_comments_only("runereader.csv")