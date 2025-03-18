import pygame
import Player_Code
import Map_Generation
print("Pygame Version: ", pygame.ver)

#def Quit():
    
def main():
    playerInstance = Player_Code.Player
    GUInstance = Player_Code.GUI
    DungeonInstance = Map_Generation.MapGenerator
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Infinite Dungeons")
    GAME_FONT = pygame.freetype.Font("Assets/Fonts/NotoSansWarangCiti-Regular.ttf", 24)
    clock = pygame.time.Clock()
    running = True


    #Run Window Till Closed
    while running:
        #Setup Window
        player = playerInstance.CreatePlayer(screen, clock)

        playerInstance.Controls(player)
        #Post Text to Screen
        GUInstance.GameText("Hello World!", screen, (40, 350), GAME_FONT)
        #Tile System
        DungeonInstance.GeneratePerlinNoise(screen)
        pygame.display.update()
        #Close Window on Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()

