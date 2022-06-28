class Rectangle(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


class Point(object):
    def __init__(self, x, y, opening, owner):
        self.x = x
        self.y = y
        self.opening = opening
        self.owner = owner

    def __repr__(self):
        return f"P<{self.x}, {self.y}>"


def sort_rectangle_points(rectangle):
    max_x = max([i[0] for i in rectangle])
    max_y = max([i[1] for i in rectangle])
    min_x = min([i[0] for i in rectangle])
    min_y = min([i[1] for i in rectangle])

    return (min_x, max_y), (max_x, max_y), (min_x, min_y), (max_x, min_y)


def sort_rectangles(rectangles_list):
    rectangles = []
    for rectangle in rectangles_list:
        a, b, c, d = sort_rectangle_points(rectangle)
        rectangles.append(Rectangle(a, b, c, d))

    return rectangles


def sort_points(rectangles_list):
    points = []
    for rectangle in rectangles_list:
        points.append(Point(rectangle.a[0], rectangle.a[1], (True, True), rectangle))
        points.append(Point(rectangle.b[0], rectangle.b[1], (False, True), rectangle))
        points.append(Point(rectangle.c[0], rectangle.c[1], (True, False), rectangle))
        points.append(Point(rectangle.d[0], rectangle.d[1], (False, False), rectangle))

    points_sorted = sorted(points, key=lambda p: (p.x, -p.y))
    return points_sorted


def count_layers(points):
    local_max = 0
    max_max = 0
    opened_rectangles = []
    for point in points:

        if all(point.opening):
            opened_rectangles.append(point.owner)

        elif not any(point.opening) and opened_rectangles:
            x_list = {p[0]
                      for rectangle in opened_rectangles
                      for p in rectangle.__dict__.values()}
            # you can save some computational power if you make register of already checked x's
            x_list = list(filter(lambda n: n <= point.x, x_list))

            x_scope = (min(x_list), max(x_list))
            point_list = [p for p in points if x_scope[0] <= p.x <= x_scope[1]]

            for x in x_list:
                y_values = [(p.y, p.opening[1]) for p in point_list if p.x <= x and
                            ((p.x, p.y) not in (p.owner.b, p.owner.d))]
                y_values_sorted = sorted(y_values, key=lambda val: (val[0], val[1]), reverse=True)

                for y in y_values_sorted:
                    local_max = local_max + 1 if y[1] else local_max - 1
                    max_max = local_max if max_max < local_max else max_max
            opened_rectangles.remove(point.owner)
        else:
            pass

    return max_max


list_of_rectangles = [[(0, 0), (17, 0), (0, 14), (17, 14)],
                      [(1, 1), (2, 1), (1, 7), (2, 7)],
                      [(1, 9), (2, 9), (1, 11), (2, 11)],
                      [(3, 9), (5, 9), (3, 11), (5, 11)],
                      [(4, 10), (8, 10), (4, 13), (8, 13)],
                      [(6, 11), (7, 11), (6, 12), (7, 12)],
                      [(9, 1), (16, 1), (9, 8), (16, 8)],
                      [(10, 2), (15, 2), (10, 7), (15, 7)],
                      [(11, 3), (14, 3), (11, 6), (14, 6)],
                      [(12, 4), (13, 4), (12, 5), (13, 5)],
                      [(16, 12), (19, 12), (16, 15), (19, 15)],
                      [(18, 0), (21, 0), (18, 11), (21, 11)],
                      [(20, 8), (22, 8), (20, 13), (22, 13)]]


def brooming(rectangles):

    sorted_list_of_rectangles = sort_rectangles(list_of_rectangles)

    sorted_points = sort_points(sorted_list_of_rectangles)

    return count_layers(sorted_points)


print(brooming(list_of_rectangles))



















