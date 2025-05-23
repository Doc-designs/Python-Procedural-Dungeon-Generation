from enum import Enum
class Terrain(Enum):
    WATER = 0
    BEACH = 1
    GRASS = 2
    MOUNTAIN = 3
class LoadAsset(Enum):
    PlayerUp = "Assets/Player/Character_Up.png"
    PlayerDown = "Assets/Player/Character_Down.png"
    PlayerLeft = "Assets/Player/Character_Left.png"
    PlayerRight = "Assets/Player/Character_Right.png"
    Enemy = "Enemy"
    TileSet = "Assets/Tilemaps/water_and_island_tiles_v2.png"
    
class WorldSettings:
    TILESIZE = 50
    WORLD_X = 100
    WORLD_Y = 100

    ALL_TERRAIN_TYPES = [Terrain.WATER, Terrain.BEACH,
                         Terrain.GRASS, Terrain.MOUNTAIN]

    TERRAIN_TILES = [
        #Water Tiles
        [
            (0, 0),
            (20, 20)
        ],
        #Beach Tiles
        [
            (0, 0),
            (20, 20)
        ],
        #Grass Tiles
        [
            (0, 0),
            (20, 20)
        ],
        #Mountain
        [
            (0, 0),
            (20, 20)
        ],
                ]

class InventorySettings:
    hotbarSize = 8
    inventorySize = 24
