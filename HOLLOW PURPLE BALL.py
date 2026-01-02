import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((255, 255, 255))
lapse_blue = (69, 176, 210)
reversal_red = (170, 0, 0)
hollow_purple = (102, 51, 153)
pygame.draw.circle(window, lapse_blue, (200, 200), 50, 3)
pygame.draw.circle(window, reversal_red, (400, 200), 50, 3)
pygame.draw.circle(window, hollow_purple, (250, 400), 75)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()