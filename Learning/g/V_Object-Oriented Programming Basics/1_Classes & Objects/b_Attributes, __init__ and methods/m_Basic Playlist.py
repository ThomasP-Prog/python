"""
Define a class Song with an __init__ that takes title and artist and stores them as attributes. Define a class Playlist.

    Its __init__ should initialize an instance attribute name (for the playlist's name) and songs as an empty list.
    Add a method add_song(song: Song) that adds a Song object to the songs list.
    Add a method list_songs() that prints "Playlist: [playlist name]" and then prints each song's title and artist on a new line 
    (e.g., "Title: Highway to Hell, Artist: AC/DC"). If no songs, it prints "Playlist is empty."

Sample Usage: Create a playlist, add a few Song instances to it, then list the songs.
"""

class Song:
    def __init__(self, title:str, artist:str) -> None:
        """Initialize the Song"""
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self, playlist_name: str) -> None:
        """Initialize the Playlist"""
        self.playlist_name = playlist_name
        self.songs = []

    def add_song(self, song: Song) -> None:
        """add a song to the playlist"""
        self.songs.append(song)

    def list_songs(self) -> None:
        """Print the list of songs in the playlist"""
        if not self.songs:
            print(f"{self.playlist_name} is empty.")
        else:
            print(f"Playlist {self.playlist_name} :")
            for song in self.songs:
                print(f"Title : {song.title}, Artist : {song.artist}")

def main() -> None:
    """main function"""
    new_playlist = Playlist("First Playlist")
    song1 = Song("First song","Bob")
    song2 = Song("Second song","Charles")
    new_playlist.add_song(song1)
    new_playlist.add_song(song2)
    new_playlist.list_songs()

if __name__ == "__main__":
    main()