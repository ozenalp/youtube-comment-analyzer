from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Initialize the YouTube API client
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

# Video ID for which you want to fetch the comments
video_id = "tLgmrUyfcd4"

# Fetch comments
def get_comments(youtube, **kwargs):
    comments = []
    commentsWithData=[]
    results = youtube.commentThreads().list(**kwargs).execute()
    # print(results)
    items = results['items']
    # print(items)
    print(items[0])

    while results:
        for item in items:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            likeCount = item['snippet']['topLevelComment']['snippet']['likeCount']
            publishDate = item['snippet']['topLevelComment']['snippet']['publishedAt']
            commentData = {}
            commentData['comment']=comment
            commentData['likeCount']=likeCount
            commentData['publishDate']=publishDate

            commentsWithData.append(commentData)
            comments.append(comment)

        # check if there is a next page
        # if 'nextPageToken' in results:
        #     kwargs['pageToken'] = results['nextPageToken']
        #     results = youtube.commentThreads().list(**kwargs).execute()
        # else:
        #     break
        break

    return commentsWithData

def get_comments_only(youtube, **kwargs):
    comments = []
    commentsWithData=[]
    results = youtube.commentThreads().list(**kwargs).execute()
    # print(results)
    items = results['items']
    # print(items)
    print(items[0])

    while results:
        for item in items:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            likeCount = item['snippet']['topLevelComment']['snippet']['likeCount']
            publishDate = item['snippet']['topLevelComment']['snippet']['publishedAt']
            commentData = {}
            commentData['comment']=comment
            commentData['likeCount']=likeCount
            commentData['publishDate']=publishDate

            commentsWithData.append(commentData)
            comments.append(comment)

        # check if there is a next page
        # if 'nextPageToken' in results:
        #     kwargs['pageToken'] = results['nextPageToken']
        #     results = youtube.commentThreads().list(**kwargs).execute()
        # else:
        #     break
        break

    return comments

if __name__ == "__main__":
    # Fetch and print comments
    comments = get_comments(youtube, part="snippet", videoId=video_id, textFormat="plainText")
    print(comments[0]['comment'],"Like count: "+str(comments[0]['likeCount']),"Publish date: "+comments[0]['publishDate'] )
    # for comment in comments:
    #     print(comment)
