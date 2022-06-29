import unittest
import random
import time
import ManyRectanglesBrooming
import TwoRectangles


def create_rectangles(amount):
    list_of_rectangles = []
    for i in range(0, amount):
        max_x = random.randint(1, 1000)
        min_x = random.randint(1, 1000)
        max_y = random.randint(1, 1000)
        min_y = random.randint(1, 1000)
        list_of_rectangles.append([(min_x, min_y), (max_x, min_y), (min_x, max_y), (max_x, max_y)])
    return list_of_rectangles


class ManyRectanglesBroomingTestCases(unittest.TestCase):

    def test_not_overlapping(self):
        self.assertEqual(ManyRectanglesBrooming.brooming([[(0, 0), (3, 0), (0, 2), (3, 2)]]), 1)
        self.assertEqual(ManyRectanglesBrooming.brooming([[(0, 0), (3, 0), (0, 2), (3, 2)],
                                                                         [(10, 10), (15, 10), (10, 15), (15, 15)]]), 1)


    def test_single_overlapping(self):
        self.assertEqual(ManyRectanglesBrooming.brooming([[(0, 0), (3, 0), (0, 2), (3, 2)],
                                                                         [(1, 1), (10, 1), (1, 4), (10, 4)]]), 2)

    def test_rectangle_inside(self):
        self.assertEqual(ManyRectanglesBrooming.brooming([[(0, 0), (10, 0), (0, 10), (10, 10)],
                                                                         [(1, 1), (5, 1), (1, 5), (5, 5)]]), 2)

    def test_rectangle_cascade_overlapping(self):
        self.assertEqual(ManyRectanglesBrooming.brooming([[(0, 0), (3, 0), (0, 2), (3, 2)],
                                                                         [(5, -2), (9, -2), (5, -1), (9, -1)],
                                                                         [(8, -1), (11, -1), (8, 1), (11, 1)],
                                                                         [(4, -3), (7, -3), (4, -2), (7, -2)],
                                                                         [(2, -1), (6, -1), (2, 1), (6, 1)]]), 2)

    def test_many_rectangles_overlapping(self):
        self.assertEqual(ManyRectanglesBrooming.brooming([[(0, 0), (3, 0), (0, 3), (3, 3)],
                                                                         [(1, -1), (4, -1), (1, 1), (4, 1)],
                                                                         [(2, 0), (5, 0), (2, 2), (5, 2)]]), 3)

    def test_rectangles_sharing_edge(self):
        self.assertEqual(ManyRectanglesBrooming.brooming([[(0, 0), (3, 0), (0, 2), (3, 2)],
                                                                         [(3, 0), (6, 0), (3, 2), (6, 2)]]), 2)

    def test_rectangles_sharing_point(self):
        self.assertEqual(ManyRectanglesBrooming.brooming([[(0, 0), (3, 0), (0, 2), (3, 2)],
                                                                         [(3, -2), (6, -2), (3, 0), (6, 0)]]), 2)

    def test_different_layer_depth_inside_rectangle(self):
        self.assertEqual(ManyRectanglesBrooming.brooming([[(0, 0), (7, 0), (0, 6), (7, 6)],
                                                                         [(1, 1), (2, 1), (1, 2), (2, 2)],
                                                                         [(3, 2), (6, 2), (3, 5), (6, 5)],
                                                                         [(4, 3), (5, 3), (4, 4), (5, 4)]]), 3)

    def test_different_layer_depth_inside_and_outside_of_rectangle(self):
        self.assertEqual(ManyRectanglesBrooming.brooming([[(0, 0), (17, 0), (0, 14), (17, 14)],
                                                                         [(1, 1), (2, 1), (1, 7), (2, 7)],
                                                                         [(1, 9), (2, 9), (1, 11), (2, 11)],
                                                                         [(3, 9), (5, 9), (3, 11), (5, 11)],
                                                                         [(4, 10), (8, 10), (4, 13), (8, 13)],
                                                                         [(6, 11), (7, 11), (6, 12), (7, 12)],
                                                                         [(9, 1), (16, 9), (9, 8), (16, 8)],
                                                                         [(10, 2), (15, 2), (10, 7), (15, 7)],
                                                                         [(11, 3), (14, 3), (11, 6), (14, 6)],
                                                                         [(12, 4), (13, 4), (12, 5), (13, 5)],
                                                                         [(16, 12), (19, 12), (16, 15), (19, 15)],
                                                                         [(18, 0), (21, 0), (18, 11), (21, 11)],
                                                                         [(20, 8), (22, 8), (20, 13), (22, 13)]]), 5)

    # def test_execution_time(self):
    #
    #     average_measurements = []
    #     for amount in (100, 200, 400):
    #         time_measurements = []
    #
    #         for i in range(4):
    #             start_time = time.time()
    #             ManyRectanglesBrooming.brooming(create_rectangles(amount))
    #             end_time = time.time()
    #             time_measurements.append(end_time - start_time)
    #
    #         average_measurements.append(sum(time_measurements)/4)
    #
    #     print(average_measurements)
    #     print(average_measurements[2]/average_measurements[1], average_measurements[1]/average_measurements[0])

    def test_random_rectangle_input_time(self):
        amount = 1000
        start_time = time.time()
        ManyRectanglesBrooming.brooming(create_rectangles(amount))
        end_time = time.time()
        print(f'Execution time for {amount} rectangles input: {end_time - start_time}')



# class TwoRectanglesTestCases(unittest.TestCase):
#
#     def test_not_overlapping(self):
#         self.assertEqual(TwoRectangles.rectangles_comparison([[(0, 0), (5, 0), (0, 5), (5, 5)],
#                                                               [(6, 0), (12, 0), (6, 5), (12, 5)]]), 0)
#
#     def test_rectangles_overlapping(self):
#         self.assertEqual(TwoRectangles.rectangles_comparison([[(0, 0), (5, 0), (0, 5), (5, 5)],
#                                                               [(1, 2), (7, 2), (1, 8), (7, 8)]]), 1)
#
#     def test_rectangle_b_inside_rectangle_a(self):
#         self.assertEqual(TwoRectangles.rectangles_comparison([[(0, 0), (5, 0), (0, 5), (5, 5)],
#                                                               [(1, 1), (4, 1), (1, 4), (4, 4)]]), 2)
#
#     def test_rectangle_a_inside_rectangle_b(self):
#         self.assertEqual(TwoRectangles.rectangles_comparison([[(1, 1), (4, 1), (1, 4), (4, 4)],
#                                                               [(0, 0), (5, 0), (0, 5), (5, 5)]]), 3)
