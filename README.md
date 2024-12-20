# JARVIS-PERSONAL-VIRTUAL-ASSISTANT
Jarvis is a Python-based voice assistant that performs tasks like Wikipedia searches, opening websites, playing music and movies, adjusting volume, and sending WhatsApp messages—all through simple voice commands. Designed for convenience and efficiency, Jarvis is a versatile tool for daily tasks.


## Features

- **Greeting**: Wishes the user based on the time of day.
- **Wikipedia Search**: Retrieves summaries for specified topics from Wikipedia.
- **Open Websites**: Opens popular websites like YouTube, Google, and Stack Overflow.
- **Date and Time**: Provides the current date and time on request.
- **Launch Applications**: Opens Visual Studio Code for coding.
- **Play Music**: Plays a random song from a specified directory.
- **Play Movies**: Plays a random movie from a specified directory.
- **Set System Volume**: Adjusts the system volume to a specified percentage.
- **Send WhatsApp Messages**: Schedules a WhatsApp message to be sent to a specified contact.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Adnan41663shah/JARVIS-PERSONAL-VIRTUAL-ASSISTANT.git
    ```

2. Install the required packages:
    ```bash
    pip install pyttsx3 SpeechRecognition wikipedia pywhatkit pycaw comtypes
    ```

3. Ensure that Python and all required dependencies are installed.

## Usage

1. Run the script:
    ```bash
    python jarvis.py
    ```
2. Jarvis will greet you and await your commands. You can ask it to:
   - Search for information on Wikipedia by saying "search [topic] on Wikipedia."
   - Open websites, for example, "open YouTube."
   - Check the date and time by asking, "what is the time?" or "what is the date?"
   - Play music or movies.
   - Set the system volume by saying "set volume to [percentage]."
   - Send a WhatsApp message by saying, "send WhatsApp message to [contact name]."

## Configuration

- **Music and Movie Paths**: Update `music_dir` and `movie_dir` variables in the code to point to your preferred directories for music and movies.
- **Application Paths**: Update `code_path` with the path to your preferred text editor or IDE.
- **WhatsApp Contacts**: Ensure the names used in the `send_whatsapp_message` function match the contact names in your phone.

## Requirements

- **Python 3.6+**
- **Internet Connection** (for Wikipedia and WhatsApp functionality)
- **Microphone** (for voice commands)
- **Windows OS** (Some features may be OS-specific)

## Libraries Used

- **pyttsx3**: Text-to-speech conversion
- **SpeechRecognition**: Microphone input and voice recognition
- **wikipedia**: Wikipedia search and summary retrieval
- **webbrowser**: Web browsing
- **os**: File and directory handling
- **random**: Random selection for music and movie playback
- **pywhatkit**: Scheduling WhatsApp messages
- **pycaw**: Adjusting system volume on Windows

## Troubleshooting

- If `pyttsx3` is not working properly, check the voice engine and ensure `sapi5` is available on your system.
- For WhatsApp functionality, ensure your WhatsApp Web is linked to your browser.



