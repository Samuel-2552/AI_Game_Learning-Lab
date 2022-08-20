import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((400, 376))
pygame.display.set_caption('Virtual Pet')
clock = pygame.time.Clock()
frames = []
for i in range(74):
    frames.append(pygame.image.load(
        'Experiment_4/Frames/frame'+str(i)+'.png').convert_alpha())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for frame in frames:
        screen.blit(frame, (0, 0))
        pygame.display.update()
        clock.tick(20)
