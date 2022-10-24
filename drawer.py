import numpy
from PIL import Image, ImageDraw


class Matrix:
    def __init__(self, width: int, height: int, cell_size: int):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.matrix = numpy.full((width, height), False)
        self.img = Image.new('RGB', (width * cell_size, height * cell_size))
        self.img_d = ImageDraw.Draw(self.img)

    def set(self, x: int, y: int):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.matrix[x][y] = True

    def clr(self, x: int, y: int):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.matrix[x][y] = False

    def clear_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i, j] = False

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.matrix[i][j]:
                    self.img_d.rectangle((self.cell_size * i, self.cell_size * j, self.cell_size * (i + 1), self.cell_size * (j + 1)), fill='#ffffff')
        return self.img
