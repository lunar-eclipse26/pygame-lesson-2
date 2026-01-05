import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((165, 78, 254))
pygame.display.set_caption(':O RECTANGLE of sqaureness that circularizes a line')
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (90, 140, 180), pygame.Rect(150, 300, 400, 300))
    pygame.display.flip()