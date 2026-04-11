import os
import pygame


class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()

        self.music_folder = music_folder
        self.playlist = self.load_playlist()
        self.current_index = 0
        self.status = "Stopped"
        self.paused = False

    def load_playlist(self):
        tracks = []

        if not os.path.exists(self.music_folder):
            return tracks

        for file_name in os.listdir(self.music_folder):
            if file_name.endswith(".mp3") or file_name.endswith(".wav"):
                full_path = os.path.join(self.music_folder, file_name)
                tracks.append(full_path)

        tracks.sort()
        return tracks

    def play(self):
        if not self.playlist:
            self.status = "No tracks"
            return

        if self.paused:
            pygame.mixer.music.unpause()
            self.status = "Playing"
            self.paused = False
        else:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
            self.status = "Playing"
            self.paused = False

    def pause(self):
        if self.status == "Playing":
            pygame.mixer.music.pause()
            self.status = "Paused"
            self.paused = True

    def next_track(self):
        if not self.playlist:
            self.status = "No tracks"
            return

        self.current_index += 1
        if self.current_index >= len(self.playlist):
            self.current_index = 0

        self.paused = False
        self.play()

    def previous_track(self):
        if not self.playlist:
            self.status = "No tracks"
            return

        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.playlist) - 1

        self.paused = False
        self.play()

    def get_current_track_name(self):
        if not self.playlist:
            return "None"
        return os.path.basename(self.playlist[self.current_index])

    def get_position_seconds(self):
        pos = pygame.mixer.music.get_pos()

        if pos == -1:
            return 0

        return pos // 1000

    def update(self):
        if self.status == "Playing" and not self.paused:
            if not pygame.mixer.music.get_busy():
                self.next_track()