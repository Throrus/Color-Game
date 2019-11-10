import pygame
import random
import sys
import time

pygame.init()

#screen
win_width = 800
win_height = 500
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Color Game")

#images
s_up = pygame.image.load("selected_up.png")
s_up = pygame.transform.scale(s_up, (50, 40))
s_dwn = pygame.image.load("selected_down.png")
s_dwn = pygame.transform.scale(s_dwn, (50, 40))
up = pygame.image.load("up.png")
up = pygame.transform.scale(up, (50, 40))
dwn = pygame.image.load("down.png")
dwn = pygame.transform.scale(dwn, (50, 40))

#colors
random_color = (0, 0, 255)

def generate_color():
    global random_color
    first = random.randint(0, 255)
    second = random.randint(0, 255)
    third = random.randint(0, 255)
    random_color = (first, second, third)

class ColorPane:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

        self.standardFont = pygame.font.Font(None, 25)

        self.reset_text = self.standardFont.render(("RESET"), True, (0, 0, 0))
        self.red_text = self.standardFont.render(("RED"), True, (0, 0, 0))
        self.green_text = self.standardFont.render(("GREEN"), True, (0, 0, 0))
        self.blue_text = self.standardFont.render(("BLUE"), True, (0, 0, 0))

    def get_playerColor(self, red, green, blue):
        self.player_color = (red, green, blue)
        return self.player_color

    def get_redValue(self, redValue):
        self.redValue = redValue
        self.redValue_text = self.standardFont.render((str(self.redValue)), True, (0, 0, 0))
        return self.redValue_text

    def get_greenValue(self, greenValue):
        self.greenValue = greenValue
        self.greenValue_text = self.standardFont.render((str(self.greenValue)), True, (0, 0, 0))
        return self.greenValue_text

    def get_blueValue(self, blueValue):
        self.blueValue = blueValue
        self.blueValue_text = self.standardFont.render((str(self.blueValue)), True, (0, 0, 0))
        return self.blueValue_text

    def addRed(self):
        self.red += 1

    def addGreen(self):
        self.green += 1

    def addBlue(self):
        self.blue += 1

    def subRed(self):
        self.red -= 1

    def subGreen(self):
        self.green -= 1

    def subBlue(self):
        self.blue -= 1

    def drawColor(self):
        pygame.draw.rect(screen, self.player_color, (0, 250, 800, 250))

    def drawValue(self, name, pos):
        screen.blit(name, (pos))

    def drawText(self, text, pos):
        screen.blit(text, (pos))

    def reset_color(self):
        self.red = 0
        self.green = 0
        self.blue = 0
        return self.red
        return self.green
        return self.blue



playerPane = ColorPane()

#button states
rup = False
rdwn = False
gup = False
gdwn = False
bup = False
bdwn = False

def refresh_window():

    pygame.draw.rect(screen, random_color, (0, 0, 800, 250))
    playerPane.get_playerColor(playerPane.red, playerPane.green, playerPane.blue)
    playerPane.drawColor()

    playerPane.drawText(playerPane.reset_text, (700, 23))

    pygame.draw.rect(screen, (255, 255, 255), (258, 344, 60, 113))
    pygame.draw.rect(screen, (255, 255, 255), (370, 344, 60, 113))
    pygame.draw.rect(screen, (255, 255, 255), (483, 344, 60, 113))

    playerPane.drawText(playerPane.red_text, (271, 380))
    playerPane.drawText(playerPane.green_text, (370, 380))
    playerPane.drawText(playerPane.blue_text, (491, 380))

    playerPane.get_redValue(playerPane.red)
    playerPane.drawValue(playerPane.redValue_text, (273, 400))
    playerPane.get_greenValue(playerPane.green)
    playerPane.drawValue(playerPane.greenValue_text, (385, 400))
    playerPane.get_blueValue(playerPane.blue)
    playerPane.drawValue(playerPane.blueValue_text, (497, 400))

    if rup:
        screen.blit(s_up, (263, 340))
    else:
        screen.blit(up, (263, 340))
    if rdwn:
        screen.blit(s_dwn, (263, 418))
    else:
        screen.blit(dwn, (263, 418))

    if gup:
        screen.blit(s_up, (375, 340))
    else:
        screen.blit(up, (375, 340))
    if gdwn:
        screen.blit(s_dwn, (375, 418))
    else:
        screen.blit(dwn, (375, 418))

    if bup:
        screen.blit(s_up, (488, 340))
    else:
        screen.blit(up, (488, 340))
    if bdwn:
        screen.blit(s_dwn, (488, 418))
    else:
        screen.blit(dwn, (488, 418))

    pygame.display.update()

