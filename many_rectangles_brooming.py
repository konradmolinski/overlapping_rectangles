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


def sort_rectangles_and_points(rectangles_list):
    """Find mix and max x and y for each rectangle in a list and compose new list of rectangle objects based on created
    point objects. Return both rectangles and points sorted by x's and y's with points sorted additionally by boolean
    values standing for opening and closing status of each point's x and y."""
    rectangles = []
    points = []
    for count, rectangle in enumerate(rectangles_list):

        max_x = max([i[0] for i in rectangle])
        max_y = max([i[1] for i in rectangle])
        min_x = min([i[0] for i in rectangle])
        min_y = min([i[1] for i in rectangle])

        a = Point(min_x, max_y, (True, True))
        b = Point(max_x, max_y, (False, True))
        c = Point(min_x, min_y, (True, False))
        d = Point(max_x, min_y, (False, False))
        rectangles.append(Rectangle(a, b, c, d))

        a.owner = rectangles[count]
        b.owner = rectangles[count]
        c.owner = rectangles[count]
        d.owner = rectangles[count]
        points += a, b, c, d

    rectangles.sort(key=lambda rect: (rect.a.x, -rect.a.y))

    points_sorted = sorted(sorted(sorted(points, key=lambda p: p.opening, reverse=True),
                                  key=lambda p: p.y, reverse=True), key=lambda p: p.x)

    return rectangles, points_sorted


def count_layers(points):
    """For each point, check if its opening or closing one. If its opening point ("a" point of rectangle object)
    then add its owner to the opened rectangles list. If it's a closing point ("d" of rectangle object) then list
    openings and closings of y's for each x in the scope of opened rectangles. Then count layers based on y's openings
    and finally remove rectangle-owner from the opened rectangles list."""
    local_max = 0
    max_max = 0
    opened_rectangles = []
    already_checked_x_list = []
    for point in points:
        if all(point.opening):
            opened_rectangles.append(point.owner)

        elif not any(point.opening) and opened_rectangles:
            x_list = []
            for rectangle in opened_rectangles:
                x_list += rectangle.a.x, rectangle.b.x

            # Limiting x_set to x's smaller than currently evaluated point so no "future" x's are considered.
            # Filtering x_set from already checked x's list.
            x_set = set(list(filter(lambda n: n <= point.x, filter(lambda n: n not in already_checked_x_list, x_list))))

            # Composing list of y's for each x of x_set.
            for x in x_set:
                y_list = []
                for rectangle in opened_rectangles:
                    if rectangle.a.x <= x:
                        y_list += (rectangle.a.y, True), (rectangle.c.y, False)

                # Sorting y's by value (descending) and by opening/closing status.
                y_list_sorted = sorted(y_list, key=lambda val: (val[0], val[1]), reverse=True)

                # Checking for local and global max layers based on openings/closings of y's list
                for y in y_list_sorted:
                    local_max = local_max + 1 if y[1] else local_max - 1
                    max_max = local_max if max_max < local_max else max_max

            already_checked_x_list += x_set
            opened_rectangles.remove(point.owner)
        else:
            pass

    return max_max


def brooming(rectangles):

    rectangle_objects, sorted_points = sort_rectangles_and_points(rectangles)
    return count_layers(sorted_points)



















