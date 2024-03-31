from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= 1
        if keys_pressed[K_s]:
            self.rect.y += 1
        if keys_pressed[K_a]:
            self.rect.x -= 1
        if keys_pressed[K_d]:
            self.rect.x += 1


        
clock = time.Clock()
window = display.set_mode((700, 500))
display.set_caption("Шарик")
background = transform.scale(image.load("fon.jpg"), (700, 500))


sprite1 = Player('', 250, 400, 7)


FPS = 60

mixer.init()
mixer.music.load('zadni_fon.mp3')
mixer.music.play()

score = 0
missing = 0

font.init()
font = font.Font(None, 50)
lose = font.render('ЛОШАРА', True, (255, 255, 255))





game = True

finish = False
while game:
    if not finish:
        window.blit(background, (0, 0))
        sprite1.update()


    display.update()
    clock.tick(FPS)
