def find_max_min_coordinates(rectangle_coordinates):  # single rectangle shape: [(),()...]
    max_x = max([i[0] for i in rectangle_coordinates])
    max_y = max([i[1] for i in rectangle_coordinates])
    min_x = min([i[0] for i in rectangle_coordinates])
    min_y = min([i[1] for i in rectangle_coordinates])

    return max_x, max_y, min_x, min_y


def is_point_inside_rectangle(point, max_min_coordinates):
    max_x, max_y, min_x, min_y = max_min_coordinates
    point_x, point_y = point

    if (min_x <= point_x <= max_x) and (min_y <= point_y <= max_y):
        return True
    else:
        return False


def rectangles_comparison(list_of_rectangles):  # list of rectangles shape: [[(x,y),(x,y)...],[(x,y),(x,y)...]]
    """Returns 0 if compared rectangles have no common space, 1 if rectangles overlap,
     2 if second_rectangle is nested within first_rectangle, and 3 vice versa."""

    first_rectangle = list_of_rectangles[0]
    second_rectangle = list_of_rectangles[1]

    if not any([is_point_inside_rectangle(point, find_max_min_coordinates(first_rectangle)) for point in second_rectangle])\
       and not any([is_point_inside_rectangle(point, find_max_min_coordinates(second_rectangle)) for point in first_rectangle]):
        return 0
    elif all([is_point_inside_rectangle(point, find_max_min_coordinates(first_rectangle)) for point in second_rectangle]):
        return 2
    elif all([is_point_inside_rectangle(point, find_max_min_coordinates(second_rectangle)) for point in first_rectangle]):
        return 3
    elif any([is_point_inside_rectangle(point, find_max_min_coordinates(first_rectangle)) for point in second_rectangle]):
        return 1
    else:
        return None



