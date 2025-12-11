# Installation Guide for Zen Music Recommender
This guide provides step-by-step instructions for installing and running the Zen Music Recommender web application on Windows, macOS, and Linux. The application maps a user's heart rate (BPM) to emotional states and recommends music accordingly, providing a lightweight, emotion-aware, and visually engaging experience.

## Prerequisites
Before installing, ensure you have:

1. Python 3.7 or higher installed on your system
2. pip (Python package manager, typically comes with Python)
3. A modern web browser (e.g., Chrome, Safari, Firefox)
4. Administrator/sudo privileges (if installing system-wide packages)

## Installation Steps

### Windows
1. Install Python (if not already installed)
- Download Python from python.org
- During installation, make sure to check "Add Python to PATH"
- Complete the installation
2. Download the project files
- Clone or download the ZIP archive from your repository
- Extract to a directory (e.g., C:\Users\YourName\Zen_Music)
3. Install required dependencies
- Open Command Prompt
- Navigate to your project directory, for example: 
``` cd C:\Users\YourName\Zen_Music```
- install Flask
```pip install flask```
4. Run the application
```python app.py```
- Open your browser and go to http://127.0.0.1:5000

### macOS
1. Install Python (if not already installed)
- Download Python from python.org
2. Download the Zen Music Recommender files. Unzip the project to a folder (e.g., ~/Zen_Music)
3. Install required dependencies
- Open Command Prompt
- Navigate to your project directory, for example: 
``` cd C:\Users\YourName\Zen_Music```
- install Flask
```pip install flask```
4. Run the application
```python app.py```
- Open your browser and go to http://127.0.0.1:5000

### Linux
1. Install Python and pip
```sudo apt update```
```sudo apt install python3 python3-pip```
2. Download the project files
3. Install Flask

```pip3 install flask```
4. Run the server
```python3 app.py```

## Using the Application
1. Enter your BPM (heart rate) between 40–180
2. Receive a music recommendation with synchronized visuals
3. A popup will appear after playback, asking for feedback
4. Click “Yes” or “No”, or dismiss by clicking outside the popup
5. Use the "Stop" button to reset and try again

## Troubleshooting
1. Audio doesn't autoplay	
Solution: Try clicking the page once to activate playback
2. "File not found" errors
Solution: Ensure music/audio files are correctly placed in the static/audio/ dir
3. BPM input rejected
Solution: Only values between 40 and 180 are accepted
4. Port already in use
Solution: Run on another port: flask run --port=5001

## Uninstallation
To uninstall the application: 
1. Delete the project folder
2. Optionally remove Flask if not used elsewhere:
``` pip uninstall flask```

