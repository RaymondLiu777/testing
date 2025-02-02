import pygame, sys


class Player(pygame.sprite.Sprite):

  def __init__(self, x, y, w, h):
    #constructor
    super().__init__()
    self.rect = pygame.Rect(x, y, w, h)
    self.change_x = 0
    self.change_y = 0
    self.on_ground = True
    self.won_game = False
    self.font = pygame.font.SysFont("Ariel", 50)
    self.text = self.font.render("You win!", False, "green")
    self.image = pygame.image.load("pixil-frame-0(1).png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (40, 40))
    print(self.image.get_rect())

  def draw(self, screen):
    if self.won_game == True:
      pygame.draw.rect(screen, "green", self.rect)
      screen.blit(self.text, (200, 250))
      self.on_ground = True
    elif self.on_ground == True:
      # pygame.draw.rect(screen, "red", self.rect)
      
      screen.blit(self.image, (self.rect.x, self.rect.y))
    else:
      pygame.draw.rect(screen, "blue", self.rect)

  def update(self):
    # gravity
    if self.change_y == 0:
      self.change_y = 1
    else:
      self.change_y += 0.35
    # detect on ground
    if self.rect.y >= 500 - self.rect.height and self.change_y >= 0:
      self.change_y = 0
      self.rect.y = 500 - self.rect.height
      self.on_ground = True
    self.rect.y += self.change_y

    # movement
    self.rect.x += self.change_x

  def platform_collide(self, platform):
    if self.rect.colliderect(platform.rect):
      # If Player hits left of platform
      if platform.rect.x <= self.rect.x + self.rect.width <= platform.rect.x + 5:
        self.rect.x = platform.rect.x - self.rect.width
      elif platform.rect.x + platform.rect.width - 5 <= self.rect.x <= platform.rect.x + platform.rect.width:
        self.rect.x = platform.rect.x + platform.rect.width
      else:
        # reset position of block based on jump/fall
        # falling reset position
        if self.change_y > 0:
          self.rect.y = platform.rect.y - self.rect.height
          self.on_ground = True
        # jumping reset position
        elif self.change_y < 0:
          self.rect.y = platform.rect.y + platform.rect.height

        # set gravity to 0
        self.change_y = 0

  def goal_collide(self, goal):
    if self.rect.colliderect(goal.rect):
      self.won_game = True
      goal.visible = False


class Platform(pygame.sprite.Sprite):

  def __init__(self, x, y, w, h):
    #constructor
    super().__init__()
    self.rect = pygame.Rect(x, y, w, h)

  def draw(self, screen):
    pygame.draw.rect(screen, "black", self.rect)


class Goal(pygame.sprite.Sprite):

  def __init__(self, x, y, w, h):
    #constructor
    super().__init__()
    self.rect = pygame.Rect(x, y, w, h)
    self.visible = True

  def draw(self, screen):
    if self.visible == True:
      pygame.draw.rect(screen, "green", self.rect)
