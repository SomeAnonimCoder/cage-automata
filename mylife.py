import random
from copy import deepcopy

from PIL import Image, ImageDraw
import numpy as np

BAC = 1
PHAG = 2
GRASS = 0


class Map:
    arr = np.zeros([10, 10])
    n = 10
    m = 10

    def create(self, m, n):
        self.n = n
        self.m = m
        self.arr = np.zeros([m, n])
        for i in range(0, m - 1):
            for j in range(0, n - 1):
                tmp = random.randint(0, 100)
                if (tmp < 10): self.arr[i, j] = BAC
                if (tmp < 30 and tmp > 10): self.arr[i, j] = PHAG

    def next_stage(self):
        result = deepcopy(self.arr)
        left = self.arr[:, :-1]
        right = self.arr[:, 1:]
        top = self.arr[1:, :]
        bottom = self.arr[:-1, :]
        condition = np.logical_and(left == BAC, right == PHAG)
        result[:, :-1] = np.where(condition, PHAG, result[:, :-1])

        condition = np.logical_and(right == BAC, left == PHAG)
        result[:, 1:] = np.where(condition, PHAG, result[:, 1:])

        condition = np.logical_and(top == BAC, bottom == PHAG)
        result[:-1, :] = np.where(condition, PHAG, result[:-1, :])

        condition = np.logical_and(bottom == BAC, top == PHAG)
        result[1:, :] = np.where(condition, PHAG, result[1:, :])

        print(result)
        self.arr = result
        return

        for i in range(0, self.m - 1):
            for j in range(0, self.n - 1):
                if self.arr[i, j] == GRASS:
                    if (random.randint(0, 10) < 0): result[i, j] = BAC

                if self.arr[i, j] == BAC:
                    fed = 0

                    if (self.arr[i - 1, j - 1] == GRASS):
                        result[i - 1, j - 1] = BAC
                        fed = 1

                    if (self.arr[i - 1, j] == GRASS):
                        result[i - 1, j] = BAC
                        fed = 1

                    if (self.arr[i - 1, j + 1] == GRASS):
                        result[i - 1, j + 1] = BAC
                        fed = 1
                    if (self.arr[i, j - 1] == GRASS):
                        result[i, j - 1] = BAC
                        fed = 1

                    if (self.arr[i, j + 1] == GRASS):
                        result[i, j + 1] = BAC
                        fed = 1

                    if (self.arr[i + 1, j - 1] == GRASS):
                        result[i + 1, j - 1] = BAC
                        fed = 1

                    if (self.arr[i + 1, j] == GRASS):
                        result[i + 1, j] = BAC
                        fed = 1

                    if (self.arr[i + 1, j + 1] == GRASS):
                        result[i + 1, j + 1] = BAC
                        fed = 1

                if self.arr[i, j] == PHAG:
                    fed = 0
                    if (self.arr[i - 1, j - 1] == BAC):
                        result[i - 1, j - 1] = PHAG
                        fed = 1
                    if (self.arr[i - 1, j] == BAC):
                        result[i - 1, j] = PHAG
                        fed = 1
                    if (self.arr[i - 1, j + 1] == BAC):
                        result[i - 1, j + 1] = PHAG
                        fed = 1
                    if (self.arr[i, j - 1] == BAC):
                        result[i, j - 1] = PHAG
                        fed = 1
                    if (self.arr[i, j + 1] == BAC):
                        result[i, j + 1] = PHAG
                        fed = 1
                    if (self.arr[i + 1, j - 1] == BAC):
                        result[i + 1, j - 1] = PHAG
                        fed = 1
                    if (self.arr[i + 1, j] == BAC):
                        result[i + 1, j] = PHAG
                        fed = 1
                    if (self.arr[i + 1, j + 1] == BAC):
                        result[i + 1, j + 1] = PHAG
                        fed = 1
                    if not fed: result[i, j] = GRASS
        self.arr = result

    def to_image(self, name):
        img = Image.new("RGB", [50 * (self.m - 1), 50 * (self.n - 1)])

        for i in range(0, self.m - 1):
            for j in range(0, self.n - 1):
                color = (0, 0, 0)

                if self.arr[i, j] == BAC:
                    color = (255, 255, 0)
                if self.arr[i, j] == PHAG:
                    color = (255, 0, 0)
                if (self.arr[i, j] == GRASS):
                    color = (0, 255, 0)
                draw = ImageDraw.Draw(img)
                draw.rectangle((i * 50, j * 50, (i + 1) * 50, (j + 1) * 50), color)
        img.save(name)


map = Map()
map.create(10, 10)
map.to_image("mylife/0.jpg")
for i in range(1, 10):
    map.next_stage()
    map.to_image("mylife/" + str(i) + ".jpg")
