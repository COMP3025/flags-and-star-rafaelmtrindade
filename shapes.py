from colors import ColorRGB
from typing import Iterable
from math import pi as PI, cos, sin
import pygame

class Shape:
  def __init__(self, color: ColorRGB, rotation=0, scale=1.0, alpha=1.0, fill=True, line_width=1):
    if isinstance(color, ColorRGB):
      self.color = color
    elif isinstance(color, Iterable) and len(color) == 3:
      self.color = ColorRGB(*color)
    else:
      raise ValueError("Color must be an RGB tuple or ColorRGB object")
    self.rotation = rotation
    self._scale = scale
    self.alpha = alpha
    self._fill = fill
    self.line_width = line_width

  def rotate_deg(self, degrees):
    rads = degrees * PI / 180
    self.rotate(rads)

  def rotate(self, radians):
    # rotate the shape and clamp to interval [0, 2pi)
    self.rotation = (self.rotation + radians) % (2 * PI)

  def scale(self, factor: float):
    self._scale *= factor

  def set_scale(self, scale = 1.0):
    self._scale = scale

  def set_alpha(self, alpha: float):
    self.alpha = alpha

  def fill(self):
    self._fill = True

  def no_fill(self):
    self._fill = False

  def draw(self, canvas, offset=(0,0)):
    pass

  def __repr__(self):
    return f"{self.__class__.__name__}(color={self.color}, rotation={self.rotation}, scale={self._scale}, alpha={self.alpha}, fill={self._fill}, line_width={self.line_width})"

class Circle(Shape):
  def __init__(self, color: ColorRGB, radius=1, rotation=0, scale=1.0, alpha=1.0, fill=True, line_width=1):
    super().__init__(color, rotation, scale, alpha, fill, line_width)
    self.radius = radius

  def draw(self, canvas: pygame.Surface, offset=(0,0)):
    # offset is location of top left corner of canvas
    real_radius = self.radius * self._scale
    center = (offset[0] + real_radius, offset[1] + real_radius)
    pygame.draw.circle(canvas, self.color, center, real_radius, 0 if self._fill else self.line_width)

  def __repr__(self):
    return f"{self.__class__.__name__}(color={self.color}, radius={self.radius}, rotation={self.rotation}, scale={self._scale}, alpha={self.alpha}, fill={self._fill}, line_width={self.line_width})"

class Rectangle(Shape):
  def __init__(self, color: ColorRGB, w=1, h=1, rotation=0, scale=1.0, alpha=1.0, fill=True, line_width=1):
    super().__init__(color, rotation, scale, alpha, fill, line_width)
    self.width = w
    self.height = h

  def draw(self, canvas: pygame.Surface, offset=(0,0)):
    # offset is location of top left corner of canvas
    real_width = self.width * self._scale
    real_height = self.height * self._scale
    pygame.draw.rect(canvas, self.color, (offset[0], offset[1], real_width, real_height), 0 if self._fill else self.line_width)

  def __repr__(self):
    return f"{self.__class__.__name__}(color={self.color}, width={self.width}, height={self.height}, rotation={self.rotation}, scale={self._scale}, alpha={self.alpha}, fill={self._fill}, line_width={self.line_width})"


class Star(Shape):
  # control the inner and outer radius of the star, the bigger the difference, the more pointy the star
  def __init__(self, color: ColorRGB, inner_radius=1, outer_radius=2, rotation=0, scale=1.0, alpha=1.0, fill=True, line_width=1):
    super().__init__(color, rotation, scale, alpha, fill, line_width)
    self.inner_radius = inner_radius
    self.outer_radius = outer_radius

  def draw(self, canvas: pygame.Surface, offset=(0,0)):
    # offset is location of top left corner of canvas
    real_inner_radius = self.inner_radius * self._scale
    real_outer_radius = self.outer_radius * self._scale
    center = (offset[0] + real_outer_radius, offset[1] + real_outer_radius)
    pygame.draw.polygon(canvas, self.color, self._get_points(center, real_inner_radius, real_outer_radius), 0 if self._fill else self.line_width)

  def _get_points(self, offset, inner_radius, outer_radius):
    # offset is location of center of star
    # returns list of points in clockwise order
    points = []
    for i in range(10):
      radius = inner_radius if i % 2 == 0 else outer_radius
      angle = (i * PI/5 + PI/2 + self.rotation) % (2 * PI)
      points.append((offset[0] + radius * cos(angle), offset[1] + radius * sin(angle)))
    return points

  def __repr__(self):
    return f"{self.__class__.__name__}(color={self.color}, inner_radius={self.inner_radius}, outer_radius={self.outer_radius}, rotation={self.rotation}, scale={self._scale}, alpha={self.alpha}, fill={self._fill}, line_width={self.line_width})"

class Triangle(Shape):
  def __init__(self, color: ColorRGB, points: tuple, rotation=0, scale=1.0, alpha=1.0, fill=True, line_width=1):
    super().__init__(color, rotation, scale, alpha, fill, line_width)
    self.points = points

  def draw(self, canvas: pygame.Surface, offset=(0,0)):
    # offset is location of top left corner of canvas
    real_points = [(offset[0] + p[0] * self._scale, offset[1] + p[1] * self._scale) for p in self.points]
    pygame.draw.polygon(canvas, self.color, real_points, 0 if self._fill else self.line_width)

  def __repr__(self):
    return f"{self.__class__.__name__}(color={self.color}, points={self.points}, rotation={self.rotation}, scale={self._scale}, alpha={self.alpha}, fill={self._fill}, line_width={self.line_width})"

