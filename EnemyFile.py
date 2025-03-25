import pygame

class Enemy(pygame.sprite.Sprite):
    def CreateEnemy(self, position):
        super().__init__(enemy_group, all_sprites_group)
        self.image = pygame.image.load("Assets/Enemies/").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 2)

        self.rect = self.image.get_rect()
        self.rect.center = position

        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.speed = Config.enemySpeed
    def DrawEnemy(self, ):
        print("draw enemy")
    def Distribute():
        print("This will Determine Enemy Placement")

    def HuntPlayer(self):
        playerVector
        enemyVector
        distance

        if distance > 0:
            self.direction = (playerVector-enemyVector).normalize()
        else:
            self.direction = pygame.math.Vector2()
        self.velocity = self.direction * self.speed
        self.position += self.velocity

        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def GetVectorDistance(self, vector_1, vector_2):
        return (vector_1 - vector_2).magnitude()

    def Update(self):
        self.HuntPlayer()

class Config:
    enemySpeed = 5
