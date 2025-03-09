# youtube-summerizer
YouTube Video Summary, Translator, English Vocab Tutor (Using YouTube API)

# YouTube Video Summarization & Language Learning using GPT API

## 📌 Project Overview
This project enhances YouTube’s functionality by integrating the YouTube API with GPT-powered features. Users can search for videos based on their favorite celebrities (e.g., Cristiano Ronaldo) and request specific numbers of videos. The system fetches relevant videos and processes them using the GPT API to generate summaries, extract slang, assist in learning languages, and provide meanings for specific words or sentences if required. The processed data is stored in **Snowflake** for future analysis.

## 🚀 Features
- 🔍 **Search & Fetch Videos**: Users can request videos by providing keywords (e.g., a celebrity name) and specifying the number of videos they need.
- 📄 **Summarization**: Generates concise summaries of fetched videos.
- 🗣️ **Slang Extraction**: Identifies and explains slangs used in the videos, helping users improve their English.
- 🌍 **Translation Support**: Converts video content into different languages for better accessibility.
- 📖 **Word & Sentence Meaning**: Provides explanations for specific words or sentences upon request.
- 🤖 **GPT Integration**: Uses OpenAI’s GPT API to process and analyze video transcripts efficiently.
- 💾 **Data Storage**: Stores processed data in **Snowflake** for further analysis and insights.

## 🛠️ Technologies Used
- **YouTube API** - For fetching videos and extracting transcripts.
- **OpenAI GPT API** - For summarization, slang detection, translations, and word/sentence meanings.
- **Python** - Core programming language used for backend processing.
- **Flask/FastAPI** *(Optional)* - To create a simple API for handling user requests.
- **Snowflake** - For storing processed data and enabling future analysis.

## 🔧 Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Up API Keys**  
   - Obtain a YouTube API key from [Google Cloud Console](https://console.cloud.google.com/)
   - Get an OpenAI API key from [OpenAI](https://openai.com/)
   - Store them in a `.env` file:
     ```
     YOUTUBE_API_KEY=your_youtube_api_key
     OPENAI_API_KEY=your_openai_api_key
     ```
4. **Run the Application**
   ```bash
   python app.py
   ```

## 📌 Usage
1. **Search Videos**: Provide a query (e.g., "Cristiano Ronaldo") and request the number of videos.
2. **Process Video Content**: The system fetches video transcripts and processes them with GPT API.
3. **Get Results**:
   - A summary of each video.
   - Extracted slang words and their meanings.
   - Optional translation of the transcript.
   - Explanation of specific words or sentences if requested.

## 🔮 Future Advancements
- **Batch Processing**: Improve efficiency by processing multiple videos in parallel.
- **Database Integration**: Connect with other databases based on user requirements.
- **Multi-Language Support**: Expand translation capabilities to support more languages.
- **Audio Processing**: Enable audio-based transcription and analysis.
- **Sentiment Analysis**: Implement sentiment detection to analyze emotions in videos.
- **Video Processing**: Enhance AI capabilities by analyzing video content beyond transcripts.

## 🤝 Contribution
Feel free to contribute to this project! Fork the repository, make improvements, and submit a pull request.

## 📜 License
This project is licensed under the MIT License.

---
🚀 **Let's enhance language learning with AI-powered YouTube videos!**
