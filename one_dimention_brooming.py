
class Line(object):
    def __init__(self, a,b):
        self.a=a
        self.b=b


class Point(object):

    def __init__(self, point, opening):
        self.point=point
        self.opening = opening
    def __repr__(self):
        return f"P<{self.point}>"

# list_of_lines = [(1, 2), (10, 11), (1, 3), (2, 3), (2, 5), (2, 7), (5, 6)]
line_objects = [Line(1, 2), Line(10, 11), Line(1, 3), Line(2, 3), Line(2, 5), Line(2, 7), Line(5, 6)]


#
# def count_layers(list_of_lines): # [(1, 2), (1, 3), (2, 5)...]
#     max_layer = 0
#     line_with_most_layers = list_of_lines[0]
#     opened_lines = []
#     for line in list_of_lines:
#         opened_lines.append(line)
#         for i in opened_lines:
#             if i[1] < line[0]:
#                 opened_lines.remove(i)
#         if len(opened_lines) > max_layer:
#             max_layer = len(opened_lines)
#             line_with_most_layers = line
#     return max_layer, line_with_most_layers



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
