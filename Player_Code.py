import pygame
import pygame.freetype #Used for Text

class Player:
    def CreatePlayer(screen):
        player = pygame.Rect(400, 300, 50, 50)
        return player
        
    def DrawPlayer(screen, player, clock):
        #Draw Over Previous Drawings
        pygame.draw.rect(screen, (0, 255, 0), player)
        clock.tick(60)
        return player
    
    def Controls(player):
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
        return player.move(player.x, player.y)
        #New Controls Implementation
        '''
        new_x = player.x // 60
        new_y = player.y // 60
        if grid[new_y][new_x] == 1:
            player.x = new_x * 60
            player.y = new_y * 60
        '''
        
class GUI:
    def GameText(text, screen, position, font):
        font.render_to(screen, position, text, (0, 0, 0))
        #pygame.display.flip()
