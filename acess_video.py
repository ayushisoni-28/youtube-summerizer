import streamlit as st
import os
import time
import logging
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import openai
import snowflake.connector
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Snowflake configuration
sf_user = 'your_user'           # Snowflake username
sf_password = 'your_password'   # Snowflake password
sf_account = 'your_account'     # Snowflake account identifier
sf_warehouse = 'your_warehouse' # Snowflake warehouse name
sf_database = 'your_database'   # Snowflake database name
sf_schema = 'your_schema'       # Snowflake schema name

# YouTube API Key
api_key = 'YOUTUBE_API_KEY'

# Set OpenAI API key using environment variable
openai.api_key = os.getenv('CHATGPT_API_KEY')

# Build the YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Snowflake connection setup
def create_snowflake_connection():
    conn = snowflake.connector.connect(
        user=sf_user,
        password=sf_password,
        account=sf_account,
        warehouse=sf_warehouse,
        database=sf_database,
        schema=sf_schema
    )
    return conn

# Function to get the transcript for a given video ID
def get_video_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return transcript
    except Exception as e:
        logging.error(f"Error fetching transcript for video {video_id}: {str(e)}")
        return None

# Function to format the transcript as plain text
def format_transcript(transcript):
    formatter = TextFormatter()
    return formatter.format_transcript(transcript)

# Function to summarize text using ChatGPT
def summarize_transcript(transcript_text, user_requirement):
    try:
        logging.info("Summarizing transcript using ChatGPT API...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[ 
                {"role": "system", "content": "You are an assistant that summarizes YouTube transcripts based on user requirements."},
                {"role": "user", "content": f"Summarize the following transcript according to this requirement: {user_requirement}\n\n{transcript_text}"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        logging.error(f"Error summarizing transcript: {str(e)}")
        return "Summary not available."

# Function to search YouTube for videos based on a query
def search_youtube(query, max_results=10):
    try:
        request = youtube.search().list(
            part='id,snippet',
            q=query,
            type='video',
            maxResults=max_results,
            order='rating'
        )
        response = request.execute()
        return response['items']
    except Exception as e:
        logging.error(f"Error searching for videos: {str(e)}")
        return []

# Function to sanitize file name
def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

# Function to generate summary content dynamically
def generate_summary_content(title, transcript, summary):
    content = f"Title: {title}\n\n"
    content += "Transcript:\n"
    content += transcript + "\n\n"
    content += "Summary:\n"
    content += summary
    return content

# Function to store video data in Snowflake
def store_in_snowflake(video_id, title, link, transcript, summary):
    conn = create_snowflake_connection()
    cursor = conn.cursor()
    try:
        query = f"""
            INSERT INTO youtube_data (video_id, title, link, transcript, summary)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (video_id, title, link, transcript, summary))
        conn.commit()
        logging.info(f"Video data for {title} inserted into Snowflake.")
    except Exception as e:
        logging.error(f"Error inserting video data into Snowflake: {str(e)}")
    finally:
        cursor.close()
        conn.close()

# Streamlit app definition
st.set_page_config(page_title="TalkTube Wizard", layout="wide")

# Centered header without color
st.markdown(
    """<h1 style="text-align:center;font-family:Trebuchet MS;">TalkTube Wizard</h1>""", 
    unsafe_allow_html=True
)

# Sidebar customization
st.sidebar.header("Search & Summarization Options")
query = st.sidebar.text_input("Enter the search query:")
max_results = st.sidebar.number_input("Number of videos to process:", min_value=1, max_value=50, value=1)
user_requirement = st.sidebar.text_area("Enter summarization requirement:")

# Session state initialization
if "video_details" not in st.session_state:
    st.session_state.video_details = []

if st.sidebar.button("Fetch and Process Videos"):
    if not query or not user_requirement:
        st.sidebar.error("Please enter both the search query and summarization requirement.")
    else:
        with st.spinner("Searching for videos on YouTube..."):
            videos = search_youtube(query, max_results=50)

        if not videos:
            st.error("No videos found for the given query.")
        else:
            st.info("Processing videos and fetching transcripts...")
            video_details = []
            processed_videos = 0

            for item in videos:
                if processed_videos >= max_results:
                    break

                video_id = item['id']['videoId']
                title = item['snippet']['title']
                link = f"https://www.youtube.com/watch?v={video_id}"

                # Fetch transcript
                transcript = get_video_transcript(video_id)

                if transcript:
                    formatted_transcript = format_transcript(transcript)
                    summary = summarize_transcript(formatted_transcript, user_requirement)

                    # Store data in Snowflake
                    store_in_snowflake(video_id, title, link, formatted_transcript, summary)

                    video_details.append({
                        'title': title,
                        'link': link,
                        'transcript': formatted_transcript,
                        'summary': summary
                    })

                    processed_videos += 1

                time.sleep(2)

            st.success("All videos have been processed.")
            
            # Save video details to session state
            st.session_state.video_details = video_details

# Display videos and summaries from session state
for video in st.session_state.video_details:
    st.subheader(video['title'])
    st.video(video['link'])
    st.write(f"**Summary:** {video['summary']}")

    # Option to download the summary with a unique key for each button
    content = generate_summary_content(video['title'], video['transcript'], video['summary'])
    file_name = f"{sanitize_filename(video['title'])}_summary.txt"

    if not content:
        st.warning("No content available for download.")
    else:
        st.download_button(
            label="Download Summary", 
            data=content,
            file_name=file_name,
            mime="text/plain",
            use_container_width=True
        )

    st.write("---")
