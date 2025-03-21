import pygame

class MapGenerator:
    def GeneratePerlinNoise(screen):
        screen.fill((153, 50, 168))
        grid = [[1 if ( x + y) % 2 == 0 else 0 for x in range(10)] for y in range(10)]
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                color = (200, 200, 200) if grid[y][x] == 1 else (50,50,50)
                pygame.draw.rect(screen, color, pygame.Rect(x*60, y*60, 60, 60))