accel_timer = 0
first_time = 0
dur_time = 0

run = True
while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if mx >= 700 and mx <= 755 and my >=25 and my <=36:
                    generate_color()
                    playerPane.reset_color()

            if event.type == pygame.MOUSEBUTTONUP:
                accel_timer = 0
                first_time = 0
                dur_time = 0
                rup = False
                rdwn = False
                gup = False
                gdwn = False
                bup = False
                bdwn = False

            if event.type == pygame.QUIT:
                    sys.exit()

        if pygame.mouse.get_pressed()[0]:
            mx,my = pygame.mouse.get_pos()
            try:
                if mx >= 263 and mx <= 313 and my >=340 and my <=380:
                    rup = True
                    if playerPane.red >= 255:
                        pass
                    else:
                        if accel_timer == 0 and first_time == 0:
                            playerPane.addRed()
                            accel_timer += 1
                            first_time += 1
                        elif first_time >= 1 and accel_timer == 0 and dur_time >= 100:
                            playerPane.addRed()
                            accel_timer += 1
                        elif accel_timer >= 50:
                            accel_timer = 0
                        else:
                            accel_timer += 1
                        dur_time += 1
                if mx >= 375 and mx <= 425 and my >=340 and my <=380:
                    gup = True
                    if playerPane.green >= 255:
                        pass
                    else:
                        if accel_timer == 0 and first_time == 0:
                            playerPane.addGreen()
                            accel_timer += 1
                            first_time += 1
                        elif first_time >= 1 and accel_timer == 0 and dur_time >= 100:
                            playerPane.addGreen()
                            accel_timer += 1
                        elif accel_timer >= 50:
                            accel_timer = 0
                        else:
                            accel_timer += 1
                        dur_time += 1
                if mx >= 488 and mx <= 538 and my >=340 and my <=380:
                    bup = True
                    if playerPane.blue >= 255:
                        pass
                    else:
                        if accel_timer == 0 and first_time == 0:
                            playerPane.addBlue()
                            accel_timer += 1
                            first_time += 1
                        elif first_time >= 1 and accel_timer == 0 and dur_time >= 100:
                            playerPane.addBlue()
                            accel_timer += 1
                        elif accel_timer >= 50:
                            accel_timer = 0
                        else:
                            accel_timer += 1
                        dur_time += 1
                if mx >= 263 and mx <= 313 and my >=418 and my <=458:
                    rdwn = True
                    if playerPane.red <= 0:
                        pass
                    else:
                        if accel_timer == 0 and first_time == 0:
                            playerPane.subRed()
                            accel_timer += 1
                            first_time += 1
                        elif first_time >= 1 and accel_timer == 0 and dur_time >= 100:
                            playerPane.subRed()
                            accel_timer += 1
                        elif accel_timer >= 50:
                            accel_timer = 0
                        else:
                            accel_timer += 1
                        dur_time += 1
                if mx >= 375 and mx <= 425 and my >=418 and my <=458:
                    gdwn = True
                    if playerPane.green <= 0:
                        pass
                    else:
                        if accel_timer == 0 and first_time == 0:
                            playerPane.subGreen()
                            accel_timer += 1
                            first_time += 1
                        elif first_time >= 1 and accel_timer == 0 and dur_time >= 100:
                            playerPane.subGreen()
                            accel_timer += 1
                        elif accel_timer >= 50:
                            accel_timer = 0
                        else:
                            accel_timer += 1
                        dur_time += 1
                if mx >= 488 and mx <= 538 and my >=418 and my <=458:
                    bdwn = True
                    if playerPane.blue <= 0:
                        pass
                    else:
                        if accel_timer == 0 and first_time == 0:
                            playerPane.subBlue()
                            accel_timer += 1
                            first_time += 1
                        elif first_time >= 1 and accel_timer == 0 and dur_time >= 100:
                            playerPane.subBlue()
                            accel_timer += 1
                        elif accel_timer >= 50:
                            accel_timer = 0
                        else:
                            accel_timer += 1
                        dur_time += 1
            except AttributeError:
                pass

        refresh_window()
