# neodium-terminal-music-player
This is a terminal based music player that uses YouTube APIs and PyTube to work! This Python script allows you to search for a song on YouTube, download its audio, add it to a playlist, and play it using the playsound library.

## Prerequisites
+ Python 3.x
+ google-api-python-client library
+ pytube library
+ playsound library

## Setup
Install the required Python libraries using pip:

``` bash
pip install google-api-python-client pytube playsound
```
+ Obtain a YouTube Data API key from the Google Developers Console.
+ Set up the YouTube Data API by enabling it for your project and creating an API key.

## Usage
+ Run the script `main.py` using Python.
+ Enter the name of the song you want to download. Make sure to include the artist's name for better search results.
+ The script will search for the song on YouTube, download its audio, save it to a 'music' folder, and play it using the playsound library.
+ You will be prompted to add the downloaded song to a playlist.
#### Optionally, you can choose to play the entire playlist once the download is complete.

## Features
+ Searches for songs on YouTube using the YouTube Data API.
+ Downloads the audio of the selected song.
+ Saves downloaded songs to a 'music' folder.
+ Adds songs to a playlist in a CSV file.
+ Plays downloaded songs using the playsound library.

## Notes
+ The script requires a stable internet connection to search and download songs from YouTube.
+ Ensure that you have sufficient disk space for storing downloaded music files.


## Author
This script was developed by [Partha Sarathi Dey](https://linkedin.com/in/sarathiparth).

## License
This project is licensed under the [MIT License](https://github.com/parthasdey2304/neodium-terminal-music-player/blob/main/LICENSE).






