import pygame
import pygame.freetype #Used for Text
class Player:
    def CreatePlayer(screen, clock):
        player = pygame.Rect(400, 300, 50, 50)
        screen.fill((153, 50, 168))
        pygame.draw.rect(screen, (0, 255, 0), player)
        #pygame.display.flip()
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
class GUI:
    def GameText(text, screen, position, font):
        font.render_to(screen, position, text, (0, 0, 0))
        #pygame.display.flip()
