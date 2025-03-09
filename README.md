# youtube-summerizer
 YouTube Video Summary, Translator, English Vocab Tutor (Using YouTube API)

# YouTube Video Summarization & Language Learning using GPT API

## 📌 Project Overview
This project enhances YouTube’s functionality by integrating the YouTube API with GPT-powered features. Users can search for videos based on their favorite celebrities (e.g., Cristiano Ronaldo) and request specific numbers of videos. The system fetches relevant videos and processes them using the GPT API to generate summaries, extract slang, and assist in learning languages.

## 🚀 Features
- 🔍 **Search & Fetch Videos**: Users can request videos by providing keywords (e.g., a celebrity name) and specifying the number of videos they need.
- 📄 **Summarization**: Generates concise summaries of fetched videos.
- 🗣️ **Slang Extraction**: Identifies and explains slangs used in the videos, helping users improve their English.
- 🌍 **Translation Support**: Converts video content into different languages for better accessibility.
- 🤖 **GPT Integration**: Uses OpenAI’s GPT API to process and analyze video transcripts efficiently.

## 🛠️ Technologies Used
- **YouTube API** - For fetching videos and extracting transcripts.
- **OpenAI GPT API** - For summarization, slang detection, and translations.
- **Python** - Core programming language used for backend processing.
- **Flask/FastAPI** *(Optional)* - To create a simple API for handling user requests.

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

## 🤝 Contribution
Feel free to contribute to this project! Fork the repository, make improvements, and submit a pull request.

## 📜 License
This project is licensed under the MIT License.

---
🚀 **Let's enhance language learning with AI-powered YouTube videos!**

 
