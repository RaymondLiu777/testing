import pygame, sys
from pygame.locals import QUIT
from Sprites import *

pygame.init()
pygame.font.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption('Platform Jumper')
b1 = Player(0, 460, 40, 40)
platforms = [
    Platform(180, 380, 300, 20),
    Platform(100, 270, 200, 20),
    Platform(250, 170, 100, 20),
    Platform(400, 100, 50, 20),
]
goal = Goal(415, 30, 20, 20)
#platform = Platform(100, 300, 100, 20)
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        b1.change_x = -5
      if event.key == pygame.K_RIGHT:
        b1.change_x = 5
      if event.key == pygame.K_UP and b1.on_ground == True:
        b1.change_y = -10
        b1.on_ground = False
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        b1.change_x = 0

  DISPLAYSURF.fill("white")
  b1.update()
  for platform in platforms:
    b1.platform_collide(platform)
    platform.draw(DISPLAYSURF)
  b1.draw(DISPLAYSURF)
  b1.goal_collide(goal)
  goal.draw(DISPLAYSURF)

  pygame.display.update()
  clock.tick(60)
