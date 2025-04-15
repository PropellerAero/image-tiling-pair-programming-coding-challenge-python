import unittest
from ..produce_tiles import get_number_of_levels_for_image

class TestGetNumberOfLevelsForImage(unittest.TestCase):
    def test_square_cases(self):
        square_cases = [
            ((1, 1), 1),
            ((2, 2), 2),
            ((3, 3), 3),
            ((4, 4), 3),
            ((8, 8), 4),
        ]
        for (width, height), expected in square_cases:
            with self.subTest(f"Square image dimensions: {width}x{height}"):
                self.assertEqual(get_number_of_levels_for_image(width, height), expected)

    def test_rectangle_cases(self):
        rectangle_cases = [
            ((1, 2), 2),
            ((2, 3), 3),
            ((16, 8), 5),
        ]
        for (width, height), expected in rectangle_cases:
            with self.subTest(f"Rectangle image dimensions: {width}x{height}"):
                self.assertEqual(get_number_of_levels_for_image(width, height), expected)
