import pygame, sys, math
pygame.init()

WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))  #1280 x 1024
font = pygame.font.Font('freesansbold.ttf', 32)

# backrground
bg_color = (255, 0, 255)
# Title and Icons:
pygame.display.set_caption("Danny's Second Game! - Derpy cookie Clicker")

# icon
icon = pygame.image.load('window_icon.png')  # imports image
pygame.display.set_icon(icon)


# COOKIE
cookie_Img = pygame.image.load('cookieImg.png')   # imports image
cookieX = WIDTH * 1/12
cookieY = (HEIGHT / 2) - 128

#counter
numCookies = 0
counterX = 120
counterY = 200


#Cookies per click
CookiesPerClickX = 110
CookiesPerClickY = 150
cookiesPerClick = 1
cookiesPerClick = round(cookiesPerClick, 2)

#upgrade_1
grandma_Img = pygame.image.load('grandma.png')
grandmaCost = 25
grandmaX = 950
grandmaY = HEIGHT - 600
# background 
background = pygame.image.load('cookie-clicker_bg.png')

#FUNCTIONS -----------------------------------------------------------
#cookie drawing
def cookie(x, y):
    screen.blit(cookie_Img, (x, y))  # blit means to draw
def cookieCounter(x, y):
    # remeber to convert to string   (typecasting)
    show_Counter = font.render("Cookies : " + str(round(numCookies, 2)), True, (255, 255, 255))
    screen.blit(show_Counter, (x, y))
def cookiesPerClick_counter(x, y):
    # remeber to convert to string   (typecasting)
    show_clicks = font.render("Cookies Per Click : " + str(round(cookiesPerClick, 2)), True, (255, 255, 255))
    screen.blit(show_clicks, (x, y))
def upgrade_1(x, y):
    screen.blit(grandma_Img, (x, y))  # blit means to draw
def upgrade_1_show(x, y):
    grandmaCost_show = font.render("Grandma Cost : " + str(round(grandmaCost, 2)), True, (255, 255, 255))
    screen.blit(grandmaCost_show, (x, y))


    #Instead of using distance formula or a hitbox in a function is just put it in the if then
    #the function seemed to mess things up???
    #----------------------------------------------------------------------------------------------------------------------------------------
""" def cookieClicked(cookieX, cookieY, mouseX, mouseY):
    distance = math.sqrt(math.pow(cookieX - mouseX, 2) +(math.pow(cookieY - mouseY, 2)))  # distance formula
    if distance < 10:
        return True
    else:
        return False """
"""def cookieClicked(cookieX, cookieY, mouseX, mouseY):
    if 145 < mouseX < 410 and 270 < mouseY < 530:
        return True
    else:
        return False
cookieClicked == False"""
    #-------------------------------------------------------------------------------------------------------------------------------------------------


# GAME LOOP:
 # first 2 lines makes it loop untill "running" = false
running = True
while running == True:
    # background makes things in the loop wayyyy slower because it takes more time too load
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        # makes the window stay open until the x has been pressed.
        if event.type == pygame.QUIT:
            running = False  # when running is false it ends the event loop
        mouseX, mouseY = pygame.mouse.get_pos()
#clicker:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 145 < mouseX < 410 and 270 < mouseY < 530:    #cookie pressed
                numCookies += cookiesPerClick
            if grandmaX < mouseX < (grandmaX + 125) and grandmaY < mouseY < (grandmaY + 130):
                if numCookies >= grandmaCost:
                    cookiesPerClick += cookiesPerClick * 0.10
                    numCookies -= grandmaCost
                    grandmaCost += grandmaCost * 0.20
            
    print(mouseX, ",", mouseY)
    cookie(cookieX, cookieY)
    upgrade_1(grandmaX, grandmaY)
    upgrade_1_show(grandmaX - 110, grandmaY - 50)
    cookiesPerClick_counter(CookiesPerClickX, CookiesPerClickY)
    cookieCounter(counterX, counterY)
    # everyhting must be before the background so it appears above it
    pygame.display.update()