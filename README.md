# YouTube Downloader Chrome Extension

## Summary

The YouTube Downloader Chrome Extension allows you to download YouTube videos as MP3 files directly from your browser. This tool is designed for ease of use, providing a simple interface to grab the video URL and start the download process quickly.

## Features

- Download YouTube videos in MP3 format.
- Supports playlist downloads.
- User-friendly interface.

## How to Install the Extension in Chrome

1. **Download the Extension Files**:
   - Clone or download the repository to your local machine.

2. **Prepare the Extension**:
   - Navigate to the `dist` folder where your extension files are located.

3. **Load the Extension in Chrome**:
   - Open Chrome and go to `chrome://extensions/`.
   - Enable "Developer mode" by toggling the switch in the top right corner.
   - Click on "Load unpacked".
   - Select the `dist` folder and click "Select".

4. **Usage**:
   - Click on the extension icon in the toolbar.
   - Click the "Get Video Link" button to retrieve the YouTube video URL from the active tab.
   - Once the URL is retrieved, click "Download MP3" to start the download.

## Running the Backend

The backend is built with Flask and uses `yt-dlp` for downloading videos. Follow these instructions to set it up:

### Prerequisites

- Python 3.x installed on your machine.
- `venv` module (comes with Python 3.x).
- `pip` for installing Python packages.

### Setting Up the Backend

1. **Navigate to the Project Directory**:
   ```bash
   cd ~/Documents/WebCrea-Youtube-Extension


2. **Create a Virtual Environment**:
    python3 -m venv venv

3. **Activate the Virtual Environment**:
    source venv/bin/activate

4. **Install Dependencies: Install the required Python packages**:
    pip install Flask flask-cors yt-dlp

5. **Run the Flask App: Start the backend server**:
    python app.py


### Important Notes
- Make sure the Flask backend is running before attempting to use the extension.
- The extension communicates with the backend via HTTP requests to fetch video download links.
- If you encounter any issues, check the browser console for errors and ensure the backend server is operational.

Feel free to customize any part of this `README.md` to better fit your project or preferences!
