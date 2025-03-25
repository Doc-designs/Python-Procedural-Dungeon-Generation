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


class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft = (0,0))

    def custom_draw(self):
        self.offset.x = player.rect.centerx - WIDTH // 2
        self.offset.y = player.rect.centery - HEIGHT //2

        floor_offset_pos = self.floor_rect.topleft - self.offset

        for sprite in all_sprites_group:
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.image, offset_pos)

class GUI:
    def GameText(text, screen, position, font):
        font.render_to(screen, position, text, (0, 0, 0))
