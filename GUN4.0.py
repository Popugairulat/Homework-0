import math

import pygame
import random
import cmath
p=1
q=0 
width = 1200
height = 720
screen = pygame.display.set_mode((width, height))

color_life = [(0, 0, 0), (178, 44, 0), (178, 111, 0), (156, 178, 0)]
color_level = [(10, 149, 204), (10, 197, 204), (10, 204, 129), (10, 204, 26), (204, 204, 10), (204, 162, 10), (204, 126, 10), (204, 84, 10), (204, 48, 10), (204, 10, 90)]

v_target = [1, 1, 1.5, 1.5, 2, 2, 10, 0.5, 2, 2]
faculty =["ФРКТ", "ФЭФМ", "ФБМФ", "ФПМИ", "ФБВТ", "ВШПИ", "ФИВТ", "ФПФЭ"]
level = 0

number=0

class Score:

    def __init__(self, screen: pygame.Surface, level):
        self.screen = screen
        self.score = 0
        self.life = 3
        self.level = level
        self.color_life = color_life[self.life-1]

    def draw(self):
        pygame.draw.rect(self.screen, (191, 191, 191), (0, 0, 1200, 100))
        pygame.draw.rect(self.screen, (38, 38, 38), (180, 50, 1000, 40), 5)
        for i in range(self.level):
            pygame.draw.rect(self.screen, color_level[i], (185+i*99*10/8, 55, 99*10/8, 30))
        score = font.render("Score : "+str(self.score), True, (0, 0, 0))
        screen.blit(score, (20, 20))
        life = font.render("Life : " + str(round(self.life)), True, color_life[round(self.life)])
        screen.blit(life, (20, 57))
        level = font.render("Level : " + str(self.level+1), True, (0, 0, 0))
        screen.blit(level, (600, 20))
        pygame.draw.line(self.screen, (0, 0, 0), (0, 640), (1200, 640), 3)

class Gun:
    def __init__(self, screen: pygame.Surface, x, a):
        self.screen = screen
        self.x = x
        self.vx = 0
        self.angle = a
        self.color = (0, 0, 0)

    def draw(self):
        pygame.draw.circle(self.screen, self.color,(self.x, 704),16, 5)
        pygame.draw.circle(self.screen, self.color,(self.x, 704),5, 5)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x-12, 703, 23, 2), 2)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x-1, 704-12, 2, 24), 2)
        angle1 = (self.angle+8)/180*math.pi
        angle2 = (self.angle - 8) / 180 * math.pi
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.x + 50 * math.cos(angle1), 704 - 50 * math.sin(angle1)), ( self.x + 50 * math.cos(angle2), 704 - 50 * math.sin(angle2)), (self.x - 16 * math.cos(angle1), 704 + 16 * math.sin(angle1)), (self.x - 16 * math.cos(angle2), 704 + 16 * math.sin(angle2))])

    def move(self):
        self.x += self.vx

class Target:
    def __init__(self, screen: pygame.Surface, level):
        self.screen = screen
        self.level_dop = 0
        self.x = random.randint(60, 1000)
        self.y = random.randint(120, 600)
        self.width = 120
        self.height = 40
        self.angle = random.randint(0, 180)/180*math.pi
        self.level = level
        self.vx = v_target[self.level] * math.cos(self.angle)
        self.vy = v_target[self.level] * math.sin(self.angle)
        self.color = (0, 0, 0)

    def draw(self):
        if self.level_dop == 0:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 5)
            text = font.render(faculty[self.level], True, self.color)
            screen.blit(text, (self.x+10, self.y+5))
        else:
            if self.level==2:
                pygame.draw.circle(self.screen, (69, 139, 0), (self.x + 20, self.y + 20), 20)
                pygame.draw.ellipse(self.screen, (69, 139, 0), (self.x + 1, self.y - 2, 12, 22))
                pygame.draw.ellipse(self.screen, (255, 255, 255), (self.x + 3, self.y + 3, 8, 11))
                pygame.draw.ellipse(self.screen, (69, 139, 0), (self.x + 27, self.y - 2, 12, 22))
                pygame.draw.ellipse(self.screen, (255, 255, 255), (self.x + 29, self.y + 3, 8, 11))
                pygame.draw.ellipse(self.screen, (255, 158, 140), (self.x + 14, self.y + 10, 12, 18))
                pygame.draw.rect(self.screen, (69, 139, 0), (self.x + 14, self.y + 10, 12, 9))
                pygame.draw.ellipse(self.screen, (69, 139, 0), (self.x + 35, self.y + 18, 12, 25))
                pygame.draw.ellipse(self.screen, (69, 139, 0), (self.x - 5, self.y + 18, 12, 25))
            elif self.level==3:
                pygame.draw.rect(self.screen, color_level[random.randint(0, 7)], (self.x, self.y, self.width, self.height), 5)
                text = font.render(faculty[self.level], True, color_level[random.randint(0, 7)])
                screen.blit(text, (self.x + 10, self.y + 5))
            elif self.level==4:
                pygame.draw.rect(self.screen, (255, 211, 150), (self.x, self.y, self.width, self.height), 5)
                text = font.render(faculty[self.level], True, (255, 211, 150))
                screen.blit(text, (self.x + 10, self.y + 5))
                text = font.render(" AXAXA ", True, (0, 0, 0))
                screen.blit(text, (600, 350))
                text = font.render("FIND ME", True, (0, 0, 0))
                screen.blit(text, (600, 380))
            elif self.level==7:
                pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 5)
                text = font.render(faculty[self.level], True, self.color)
                screen.blit(text, (self.x + 10, self.y + 5))


    def move(self):
        if self.x + self.width >= width or self.x <= 0:
            self.vx = - self.vx
        elif self.y + self.height >= height-80 or self.y <= 100:
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy

