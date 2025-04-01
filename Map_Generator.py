import random
import pygame
import Config

class MapGeneration:

    def DrawGrid(screen, WINDOW_WIDTH, WINDOW_HEIGHT):
        blockSize = 50 #Set the size of the grid block
        BLACK = (0, 0, 0)
        WHITE = (200, 200, 200)
        screen.fill(BLACK)
        for x in range(0, WINDOW_WIDTH, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, WHITE, rect, 1)
                
    def GenerateNoise(width, height):
        noise_map = []
        # Populate a noise map with 0s
        for y in range(height):
            new_row = []
            for x in range(width):
                new_row.append(0)
            noise_map.append(new_row)

        # Progressively apply variation to the noise map but changing values + or -
        # 5 from the previous entry in the same list, or the average of the
        # previous entry and the entry directly above
        new_value = 0
        top_of_range = 0
        bottom_of_range = 0
        for y in range(height):
            for x in range(width):
                if x == 0 and y == 0:
                    continue
                if y == 0:  # If the current position is in the first row
                    new_value = noise_map[y][x - 1] + random.randint(-1000, +1000)
                elif x == 0:  # If the current position is in the first column
                    new_value = noise_map[y - 1][x] + random.randint(-1000, +1000)
                else:
                    minimum = min(noise_map[y][x - 1], noise_map[y-1][x])
                    maximum = max(noise_map[y][x - 1], noise_map[y-1][x])
                    average_value = minimum + ((maximum-minimum)/2.0)
                    new_value = average_value + random.randint(-1000, +1000)
                noise_map[y][x] = new_value
                # check whether value of current position is new top or bottom
                # of range
                if new_value < bottom_of_range:
                    bottom_of_range = new_value
                elif new_value > top_of_range:
                    top_of_range = new_value
        # Normalises the range, making minimum = 0 and maximum = 1
        difference = float(top_of_range - bottom_of_range)
        for y in range(height):
            for x in range(width):
                noise_map[y][x] = (noise_map[y][x] - bottom_of_range)/difference
        return noise_map
    def CreateMap(noiseMap):
        ConfigInstance = Config.WorldSettings
        mapTiles = []
        for y in range(0, maxCol):
            for x in range(0, maxRow):
                if noiseMap[y][x] < .3:
                    imagePath = Config.LoadAsset(Water)
                    image = pygame.image.load(imagePath)
                    mapTiles[y][x] = image
                #Draw Mountains
                elif noiseMap[y][x] > .6:
                    imagePath = Config.LoadAsset(Water)
                    image = pygame.image.load(imagePath)
                    mapTiles[y][x] = image
        return mapTiles
    def DrawMap(screen, noiseMap, minCol, maxCol, minRow, maxRow):
        ConfigInstance = Config.WorldSettings
        for y in range(minCol, maxCol):
            for x in range(minRow, maxRow):
                #Draw Water
                if noiseMap[y][x] < .3:
                    imageRect = image.get_rect()
                    screen.blit(myimage)
                #Draw Mountains
                elif noiseMap[y][x] > .6:
                    print("Draw Stuff")
