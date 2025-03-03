# YouTube Video Summarizer

This is a simple web application that takes a YouTube video URL and generates a concise summary of its content. The app uses Flask for the backend and a modernized frontend with HTML, TailwindCSS, and JavaScript.

## Features

- Clean and modern user interface
- Real-time video embedding
- Elegant loading spinner animation
- Responsive design

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML, TailwindCSS, JavaScript
- **API:** Google API (e.g., YouTube Data API)

## Prerequisites

- Python 3.8+
- Flask
- Google API Key (for accessing YouTube data)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your Google API key:

```
GOOGLE_API_KEY=your_google_api_key
```

5. Make sure your `.env` file is in `.gitignore`:

```
.env
```

## Usage

1. Start the Flask application:

```bash
flask run
```

2. Open your browser and go to:

```
http://127.0.0.1:5000/
```

3. Enter a YouTube video URL, click the **Summarize** button, and watch the video and summary appear below!

## Project Structure

```
.
├── main.py                    # Function to summarize YouTube videos
├── app.py                     # Flask application
├── templates
│   └── index.html             # Frontend interface
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Contributing

Feel free to fork the repo and submit pull requests! Suggestions and improvements are always welcome.