class Ball:
    def __init__(self, screen: pygame.Surface, x, a, type ):
        self.screen = screen
        self.x = x
        self.y = 704
        self.angle = a
        self.type = type
        self.vr = [0, 0.08][self.type]
        self.vx = [3, 1][self.type] * math.cos(self.angle/180*math.pi)
        self.vy = -[3, 1][self.type] * math.sin(self.angle/180*math.pi)
        self.r = [6, 10][self.type]

    def draw(self):
        if self.type == 0:
            pygame.draw.circle(self.screen, (200, 0, 0), (self.x, self.y), self.r)
        elif self.type == 1:
            pygame.draw.circle(self.screen, (255, 200, 0), (self.x, self.y), self.r)
            pygame.draw.circle(self.screen, (200, 0, 0), (self.x, self.y), self.r, 4)

    def move(self):
        if self.x + self.r >= width or self.x - self.r <= 0:
            self.vx = - self.vx
        elif self.y + self.r >= height or self.y - self.r <= 100:
            self.vy = -self.vy
        self.x += self.vx
        self.vy +=[0.008, 0.001][self.type]
        self.y += self.vy
        if self.r <= 100:
            self.r += self.vr

def draw_move(object):
    i = 0
    while i < len(object):
        object[i].draw()
        object[i].move()
        i+=1

def normal_crash(balls, targets, i, j, scors):
    if len(targets)==1:
        targets[j].level += 1
        targets.append(Target(screen, targets[j].level))

    scors.score+=1

    targets.pop(j)
    balls.pop(i)
def bio_crash(balls, targets, i, j, scors):
    if targets[j].level_dop == 0:
        targets.append(Target(screen, targets[j].level))
        targets.append(Target(screen, targets[j].level))
        targets.append(Target(screen, targets[j].level))
        targets.append(Target(screen, targets[j].level))
        targets.pop(j)
        balls.pop(i)
        for r in range (4):
            targets[j+r].level_dop=1
            targets[j+r].width=40
    else:
        normal_crash(balls, targets, i, j, scors)


def disko_crash(balls, targets, i, j, scors):
    if targets[j].level_dop==0:
        targets.append(Target(screen, targets[j].level))
        targets[j+1].level_dop =1
        targets.pop(j)
        balls.pop(i)
    else:
        normal_crash(balls, targets, i, j, scors)

def fpf_crash(balls, targets, i, j, scors):
    if len(targets)<150:
        for y in range(len(targets)):
            targets.append(Target(screen, targets[j].level))
        balls.pop(i)

    else:
        screen.fill((255, 211, 150))
        text = font.render("YOU ARE LOOSE ", True, (255, 0, 0))
        screen.blit(text, (500, 350))
        pygame.display.update()

def crash_ball_with_target(balls, targets, number):
    i, j = 0, 0
    while j < len(targets):
        if len(balls)>0:
            b = balls[i]
            t = targets[j]
            if b.x + b.r >= t.x and b.x - b.r <= t.x + t.width and b.y + b.r >= t.y and b.y - b.r <= t.y + t.height:
                if t.level in (0, 5, 1,  6):
                    normal_crash(balls, targets, i, j, scors)
                elif t.level == 2:
                    bio_crash(balls, targets, i, j, scors)
                elif t.level == 3:
                    disko_crash(balls, targets, i, j, scors)
                elif t.level == 4:
                    disko_crash(balls, targets, i, j, scors)
                else:
                    fpf_crash(balls, targets, i, j, scors)
                j = 0

        j+=1

def crash_ball_with_gun(balls, guns, scors):
    i, j = 0, 0
    while j < 2:
        if len(balls)>0:
            b = balls[i]
            t = guns[j]
            if b.x + b.r >= t.x -30 and b.x - b.r <= t.x +30  and b.y + b.r >= 690 and b.y - b.r <= 720 and b.vy>0:
                scors.life -= 1
                balls.pop(i)

                j=0
        j+=1


pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()

targets = [Target(screen, level)]
guns = [Gun(screen, 250, 30), Gun(screen, 950, 150)]
balls = []
scors = Score(screen, targets[0].level)
while True:
    if scors.life>=1:
        screen.fill((255, 211, 150))

        scors.level=targets[0].level
        scors.draw()
        draw_move(guns)
        draw_move(targets)
        draw_move(balls)

        crash_ball_with_target(balls, targets,  scors)
        crash_ball_with_gun(balls, guns, scors)

        clock.tick(300)
        pygame.display.update()

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif keys[pygame.K_l]:
                q = 0
            elif keys[pygame.K_r]:
                q = 1
            elif keys[pygame.K_SPACE]:
                balls = [(Ball(screen, guns[q].x, guns[q].angle, 0))]
            elif keys[pygame.K_ESCAPE]:
                balls = [(Ball(screen, guns[q].x, guns[q].angle, 1))]
            elif keys[pygame.K_UP]:
                guns[q].angle += 10
            elif keys[pygame.K_DOWN]:
                guns[q].angle -= 10
            elif keys[pygame.K_LEFT]:
                guns[q].x -= 10
            elif keys[pygame.K_RIGHT]:
                guns[q].x += 10
    else:
        screen.fill((255, 211, 150))
        pygame.display.update()
        text = font.render("YOU ARE LOOSE", True, (250, 0, 0))
        text.blit(text, (600, 300))
        p=0
    while p==0:
        text = font.render("YOU ARE LOOSE ", True, (255, 0, 0))
        screen.blit(text, (500, 350))
        pygame.display.update()



pygame.quit()