import pygame
import pygame.freetype #Used for Text
print("Pygame Version: ", pygame.ver)


def CreatePlayer(screen, player, clock):
    screen.fill((153, 50, 168))
    pygame.draw.rect(screen, (0, 255, 0), player)
    #pygame.display.flip()
    clock.tick(60)
    
    
def Controls(player, keys, grid):
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
    #New Controls Implementation
    '''
    new_x = player.x // 60
    new_y = player.y // 60
    if grid[new_y][new_x] == 1:
        player.x = new_x * 60
        player.y = new_y * 60
    '''
        
def GameText(text, screen, position, font):
    font.render_to(screen, position, text, (0, 0, 0))
    #pygame.display.flip()

def GeneratePerlinNoise(grid, screen):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            color = (200, 200, 200) if grid[y][x] == 1 else (50,50,50)
            pygame.draw.rect(screen, color, pygame.Rect(x*60, y*60, 60, 60))

#def Quit():
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Infinite Dungeons")
    GAME_FONT = pygame.freetype.Font("NotoSansWarangCiti-Regular.ttf", 24)
    clock = pygame.time.Clock()
    player = pygame.Rect(400, 300, 50, 50)
    running = True


    #Run Window Till Closed
    while running:
        #Setup Window
        CreatePlayer(screen, player, clock)
        #Controls
        keys = pygame.key.get_pressed()
        grid = [[1 if ( x + y) % 2 == 0 else 0 for x in range(10)] for y in range(10)]
        Controls(player, keys, grid)
        #Post Text to Screen
        GameText("Hello World!", screen, (40, 350), GAME_FONT)
        #Tile System
        GeneratePerlinNoise(grid, screen)
        pygame.display.update()
        #Close Window on Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()

