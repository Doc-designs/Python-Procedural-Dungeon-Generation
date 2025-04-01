import pygame

class Collision:
    def MapBounds(player, WINDOW_WIDTH, WINDOW_HEIGHT):
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
