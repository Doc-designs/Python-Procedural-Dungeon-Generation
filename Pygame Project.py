import pygame
import pygame.freetype #Used for Text
print("Pygame Version: ", pygame.ver)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Infinite Dungeons")
GAME_FONT = pygame.freetype.Font("freesansbold.ttf", 24)
running = True

clock = pygame.time.Clock()
player = pygame.Rect(400, 300, 50, 50)

#Run Window Till Closed
while running:
    #Setup Window
    screen.fill((153, 50, 168))
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.display.flip()
    clock.tick(60)
    #Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if player.x < 0:
        player.x = 0
    if player.y < 0:
        player.y = 0
    if player.x > 750:
        player.x = 750
    if player.y > 550:
        player.y = 550
    #Post Text to Screen
    GAME_FONT.render_to(screen, (40, 350), "Hello World!", (0, 0, 0))
    pygame.display.flip()
    #Tile System
    grid = [[1 if ( x + y) % 2 == 0 else 0 for x in range(10)] for y in range(10)]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            color = (200, 200, 200) if grid[y][x] == 1 else (50,50,50)
            pygame.draw.rect(screen, color, pygame.Rect(x*60, y*60, 60, 60))
    #Close Window on Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
