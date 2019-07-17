import random
from copy import deepcopy

from PIL import Image, ImageDraw
import numpy as np

ALIVE=1
DEAD=0

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
                self.arr[i,j]=random.randint(0,1)

    def next_stage(self):
        arr=deepcopy(self.arr)
        for i in range(0, self.m - 1):
            for j in range(0, self.n - 1):
                sum = \
                    self.arr[i-1, j-1]+self.arr[i, j-1]+self.arr[i+1, j-1]+ \
                    self.arr[i - 1, j ] + self.arr[i, j ] + self.arr[i + 1, j ] + \
                    self.arr[i - 1, j + 1] + self.arr[i, j + 1] + self.arr[i + 1, j + 1]
                if self.arr[i,j]==DEAD:
                    if sum==3: arr[i,j]=ALIVE
                if self.arr[i,j]==ALIVE:
                    if sum >3:arr[i,j]=DEAD
                    if sum <2: arr[i,j]=DEAD

        self.arr=arr

    def to_image(self, name):
        img = Image.new("RGB", [50 * (self.m-1) , 50 * (self.n-1) ])

        for i in range(0, self.m - 1):
            for j in range(0, self.n - 1):
                color = (0, 0, 0)

                if self.arr[i, j] == DEAD:
                    color = (255, 0, 0)
                if (self.arr[i, j] == ALIVE):
                    color = (0, 255, 0)
                draw = ImageDraw.Draw(img)
                draw.rectangle((i*50,j*50,(i+1)*50,(j+1)*50), color)
        img.save(name)


map = Map()
map.create(100, 100)
map.to_image("life/0.jpg")
for i in range(1, 50):
    map.next_stage()
    map.to_image("life/"+str(i)+".jpg")