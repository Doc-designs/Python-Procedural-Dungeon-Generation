import pygame
import Player_Code
import Map_Generation
print("Pygame Version: ", pygame.ver)

def WindowSetup():
    #Create a Global Window Variable to Create And Track
    #Programs Display Window
    global screen
    screen = pygame.display.set_mode((800, 600))
    #Display Game Title On Window
    pygame.display.set_caption("Infinite Dungeons")
    
def CheckIfQuit():
    #Loop Through All Active Events
    for event in pygame.event.get():
            #If Active Event is Quit
            if event.type == pygame.QUIT:
                #set Running to False
                return False
    #No Active Quit Event Call, So Continue Running Game
    return True

def MapBounds(player):
    #If Player is Too Far Left
    if player.x < 0:
        #Set Border Limit
        player.x = 0
    #If Player is Too Far Down
    if player.y < 0:
        #Set Border Limit
        player.y = 0
    #If Player is Too Far Right
    if player.x > 750:
        #Set Border Limit
        player.x = 750
    #If Player is Too Far Down
    if player.y > 550:
        #Set Border Limit
        player.y = 550

def main():
    #Activate Pygame Tools
    pygame.init()
    #Call WindowSetup Function to Create Game Display Window
    WindowSetup()
    #Connect Other Scripts
    playerInstance = Player_Code.Player
    GUInstance = Player_Code.GUI
    DungeonInstance = Map_Generation.MapGenerator
    #Assign Game Assets
    GAME_FONT = pygame.freetype.Font("Assets/Fonts/NotoSansWarangCiti-Regular.ttf", 24)

    #Game Initialization
    clock = pygame.time.Clock()
    running = True

    #Create Player
    player = playerInstance.CreatePlayer(screen)


    #Run Window Till Closed
    while running:
        #Tile System
        DungeonInstance.GeneratePerlinNoise(screen)
        #Draw Player
        playerInstance.DrawPlayer(screen, player, clock)
        #Player Controls Handler
        playerInstance.Controls(player)
        #Check Map Bounds
        MapBounds(player)
        #Post Text to Screen
        GUInstance.GameText("Hello World!", screen, (40, 350), GAME_FONT)
        pygame.display.update()
        #Close Window on Exit
        running = CheckIfQuit()

    pygame.quit()

if __name__ == "__main__":
    main()

