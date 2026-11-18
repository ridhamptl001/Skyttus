
class MusicPlayer:
    def play(self):
        print("Playing music.")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify.")


player = MusicPlayer()
spotify = Spotify()

player.play()
spotify.play()
