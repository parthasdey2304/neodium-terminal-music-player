import os
from googleapiclient.discovery import build
from pytube import YouTube
from playsound import playsound

# Set up the YouTube Data API
api_key = 'AIzaSyAS2dwBxkWHjixnZT4Kf1zHDoO3uO_DbyU'
youtube = build('youtube', 'v3', developerKey=api_key)

# Function to get the URL of the YouTube video based on its name
def get_video_url(video_name):
    try:
        # Call the search.list method to retrieve matching videos
        request = youtube.search().list(
            q=video_name,
            part='id',
            maxResults=1,
            type='video'
        )
        response = request.execute()

        # Extract the video ID from the response
        if 'items' in response:
            video_id = response['items'][0]['id']['videoId']
            # Construct the URL based on the video ID
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            return video_url
        else:
            return None
    except Exception as e:
        print(f"An error occurred while searching for the video: {str(e)}")
        return None

# Function to download and play the music
def download_and_play_music(video_url):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the best audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Create a 'music' folder if it doesn't exist
        if not os.path.exists('music'):
            os.makedirs('music')

        # Get the filename of the downloaded audio
        audio_filename = os.path.join('music', audio_stream.default_filename)

        # Check if the file already exists in the 'music' folder
        if not os.path.exists(audio_filename):
            # Download the audio stream and save it to the 'music' folder if it's not already present
            print("Downloading...")
            print("Download completed successfully!")
            audio_stream.download(output_path='music')
        else:
            print("File already exists. Skipping download.")

        # Add the song to the playlist
        add_to_playlist(yt.title, yt.author, yt.length)

        # Play the downloaded audio
        play_music(audio_filename)

    except Exception as e:
        print(f"An error occurred while downloading or playing the music: {str(e)}")

# Function to play the music
def play_music(filename):
    try:
        print("Playing...")
        playsound(filename)
    except Exception as e:
        print(f"An error occurred while playing the music: {str(e)}")

# Function to add a song to the playlist
def add_to_playlist(song_name, singer, duration):
    try:
        # Read existing playlist data
        existing_songs = set()
        with open('playlist.csv', mode='r') as file:
            for line in file:
                # Split each line and extract song details
                _, existing_song_name, existing_singer, existing_duration = line.strip().split(', ')
                existing_songs.add((existing_song_name, existing_singer, existing_duration))

        # Check if the song with the same singer and duration already exists
        if (song_name, singer, duration) in existing_songs:
            print("Song already exists in the playlist.")
        else:
            with open('playlist.csv', mode='a') as file:
                # Get the current number of songs in the playlist
                num_songs = len(existing_songs)

                # Write the song details to the playlist file
                file.write(f"{num_songs + 1}, {song_name}, {singer}, {duration}\n")
                print("Song added to playlist successfully!")

    except Exception as e:
        print(f"An error occurred while adding the song to the playlist: {str(e)}")


# Function to play the playlist
def play_playlist():
    try:
        with open('playlist.csv', mode='r') as file:
            lines = file.readlines()
            for line in lines:
                song_details = line.strip().split(', ')
                print(f"\nNow playing: {song_details[1]} by {song_details[2]}")
                # Play the song
                filename = os.path.join('music', f"{song_details[1]}.mp4")  # Assuming the filename is the song name with .mp4 extension
                play_music(filename)
                # Wait for user input to continue playing the next song
                input("Press Enter to play the next song...")
    except Exception as e:
        print(f"An error occurred while playing the playlist: {str(e)}")

if __name__ == "__main__":
    video_name = input("Enter the name of the song (with the artist's name): ")
    video_url = get_video_url(video_name)

    if video_url:
        print("Video URL found:", video_url)
        download_and_play_music(video_url)
    else:
        print("No video found for the given name.")

    # Option to play the playlist
    print(f"\nPLAYLIST\n{'-' * 15}\n")
    os.system("tree music")
    choice = (input("\nDo you want to play the playlist? (yes/no): ").lower()).strip()
    if choice == 'yes':
        play_playlist()
    else:
        print("Thank You! Bye Bye!!")