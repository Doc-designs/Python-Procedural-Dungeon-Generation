import pygame
import Player_Code
import Map_Generator
import CollisionHandler
import Config
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

    def main():
        #Activate Pygame Tools
        pygame.init()
        #Call WindowSetup Function to Create Game Display Window
        WindowHandler.WindowSetup()
        #RegisterConfig
        inventoryConfig = Config.InventorySettings
        #Connect Other Scripts
        playerInstance = Player_Code.Player(False)
        playerInstance.SwapAnimation(playerInstance.animationSheet)
        collisionHandler = CollisionHandler.Collision
        inventoryHandler = Player_Code.Inventory
        dungeonInstance = Map_Generator.MapGeneration
        #Assign Game Assets
        GAME_FONT = pygame.freetype.Font("Assets/Fonts/NotoSansWarangCiti-Regular.ttf", 24)

        #Game Initialization
        clock = pygame.time.Clock()
        running = True

        #Create Player
        player = playerInstance.CreatePlayer()


        #Run Window Till Closed
        while running:
            #print(playerInstance.isInventoryOpen)
            playerInputs = playerInstance.Controls(player)
            #Player Controls Handler
            playerInstance.Controls(player)
            #Check Map Bounds
            collisionHandler.MapBounds(player, WINDOW_WIDTH, WINDOW_HEIGHT)
            #Draw Tiles
            dungeonInstance.DrawGrid(screen, WINDOW_WIDTH, WINDOW_HEIGHT)
            #Tile System
            #DungeonInstance.GeneratePerlinNoise(screen)
            #Draw Player
            playerInstance.DrawPlayer(screen, player, clock)
            print([player.x, player.y])
            #Draw Inventory
            hotBar = inventoryHandler.CreateHotbar(screen, WINDOW_WIDTH, WINDOW_HEIGHT, inventoryConfig.hotbarSize)
            if playerInstance.isInventoryOpen:
                inventory = inventoryHandler.CreateInventory(screen, WINDOW_WIDTH, WINDOW_HEIGHT, inventoryConfig.inventorySize)
            #Post Text to Screen
            pygame.display.update()
            #Close Window on Exit
            running = WindowHandler.CheckProgramEvents(screen)

        pygame.quit()

if __name__ == "__main__":
    Game.main()

