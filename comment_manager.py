from comment_downloader import get_comments, get_comments_only
import pandas as pd

from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Initialize the YouTube API client
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

test_video_id = "tLgmrUyfcd4"

def get_video_comments(datafile,video_id):
    output = get_comments(youtube, part="snippet", videoId=video_id, textFormat="plainText",maxResults=100,order="relevance")
    print(1)
    df = pd.DataFrame(output)
    df.to_csv(datafile)

def get_video_comments_only(datafile,video_id):
    output = get_comments_only(youtube, part="snippet", videoId=video_id, textFormat="plainText",maxResults=50,order="relevance")
    print(1)
    df = pd.DataFrame(output)
    df.to_csv(datafile)

def GetVideoCommentsBatch(videoNamesText):
    with open(videoNamesText, 'r') as file:
        csv_data = file.read()
    # Split the CSV data into lines
    videoIDs = csv_data.split('\n')

    # Define the folder path
    folder_path = 'videoComments'

    # Check if the folder exists
    if not os.path.exists(folder_path):
        # Create the folder
        os.makedirs(folder_path)
    for videoID in videoIDs:
        print(videoID)
        get_video_comments_only("videoComments/"+videoID+".csv",videoID)    

# get_video_comments("runereader.csv")
# get_video_comments_only("runereader.csv")
GetVideoCommentsBatch("private/videoIDs.txt")