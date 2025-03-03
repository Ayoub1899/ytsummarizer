import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import os

api_key = os.getenv("GOOGLE_API_KEY") #Replace this value with your own Google API key

def get_youtube_transcript(video_id):
    languages = ['en', 'zh-Hans', 'hi', 'es', 'fr', 'ar', 'bn', 'pt', 'ru', 'ur']
    for lang in languages:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
            transcript_text = ' '.join([entry['text'] for entry in transcript])
            return transcript_text, lang
        except NoTranscriptFound:
            continue
        except TranscriptsDisabled:
            return None, "Les sous-titres sont désactivés pour cette vidéo."

    return None, "Aucune transcription disponible dans les 10 langues les plus parlées."

def detect_and_translate(text, api_key):
    """Detects language and translates text to English if necessary."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    try:
        response = model.generate_content(f"Detect the language of the following text and translate it to English if necessary:\n\n{text}")
        return response.text
    except Exception as e:
        print(f"Error in translation: {e}")
        return text  # Return original text if translation fails

def summarize_with_gemini(text, api_key):
    """Summarizes text using Google's Gemini."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    try:
        response = model.generate_content(f"Summarize the following text:\n\n{text}")
        return response.text
    except Exception as e:
        print(f"Error summarizing with Gemini: {e}")
        return None

def summarize_youtube_video(video_url, api_key):
    """Summarizes a YouTube video from its URL."""
    try:
        video_id = video_url.split("v=")[1]
        if "&" in video_id:
            video_id = video_id.split("&")[0]

        transcript = get_youtube_transcript(video_id)
        if transcript:
            translated_text = detect_and_translate(transcript, api_key)
            summary = summarize_with_gemini(translated_text, api_key)
            if summary:
                return summary
            else:
                return "Failed to generate summary."
        else:
            return "Failed to retrieve transcript."

    except IndexError:
        return "Invalid YouTube URL format."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# main function:
def main():
    print("Enter video URL: ")
    video_url = input()
    summary = summarize_youtube_video(video_url, api_key)
    print(summary)

if __name__ == "__main__":
    main()
