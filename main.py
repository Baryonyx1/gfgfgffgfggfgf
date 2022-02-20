from pygame import *
from random import randint
font.init()


class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s]and self.rect.y < win_width - 80:
            self.rect.y += self.speed
        if keys_pressed[K_a]and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d]and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys_pressed[K_UP]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]and self.rect.y < win_width - 80:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT]and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT]and self.rect.x < win_width - 80:
            self.rect.x += self.speed
            
class enemy(Gamesprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >=  win_width -85:
            self.direction = 'left'

        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class stenka(sprite.Sprite):
    def __init__(self,r,g,b,wid,hei,xx,yy,):
        super().__init__()
        self.r = r
        self.g = g
        self.b = b
        self.width = wid
        self.height = hei
        self.image = Surface((self.width, self.height))
        self.image.fill((r,g,b))
        self.rect = self.image.get_rect()

        self.rect.x = xx
        self.rect.y = yy
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))




#text
font = font.Font(None,70)
win = font.render('ТЫ НИГЕР',True,(255, 255, 255))

lose = font.render('ТЫ ЛОХ',True,(255, 255, 255))
dd = font.render('ЗАНОВОООО',True,(0,0,0))

        







win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))


player = Player('hero.png',5, win_height - 80, 4)
monster = enemy('cyborg.png', win_width - 80,280,2)
final = Gamesprite("treasure.png", win_width - 120,win_height - 80,0)
st1 = stenka(79,89,57,56,67,56,90)
st2 = stenka(79,89,57,56,67,80,159)
st3 = stenka(79,89,57,56,67,250,300)
st = [st1,st2,st3]
h1 = Gamesprite("i.jpeg", win_width - 300,win_height - 500,0)
h2 = Gamesprite("i.jpeg", win_width - 200,win_height - 500,0)
h3 = Gamesprite("i.jpeg", win_width - 100,win_height - 500,0)
game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')

mixer.music.play()
kick = mixer.Sound('kick.ogg')
moey = mixer.Sound('money.ogg')
h = False
l = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    if h != True:
        player.update()
        monster.update()
        if l == 0:
            h1.update()
            h1.reset()
        if l  <= 1:
            h2.update()
            h2.reset()
        if l != 3:
            h3.update()
            h3.reset()
        st1.draw_wall()
        st2.draw_wall()
        st3.draw_wall()
        
        
        final.reset()
        player.reset()
        monster.reset()
    
        
        if sprite.collide_rect(player, monster):
            h = True
            window.blit(lose,(220,220))
            kick.play()
            mixer.music.stop()
        elif sprite.collide_rect(player, final) :
            h = True
            window.blit(win,(220,220))
            moey.play()
            mixer.music.stop()
        for s in st:
            if sprite.collide_rect(player,s):
                l = l + 1
                window.blit(dd,(220,220))
                kick.play()
                player = Player('hero.png',5, win_height - 80, 4)
                
                
                
                    
                
                
                if l == 3:
                    h = True
                    window.blit(lose,(220,220))
        display.update()
        clock.tick(FPS)
