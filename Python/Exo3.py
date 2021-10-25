import math

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x


    def getY(self):
        return self.y

    def distance(self, Point):
        point_x = Point.getX()
        point_y = Point.getY()

        distance = math.sqrt(pow((point_x - self.x), 2) + pow((point_y - self.y), 2))

        return round(distance, 3)


"""
=================
Mise en situation
=================
"""

A = Point(2, 3)
B = Point(4, 1)

print("Distance entre le point A et le point B : ", A.distance(B))