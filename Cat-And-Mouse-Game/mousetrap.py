import pygame,sys
import random
from pygame.locals import*
import time
 

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

catImg = pygame.image.load('cat.png')
catImg = pygame.transform.scale(catImg,(150,100))


class Cat(pygame.sprite.Sprite):

    def __init__(self, screen, width, height):

        super().__init__()
        self.image = catImg
        self.screen = screen
        self.rect = self.image.get_rect()
        self.speedx = random.randint(1,10)
        self.speedy = random.randint(1,10)

    def update(self):
        self.rect.left += self.speedx
        self.rect.top += self.speedy
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speedx *= -1
        if self.rect.bottom > self.screen.get_height() or self.rect.top < 0:
            self.speedy *= -1

    def collide(self,spriteGroup):
        if pygame.sprite.spritecollide(self,spriteGroup,False):
            self.speedy *= -1
            self.speedx *= -1
    


#___________________________________________________________________________

def main():
    pygame.init()

    lose = -1
    SCREENWIDTH = 1000
    SCREENHEIGHT = 1000
    BLOCK_WIDTH = 25
    BLOCK_HEIGHT = 25
    score = 0
    
    clock = pygame.time.Clock()
    x = 500
    y = 500
    x_change = 10
    y_change = 5
    mouseImg = pygame.image.load('mouse.png')
    mouseImg = pygame.transform.scale(mouseImg,(50,50))
    cheesex = 300
    cheesey = 300
    cheeseImg = pygame.image.load('cheese.png')
    cheeseImg = pygame.transform.scale(cheeseImg,(20,20))
    

    mainSurface = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),0,32)
    pygame.display.set_caption("Create Task")
    catsGroup = pygame.sprite.Group()

    def mouse(x,y):
        mainSurface.blit(mouseImg,(x,y))
    def cheese(cheesex,cheesey):
        mainSurface.blit(cheeseImg,(cheesex,cheesey))

    myCat = Cat(mainSurface,BLOCK_WIDTH,BLOCK_HEIGHT)
    myCat.rect.x = random.randrange(SCREENWIDTH - BLOCK_WIDTH)
    myCat.rect.y = random.randrange(SCREENHEIGHT - BLOCK_HEIGHT)
    catsGroup.add(myCat)
#___________________________________________________________________________
    while lose == -1:
        mainSurface.fill(WHITE)
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 70)
        titlesurface = myfont.render('You are the mouse', False, (0, 0, 0))
        mainSurface.blit(titlesurface,(300,300))
        Infosurface = myfont.render('Use the arrow keys to get cheese', False,(0,0,0))
        Infoosurface = myfont.render('Avoid the cats', False,(0,0,0))
        mainSurface.blit(Infosurface,(200,400))
        mainSurface.blit(Infoosurface,(300,500))
        clicksurface = myfont.render('click any key to continue',False,(0,0,0))
        mainSurface.blit(clicksurface,(300,600))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                lose += 1

    while lose == 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_DOWN:
                    y_change = 10
                elif event.key == pygame.K_UP:
                    y_change = -10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        x+=x_change
        y+=y_change

        
        mainSurface.fill((255,255,255))

        mouse(x,y)
        if -25<cheesex-x<25 and -25<cheesey-y<25:
            cheesex = random.randint(250,750)
            cheesey = random.randint(250,750)
            score+=1
            print(str(score))
            if score%10==0 and score > 0:
                myCat = Cat(mainSurface,BLOCK_WIDTH,BLOCK_HEIGHT)
                myCat.rect.x = random.randrange(SCREENWIDTH - BLOCK_WIDTH)
                myCat.rect.y = random.randrange(SCREENHEIGHT - BLOCK_HEIGHT)
                catsGroup.add(myCat)
        cheese(cheesex,cheesey)
        for aCat in catsGroup:
            if -25<x-aCat.rect.x<25 and -25<y-aCat.rect.y<25:
                lose += 1

        for aCat in catsGroup:
            catsGroup.remove(aCat)
            aCat.collide(catsGroup)
            catsGroup.add(aCat)
        
        catsGroup.update()
        catsGroup.draw(mainSurface)
        pygame.display.update()
        clock.tick(60)
    while lose == 1:
        mainSurface.fill(WHITE)
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 100)
        textsurface = myfont.render('You Lose', False, (0, 0, 0))
        mainSurface.blit(textsurface,(400,400))
        scoresurface = myfont.render('Score: '+str(score), False,(0,0,0))
        mainSurface.blit(scoresurface,(400,600))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            

main()



