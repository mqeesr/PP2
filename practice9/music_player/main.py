import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 26)
clock = pygame.time.Clock()

music_directory = "/home/deuteruim/Desktop/code/pp2/practice9/player/music"

music_files = []
for file in os.listdir(music_directory):
    if file.endswith(".mp3") or file.endswith(".wav"):
        music_files.append(file)

music_files.sort()

current_track = 0
paused = False
started = False

if len(music_files) > 0:
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(music_files) > 0:
                    if not started:
                        pygame.mixer.music.play()
                        started = True
                        paused = False
                    elif paused:
                        pygame.mixer.music.unpause()
                        paused = False
                    else:
                        pygame.mixer.music.pause()
                        paused = True

            elif event.key == pygame.K_RIGHT:
                if len(music_files) > 0:
                    current_track = (current_track + 1) % len(music_files)
                    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
                    pygame.mixer.music.play()
                    started = True
                    paused = False

            elif event.key == pygame.K_LEFT:
                if len(music_files) > 0:
                    current_track = (current_track - 1) % len(music_files)
                    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
                    pygame.mixer.music.play()
                    started = True
                    paused = False

            elif event.key == pygame.K_q:
                running = False

    screen.fill((255, 255, 255))

    title = font.render("Music Player", True, (0, 0, 0))
    screen.blit(title, (270, 20))

    instructions = small_font.render(
        "SPACE - Play/Pause   LEFT - Previous   RIGHT - Next   Q - Quit",
        True,
        (0, 0, 0)
    )
    screen.blit(instructions, (30, 60))

    if len(music_files) > 0:
        current_text = font.render("Current track:", True, (0, 0, 0))
        screen.blit(current_text, (50, 140))

        track_text = small_font.render(music_files[current_track], True, (0, 0, 255))
        screen.blit(track_text, (50, 180))

        list_title = font.render("Playlist:", True, (0, 0, 0))
        screen.blit(list_title, (420, 140))

        y = 190
        for i in range(len(music_files)):
            if i == current_track:
                text = small_font.render("> " + music_files[i], True, (255, 0, 0))
            else:
                text = small_font.render(music_files[i], True, (0, 0, 0))
            screen.blit(text, (420, y))
            y += 35
    else:
        no_music = font.render("No music files found", True, (255, 0, 0))
        screen.blit(no_music, (180, 220))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()