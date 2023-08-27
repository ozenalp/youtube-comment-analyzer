import streamlit as st
# Import your custom library
import comment_downloader

from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Initialize the YouTube API client
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)


def main():
    st.title("Video URL Processor")

    # Create a text box for video URL input
    video_url = st.text_input("Enter the video URL:", "")

    # Create a button to submit the video URL
    if st.button("Submit"):
        # Display a loading spinner while processing the request
        with st.spinner("Processing the video URL..."):
            # Call your custom library function to process the video URL
            # output = process_video_url(video_url)
            output = comment_downloader.get_comments(youtube, part="snippet", videoId=video_url, textFormat="plainText",maxResults=20,order="relevance")

            # Display the output
            st.write(f"Processed Output: {video_url}")
            st.write(f"Fetched comment count: {len(output)}")
            for comment in output:
                # print(output['comment'])
                st.write(f"Processed Output: {comment['comment']}")
            st.write(f"Processed Output: {output[0]['comment']}")

if __name__ == "__main__":
    main()