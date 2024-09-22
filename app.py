from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/download', methods=['GET'])
def download():
    video_url = request.args.get('url')
    
    # Only allow mp3 format
    format = 'mp3'
    
    # Determine the user's Downloads directory based on the OS
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    save_directory = os.path.join(downloads_path, "webcrea-downloader")
    os.makedirs(save_directory, exist_ok=True)

    # Define the output filename based on video title
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(save_directory, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format,
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return jsonify({'message': 'File downloaded successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
