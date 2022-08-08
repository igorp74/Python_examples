class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return (abs(self.__x - x)**2 + abs(self.__y - y)**2)**0.5

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:
    def __init__(self, v1, v2, v3):
        self.__vs = [v1, v2, v3]

    def perimeter(self):
        p = 0
        for i in range(3):
            p += self.__vs[i].distance_from_point(self.__vs[(i+1) % 3])
        return p

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())


