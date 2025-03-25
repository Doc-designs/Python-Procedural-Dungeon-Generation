import pygame
import Player_Code
import Map_Generator
print("Pygame Version: ", pygame.ver)
class WindowHandler:
    def WindowSetup():
        #Create a Global Window Variable to Create And Track
        #Programs Display Window
        global WINDOW_HEIGHT
        WINDOW_HEIGHT = 600
        global WINDOW_WIDTH
        WINDOW_WIDTH = 800
        global screen
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        #Display Game Title On Window
        pygame.display.set_caption("Infinite Dungeons")
        
    def CheckProgramEvents(screen):
        #Loop Through All Active Events
        for event in pygame.event.get():
                #If Active Event is Quit
                if event.type == pygame.QUIT:
                    #set Running to False
                    return False
                elif event.type == pygame.VIDEORESIZE:
                    global WINDOW_WIDTH
                    WINDOW_WIDTH = event.w
                    global WINDOW_HEIGHT
                    WINDOW_HEIGHT = event.h
                    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        #No Active Quit Event Call, So Continue Running Game
        return True
class Game:
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
        if player.x > WINDOW_WIDTH-50:
            #Set Border Limit
            player.x = WINDOW_WIDTH-50
        #If Player is Too Far Down
        if player.y > WINDOW_HEIGHT-50:
            #Set Border Limit
            player.y = WINDOW_HEIGHT-50

    def main():
        #Activate Pygame Tools
        pygame.init()
        #Call WindowSetup Function to Create Game Display Window
        WindowHandler.WindowSetup()
        #Connect Other Scripts
        playerInstance = Player_Code.Player
        GUInstance = Player_Code.GUI
        DungeonInstance = Map_Generator.MapGeneration
        #Assign Game Assets
        GAME_FONT = pygame.freetype.Font("Assets/Fonts/NotoSansWarangCiti-Regular.ttf", 24)

        #Game Initialization
        clock = pygame.time.Clock()
        running = True

        #Create Player
        player = playerInstance.CreatePlayer(screen)


        #Run Window Till Closed
        while running:
            #Draw Tiles
            DungeonInstance.DrawGrid(screen, WINDOW_WIDTH, WINDOW_HEIGHT)
            #Tile System
            #DungeonInstance.GeneratePerlinNoise(screen)
            #Draw Player
            playerInstance.DrawPlayer(screen, player, clock)
            #Player Controls Handler
            playerInstance.Controls(player)
            #Check Map Bounds
            Game.MapBounds(player)
            #Post Text to Screen
            pygame.display.update()
            #Close Window on Exit
            running = WindowHandler.CheckProgramEvents(screen)

        pygame.quit()

if __name__ == "__main__":
    Game.main()

