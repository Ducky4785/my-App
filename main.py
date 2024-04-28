from pygame import *
from random import randint

score = 0
health = 3
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.speedX = player_speed
        self.speedY = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.rect.x -= 5
        if keys_pressed[K_RIGHT]:
            self.rect.x += 5

class Enemy(GameSprite):
    directionY = 'down'
    def update(self):
        global health
        self.rect.x += self.speedX
        self.rect.y += self.speedY

        if self.rect.x >= 650:
            self.speedX *= -1
        if self.rect.x <= 0:
            self.speedX *= -1
        if self.directionY == 'up':
            if self.rect.y <= 0:
                self.speedY *= -1

        
        if self.rect.y >= 499:
            self.rect.y = randint(-200, 50)
            self.rect.x = randint(0, 650)
            health -= 1
            self.directionY = 'down'
        
        if sprite.collide_rect(self, sprite1):
            self.speedY *= -1
            self.directionY = 'up'


mixer.init()
otskok = mixer.Sound('otskok.mp3')

mixer.music.load('music.mp3')
mixer.music.play()



clock = time.Clock()
window = display.set_mode((700, 500))
display.set_caption("Пинг понг")
background = transform.scale(image.load("Fon.jpg"), (700, 500))


sprite1 = Player('Player_dos.png', 250, 400, 7)

Enemys = sprite.Group()
for i in range(1):
    EnemyE = Enemy('sharik.png', randint(0, 650), randint(-200, -50), randint(3, 4))
    Enemys.add(EnemyE)

bullets = sprite.Group()

FPS = 60

    

font.init()
font = font.Font(None, 50)

lose = font.render('+1', True, (255, 255, 255))
final_text = font.render('Ты проиграл', True, (255, 255, 255))


game = True

finish = False
while game:
    if not finish:
        window.blit(background, (0, 0))
        sprite1.reset()
        sprite1.update()
        Enemys.update()
        Enemys.draw(window)
        


    schet = font.render('Счет: '+ str(score), True, (255, 255, 255))
    propysh = font.render('Жизней: ' + str(health), True, (255, 255, 255))
    window.blit(schet, (10, 20))
    window.blit(propysh, (10, 50))

    for j in Enemys:
        if sprite.collide_rect(sprite1, j):
            window.blit(lose, (200, 0))
            score += 1
            otskok.play()

    if health <= 0:
        window.blit(final_text, (250, 200))
        finish = True


    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
