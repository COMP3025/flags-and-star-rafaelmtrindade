from shapes import *
from colors import *
from pygame import Surface

class _Flag:
  def __init__(self, display: Surface, w: int, h: int, offset=(0,0)):
    self.display = display
    self.w = w
    self.h = h
    self.offset = offset

  def draw(self):
    pass

class CzFlag(_Flag):
  def __init__(self, display: Surface, w: int, h: int, offset = (0, 0)):
    super().__init__(display, w, h, offset)

  def draw(self):
    w_45 = self.w * 0.45
    half_h = self.h // 2
    red_rect = Rectangle(RED,self.w, half_h)
    white_rect = Rectangle(WHITE, self.w, half_h)
    blue_triangle = Triangle(BLUE, ((0,0), (w_45, half_h), (0, self.h)))

    red_rect.draw(self.display, self.offset)
    white_rect.draw(self.display, (self.offset[0], self.offset[1] + half_h))
    blue_triangle.draw(self.display, self.offset)

class JpFlag(_Flag):
  def __init__(self, display: Surface, w: int, h: int, offset = (0, 0)):
    super().__init__(display, w, h, offset)

  def draw(self):
    elipse_rect = (
      self.offset[0] + (self.w // 3),
      self.offset[1] + (self.h // 4),
      self.w // 3,
      self.h // 2
    ) # 3:2 ratio, centered
    white_rect = Rectangle(WHITE, self.w, self.h)
    white_rect.draw(self.display, self.offset)
    pygame.draw.ellipse(self.display, RED, elipse_rect)

class ChFlag(_Flag):
  def __init__(self, display: Surface, w: int, h: int, offset = (0, 0)):
    super().__init__(display, w, h, offset)

  def draw(self):
    half_h = self.h // 2
    red_rect = Rectangle(RED,self.w, half_h)
    white_rect = Rectangle(WHITE, self.w, half_h)
    blue_sq = Rectangle(BLUE, half_h, half_h)
    white_star = Star(WHITE, half_h//8, half_h//3)

    white_rect.draw(self.display, self.offset)
    red_rect.draw(self.display, (self.offset[0], self.offset[1] + half_h))
    blue_sq.draw(self.display, self.offset)
    white_star.draw(self.display, (self.offset[0] + (half_h // 6), self.offset[1] + (half_h // 6)))

class CoFlag(_Flag):
  def __init__(self, display: Surface, w: int, h: int, offset = (0, 0)):
    super().__init__(display, w, h, offset)

  def draw(self):
    w_45 = self.w * 0.45
    half_h = self.h // 2
    quarter_h = self.h // 4
    star_radius = 12
    circle_radius = w_45 // 4
    star_h_offset = (half_h) - (star_radius * 2 * 2) - 4

    rectangles = (
      Rectangle(YELLOW, self.w, quarter_h),
      Rectangle(WHITE, self.w, quarter_h),
      Rectangle(RED,self.w, quarter_h),
      Rectangle(BLUE, self.w, quarter_h)
    )
    green_triangle = Triangle(GREEN, ((0,0), (w_45, half_h), (0, self.h)))
    white_circle = Circle(WHITE, circle_radius)
    green_circle = Circle(GREEN, circle_radius)
    white_star = Star(WHITE, star_radius* 5//12, star_radius)

    [rect.draw(self.display, (self.offset[0], self.offset[1] + (i * quarter_h))) for i, rect in enumerate(rectangles)]
    green_triangle.draw(self.display, self.offset)
    white_circle.draw(self.display, (self.offset[0] + w_45//8, self.offset[1] + half_h - circle_radius))
    green_circle.draw(self.display, (self.offset[0] + w_45//8 + w_45//10, self.offset[1] + half_h - circle_radius))

    for i in range(4):
      white_star.draw(self.display, (self.offset[0] + (w_45 // 2.5), self.offset[1] + star_h_offset + (i * star_radius * 2) + (i * 4)))