from flask import Flask, render_template, request, jsonify
from main import summarize_youtube_video
import os

app = Flask(__name__)
api_key = os.getenv("GOOGLE_API_KEY") #Create your own environment variable with your own google API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    video_url = request.form.get('video_url')
    if not video_url:
        return jsonify({'error': 'No video URL provided'}), 400

    summary = summarize_youtube_video(video_url, api_key)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
