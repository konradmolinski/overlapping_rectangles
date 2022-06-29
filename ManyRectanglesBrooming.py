class Rectangle(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


class Point(object):
    def __init__(self, x, y, opening, owner=None):
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
        rectangles.append([a, b, c, d])

    return rectangles


def sort_points_and_create_rectangles(rectangles_list):
    points = []
    rectangles = []
    for count, rectangle in enumerate(rectangles_list):
        a = Point(rectangle[0][0], rectangle[0][1], (True, True))
        b = Point(rectangle[1][0], rectangle[1][1], (False, True))
        c = Point(rectangle[2][0], rectangle[2][1], (True, False))
        d = Point(rectangle[3][0], rectangle[3][1], (False, False))

        rectangles.append(Rectangle(a, b, c, d))

        a.owner = rectangles[count]
        b.owner = rectangles[count]
        c.owner = rectangles[count]
        d.owner = rectangles[count]

        points += a, b, c, d

    # points_sorted = sorted(points, key=lambda p: (p.x, -p.y, -p.opening))
    points_sorted = sorted(sorted(sorted(points, key=lambda p: p.opening, reverse=True),
                                  key=lambda p: p.y, reverse=True), key=lambda p: p.x)
    return points_sorted, rectangles


def count_layers(points):
    local_max = 0
    max_max = 0
    opened_rectangles = []
    already_checked_xs = []
    for point in points:

        if all(point.opening):
            opened_rectangles.append(point.owner)

        elif not any(point.opening) and opened_rectangles:
            x_list = []
            for rectangle in opened_rectangles:
                x_list += rectangle.a.x, rectangle.b.x

            x_set = set(list(filter(lambda n: n <= point.x, filter(lambda n: n not in already_checked_xs, x_list))))

            for x in x_set:
                y_list = []
                for rectangle in opened_rectangles:
                    if rectangle.a.x <= x:
                        y_list += (rectangle.a.y, True), (rectangle.c.y, False)

                y_list_sorted = sorted(y_list, key=lambda val: (val[0], val[1]), reverse=True)

                for y in y_list_sorted:
                    local_max = local_max + 1 if y[1] else local_max - 1
                    max_max = local_max if max_max < local_max else max_max

            already_checked_xs += x_set
            opened_rectangles.remove(point.owner)
        else:
            pass

    return max_max


def brooming(rectangles):

    sorted_list_of_rectangles = sort_rectangles(rectangles)

    sorted_points, rectangle_objects = sort_points_and_create_rectangles(sorted_list_of_rectangles)

    return count_layers(sorted_points)


# list_of_rectangles = [[(0, 0), (3, 0), (0, 2), (3, 2)],
#                       [(3, -2), (6, -2), (3, 0), (6, 0)]]

# print(brooming(list_of_rectangles))



















