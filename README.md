# Discord Transcript Library
A simple library to generate transcripts of text channels and threads. The library exports conversations to HTML files, preserving the formatting and attachments.

## Features

- Channel Transcript: Generates a transcript of an entire text channel, including messages and attachments.
- Thread Transcript: Creates a transcript for a specific thread, preserving the conversation history.
- All Threads Transcript: Exports transcripts for all threads in a channel, combining them into separate HTML files.

## Setup

### Clone the repository:
```
git clone https://github.com/yourusername/discord-transcript-bot.git
cd discord-transcript-bot
```
### Install the required dependencies:
```
pip install discord.py
```
### Build
```
python setup.py bdist_wheel
pip install path/to/dist/htmlDiscordTranscript-0.1.1-py3-none-any.whl
```

## Notes

- HTML files will be sent to the user who triggered the command through direct messages.

Feel free to contribute, report issues, or suggest improvements!
