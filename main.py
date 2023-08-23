import sys

import pygame
from pygame.locals import QUIT

from flags import *
from shapes import Star
from math import pi as PI

pygame.init()
DISPLAY_SIZE = (640, 360)
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('Flags')

rotation = 0 # rads
star_animation_enabled = False
def draw_star(screen: pygame.Surface, size: int, position=(0,0), angle=0):
  """
  size: raio em pixels da estrela
  angle: ângulo em radianos para rotacionar a estrela
  """
  pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0, *DISPLAY_SIZE))
  star = Star((255,255,255), size*5//12, size, angle)
  star.draw(screen, position)

def animate_star():
  global rotation
  draw_star(DISPLAY, 120, (DISPLAY_SIZE[0]//3, DISPLAY_SIZE[1]//5), rotation)
  rotation += PI/6 % (2*PI) # rotacionar 30 graus por frame


def toggle_star_animation():
  global star_animation_enabled
  global rotation
  star_animation_enabled = not star_animation_enabled
  rotation = 0
  # 12 FPS
  pygame.time.set_timer(pygame.USEREVENT, 1000//12 if star_animation_enabled else 0)

key_functions = {
  pygame.K_c: CzFlag(DISPLAY, *DISPLAY_SIZE).draw,
  pygame.K_o: CoFlag(DISPLAY, *DISPLAY_SIZE).draw,
  pygame.K_j: JpFlag(DISPLAY, *DISPLAY_SIZE).draw,
  pygame.K_l: ChFlag(DISPLAY, *DISPLAY_SIZE).draw,
  pygame.K_s: toggle_star_animation
}

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key != pygame.K_s:
        star_animation_enabled = True
        toggle_star_animation()
      key_functions.get(event.key, lambda: None)()
    elif event.type == pygame.USEREVENT:
      animate_star()
    elif event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
