import TwoRectangles


def find_adherent_rectangles(base_rectangle, list_of_rectangles):
    """Filtering function which returns list of overlapping or nested rectangles in relation to base_rectangle
     (except for base_rectangle itself)."""

    base_rectangle_index = list_of_rectangles.index(base_rectangle)
    adherent_rectangles = []

    for rectangle in list_of_rectangles:
        if list_of_rectangles.index(rectangle) != base_rectangle_index\
           and TwoRectangles.rectangles_comparison([base_rectangle, rectangle]) in (1, 2):
            adherent_rectangles.append(rectangle)
    return adherent_rectangles


def count_layers(adherent_rectangles, layer_counter=0):
    """Recursively counts layer depth of each rectangle within scope of adherent_rectangles and returns maximum depth
    level occurrence."""

    if not adherent_rectangles:
        return layer_counter
    else:
        layer_counter += 1
        max_layers = 0

        for rectangle in adherent_rectangles:
            nested_adherent_rectangles = find_adherent_rectangles(rectangle, adherent_rectangles)
            layers = count_layers(nested_adherent_rectangles, layer_counter)
            if max_layers < layers:
                max_layers = layers

        return max_layers


def find_rectangle_with_most_layers(list_of_rectangles):
    """Finds maximum layer depth level for each rectangle in list_of_rectangles and returns rectangle with the
    biggest layer depth level."""

    rectangle_with_most_layers = list_of_rectangles[0]
    max_layers = 0

    for base_rectangle in list_of_rectangles:
        adherent_rectangles = find_adherent_rectangles(base_rectangle, list_of_rectangles)
        layers = count_layers(adherent_rectangles)
        if layers > max_layers:
            rectangle_with_most_layers = base_rectangle
            max_layers = layers

    return rectangle_with_most_layers, max_layers







