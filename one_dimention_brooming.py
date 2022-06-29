
class Line(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Point(object):

    def __init__(self, point, opening):
        self.point=point
        self.opening = opening

    def __repr__(self):
        return f"P<{self.point}>"


line_objects = [Line(1, 2), Line(10, 11), Line(1, 3), Line(2, 3), Line(2, 5), Line(2, 7), Line(5, 6)]


def sort_lines(lines):
    points = []
    for line in lines:
        points.append(Point(line.a, True))
        points.append(Point(line.b, False))
    points_sorted = sorted(points, key=lambda x: x.point)
    return points_sorted


def brooming(points):
    local_max = 0
    max_max = 0
    for point in points:
        local_max = local_max + 1 if point.opening else local_max - 1
        max_max = local_max if max_max < local_max else max_max
    print(max_max)


if __name__ == "__main__":
    points = sort_lines(line_objects)
    brooming(points)






#
# list_of_lines.sort(key=lambda x: x[0])
# print(list_of_lines)
# print(count_layers(list_of_lines))
