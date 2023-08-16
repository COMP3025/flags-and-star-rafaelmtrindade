import sys

import pygame
from pygame.locals import QUIT

from flags import CzFlag, JpFlag, ChFlag
from shapes import Star
from math import pi as PI

pygame.init()
DISPLAY_SIZE = (640, 360)
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('Flags')

rotation = 0 # rads
animate_star = False
def draw_star(screen: pygame.Surface, size: int, position=(0,0), angle=0):
  """
  size: raio em pixels da estrela
  angle: ângulo em radianos para rotacionar a estrela
  """
  pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0, *DISPLAY_SIZE))
  star = Star((255,255,255), size,size*12//5 , angle)
  star.draw(screen, position)

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_c:
        cz_flag = CzFlag(DISPLAY, *DISPLAY_SIZE)
        cz_flag.draw()
      elif event.key == pygame.K_j:
        jp_flag = JpFlag(DISPLAY, *DISPLAY_SIZE)
        jp_flag.draw()
      elif event.key == pygame.K_l:
        ch_flag = ChFlag(DISPLAY, *DISPLAY_SIZE)
        ch_flag.draw()
      elif event.key == pygame.K_s:
        draw_star(DISPLAY, 50, (DISPLAY_SIZE[0]//3, DISPLAY_SIZE[1]//5), rotation)
        animate_star = not animate_star
        pygame.time.set_timer(pygame.USEREVENT, 1000//12 if animate_star else 0)
        rotation = 0
    elif event.type == pygame.USEREVENT:
      # rotacionar 30 graus a cada 1/12 de segundo
      draw_star(DISPLAY, 50, (DISPLAY_SIZE[0]//3, DISPLAY_SIZE[1]//5), rotation)
      rotation += PI/6
    elif event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
