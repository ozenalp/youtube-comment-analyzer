from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
# Your API key goes here; this is just a sample

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Initialize the YouTube API client
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

# Video ID for which you want to fetch the comments
video_id = "pCQDJQZh_UE"

# Fetch comments
def get_comments(youtube, **kwargs):
    comments = []
    results = youtube.commentThreads().list(**kwargs).execute()
    # print(results)
    items = results['items']
    print(items)
    while results:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        # check if there is a next page
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
            results = youtube.commentThreads().list(**kwargs).execute()
        else:
            break

    return comments

# Fetch and print comments
comments = get_comments(youtube, part="snippet", videoId=video_id, textFormat="plainText")
# for comment in comments:
#     print(comment)