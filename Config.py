import Enum
class Terrain(Enum):
    WATER = 0
    BEACH = 1
    GRASS = 2
    MOUNTAIN = 3
class LoadAsset(Enum):
    Player = "Player"
    Enemy = "Enemy"
    Water = ""
    Mountain = "Mountain"
    
class WorldSettings:
    TILESIZE = 50
    WORLD_X = 100
    WORLD_Y = 100

    ALL_TERRAIN_TYPES = [WATER, BEACH, GRASS, MOUNTAIN]

    TERRAIN_TILES = [
        #Deep Ocean Tiles
        [
            (0, 0),
            (20, 20)
        ],
        #Light Water Tiles
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

