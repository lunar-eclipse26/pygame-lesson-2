# i failed the original hollow purple so here is the true hollow purple
# read half the caption while looking at the blue circle
# then read the other half except the words hollw purple while looking at the red circle
# and finally read the words hollow purple while looking at he purple circle
import pygame
pygame.init()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('(blue circle) nine ropes... polarized light... (now the red circle) crow and declaration... between front and back... (purple circle now) HOLLOW PURPLE')
window.fill((255, 255, 255))
lapse_blue = (69, 176, 210)
reversal_red = (170, 0, 0)
hollow_purple = (102, 51, 153)
pygame.draw.circle(window, lapse_blue, (100, 200), 50, 3)
pygame.draw.circle(window, reversal_red, (400, 200), 50, 3)
pygame.draw.circle(window, hollow_purple, (250, 400), 75)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()