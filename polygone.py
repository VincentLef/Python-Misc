
import math
from lib.turtle import *

class Polygon(object):

    def __init__(self, points):
        self.points = points

    def circumference(self):
        circumference = 0
        # Calculate circumference by adding the distance between each points 2 by 2
        for index in range(len(self.points)):
            current = self.points[index]
            next = self.points[(index + 1) % len(self.points)]
            circumference += math.sqrt(math.fabs(math.pow(next['x'] - current['x'], 2) + math.pow(next['y'] - current['y'], 2)))

        return circumference

    def area(self):
        area = 0
        # Calculate area by adding/subtracting the integrals between each points 2 by 2
        for index in range(len(self.points)):
            current = self.points[index]
            next = self.points[(index + 1) % len(self.points)]
            # Calculate integrals as trapezium
            area += 0.5 * (current['y'] + next['y']) * (next['x'] - current['x'])

        return area

def main():
    points = []
    points.append({'x': 0, 'y': 0})
    points.append({'x': 4, 'y': 6})
    points.append({'x': 12, 'y': 4})
    points.append({'x': 8, 'y': 2})
    # points.append({'x': 0, 'y': 0})
    # points.append({'x': 0, 'y': 2})
    # points.append({'x': 2, 'y': 2})
    # points.append({'x': 2, 'y': 0})

    polygon = Polygon(points)
    print(polygon.circumference())
    print(polygon.area())

    turtle = Turtle()

    # Set up turtle
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    turtle.goto(points[0]['x'], points[0]['y'])
    turtle.pendown()

    # Set window size
    xs = list(p['x'] for p in points)
    ys = list(p['y'] for p in points)
    turtle.screen.setworldcoordinates(min(xs) - 1, min(ys) - 1, max(xs) + 1, max(ys) + 1)

    # Draw Polygon
    for index in range(1, len(points)):
        turtle.goto(points[index]['x'], points[index]['y'])
    turtle.goto(points[0]['x'], points[0]['y'])

    # Clean up turtle
    turtle.end_fill()
    turtle.hideturtle()

    input("Press Enter to continue...")

if __name__ == '__main__':
    main()
