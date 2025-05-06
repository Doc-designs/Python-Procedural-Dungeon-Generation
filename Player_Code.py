import pygame
import pygame.freetype #Used for Text
import Config
from enum import Enum

class Player:
    def __init__(self, isInventoryOpen):
        self.isInventoryOpen = isInventoryOpen
        self.spriteWidth = 32
        self.spriteHeight = 32
        self.repeatedAction = False
        self.PreviousAction = "Down"
        self.frameIndex = 0
        self.frameList = []
        self.animationSheet = Config.LoadAsset.PlayerDown.value
        self.playerImage = pygame.transform.scale(pygame.image.load(self.animationSheet).convert_alpha(), (50, 50))       
    def CreatePlayer(self):
        player = pygame.Rect(400, 300, 50, 50)
        return player
    def SwapAnimation(self, animation):
        match animation:
            case Config.LoadAsset.PlayerUp:
                self.animationSheet = Config.LoadAsset.PlayerUp
            case Config.LoadAsset.PlayerDown:
                self.animationSheet = Config.LoadAsset.PlayerDown
            case Config.LoadAsset.PlayerLeft:
                self.animationSheet = Config.LoadAsset.PlayerLeft
            case Config.LoadAsset.PlayerRight:
                self.animationSheet = Config.LoadAsset.PlayerRight
        self.playerImage = pygame.transform.scale(pygame.image.load(animation).convert_alpha(), (50, 50))
        self.SwapFrameList()
    def SwapFrameList(self):
        self.frameList = []
        for x in range(4):
            for y in range(0):
                rect = pygame.Rect(x*self.spriteWidth, y*self.spriteHeight, self.spriteWidth, self.spriteHeight)
                frame = self.playerImage.subsurface(rect)
                self.frameList.append(frame)
    def IndexFrameList(self):
        if self.previousAction!="Idle":
            if self.frameIndex < len(self.frameList):
                self.frameIndex+=1
            else:
                self.frameIndex = 0
    def DrawPlayer(self, screen, player, clock):
        #Draw Over Previous Drawings
        if len(self.frameList)>0:
            screen.blit(self.frameList[self.frameIndex], self.playerImage.get_rect(center = (player.x, player.y)))
        #pygame.draw.rect(screen, (0, 255, 0), player)
        clock.tick(60)
        return player
    
    def Controls(self, player):
        #Controls
        keys = pygame.key.get_pressed()
        if len(keys)<1:
            self.frameIndex = 0
            self.PreviousAction="Idle"
        if keys[pygame.K_UP]:
            if self.repeatedAction == False and self.PreviousAction == "Up":
                repeatedAction = True
                self.previousAction = "Up"
                self.IndexFrameList()
            elif not(self.PreviousAction=="Up"):
                repeatedAction = False
                self.SwapAnimation(Config.LoadAsset.PlayerUp.value)
                self.frameIndex = 0
            player.y -= 5
        if keys[pygame.K_DOWN]:
            if self.repeatedAction == False and self.PreviousAction == "Down":
                repeatedAction = True
                self.previousAction = "Down"
                self.IndexFrameList()
            elif not(self.PreviousAction=="Down"):
                repeatedAction = False
                self.SwapAnimation(Config.LoadAsset.PlayerDown.value)
                self.frameIndex = 0
            player.y += 5
        if keys[pygame.K_LEFT]:
            if self.repeatedAction == False and self.PreviousAction == "Left":
                repeatedAction = True
                self.previousAction = "Left"
                self.IndexFrameList()
            elif not(self.PreviousAction=="Left"):
                repeatedAction = False
                self.SwapAnimation(Config.LoadAsset.PlayerLeft.value)
                self.frameIndex = 0
            player.x -= 5
        if keys[pygame.K_RIGHT]:
            if self.repeatedAction == False and self.PreviousAction == "Right":
                repeatedAction = True
                self.previousAction = "Right"
                self.IndexFrameList()
            elif not(self.PreviousAction=="Right"):
                repeatedAction = False
                self.SwapAnimation(Config.LoadAsset.PlayerRight.value)
                self.frameIndex = 0
            player.x += 5
        if keys[pygame.K_TAB]:
            if self.repeatedAction == True and self.PreviousAction == "Inventory":
                return
            else:
                self.repeatedAction = False
                self.PreviousAction = "Inventory"
                if self.isInventoryOpen == False:
                    self.isInventoryOpen = True
                else:
                    self.isInventoryOpen = False
        
        return player.move(player.x, player.y)

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft = (0,0))

    def custom_draw(self):
        self.offset.x = player.rect.centerx - WIDTH // 2
        self.offset.y = player.rect.centery - HEIGHT // 2

        floor_offset_pos = self.floor_rect.topleft - self.offset

        for sprite in all_sprites_group:
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.image, offset_pos)

class Inventory:
    #def __init__(self, player, WINDOW_WIDTH, WINDOW_HEIGHT):
        #self.player = player
        #self.selector_image = pygame.transform.scale(pygame.image.load("Assets/GUI/Selector.png"), (50, 55))
        #self.hotbar_image = pygame.transform.scale(pygame.image.load("Assets/GUI/Hotbar.png"), (500, 64))
        #self.hotbar_rect = self.hotbar_image.get_rect(WINDOW_HEIGHT-30, center=(WINDOW_WIDTH/2))

    def CreateHotbar(screen, WINDOW_WIDTH, WINDOW_HEIGHT, Slots_Amount):
        blockSize = 50 #Set the size of the grid block
        GRAY = (192, 192, 192)
        WHITE = (255, 255, 255)
        for x in range(int(WINDOW_WIDTH/4), int(WINDOW_WIDTH-(WINDOW_WIDTH/4)), blockSize):
                slotSpace = pygame.Rect(x, WINDOW_HEIGHT-blockSize, 50, 50)
                pygame.draw.rect(screen, WHITE, slotSpace, 1)
                border = pygame.Rect(x, WINDOW_HEIGHT-blockSize, blockSize, blockSize)
                pygame.draw.rect(screen, WHITE, border, 1)
                
    def CreateInventory(screen, WINDOW_WIDTH, WINDOW_HEIGHT, Slots_Amount):
        blockSize = 50 #Set the size of the grid block
        GRAY = (192, 192, 192)
        WHITE = (200, 200, 200)
        for x in range(int(WINDOW_WIDTH/2), int(WINDOW_WIDTH-(WINDOW_WIDTH/2)), blockSize):
            for y in range(int(WINDOW_HEIGHT/2), int(WINDOW_HEIGHT-(WINDOW_HEIGHT/2)), blockSize):
                slotSpace = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, GRAY, slotSpace, 1)
                border = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, WHITE, border, 1)
class UI:
    def GameText(text, screen, position, font):
        font.render_to(screen, position, text, (0, 0, 0))
