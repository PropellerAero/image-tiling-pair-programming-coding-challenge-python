import unittest
from unittest.mock import MagicMock, patch
from src.produce_tiles import produce_tiles

class FakeImage:
    def __init__(self, width, height, mock_save):
        self.width = width
        self.height = height
        self._mock_save = mock_save

    def resize(self, new_width, new_height):
        # Return a new fake image with the new dimensions.
        return create_image_mock(new_width, new_height, self._mock_save)

    def extract(self, left, top, w, h):
        # Mimic invalid extraction if the requested region exceeds dimensions.
        if left + w > self.width or top + h > self.height:
            raise ValueError("Invalid extract")
        return create_image_mock(w, h, self._mock_save)

    def save(self, path):
        self._mock_save(path)

def create_image_mock(width, height, mock_save):
    return FakeImage(width, height, mock_save)

class TestProduceTiles(unittest.TestCase):
    def setUp(self):
        # Create a MagicMock to track calls to "save"
        self.mock_save = MagicMock()

    # We patch get_number_of_levels_for_image to force 3 levels for a 4x4 image,
    # matching the expected TS behavior. In TS:
    #   [[4, 4], 3]
    @patch("src.produce_tiles.get_number_of_levels_for_image", return_value=3)
    @patch("src.produce_tiles.prepare_level_directory", new=lambda path, level: f"{path}/{level}")
    @patch("src.produce_tiles.get_image_name", new=lambda x, y: f"{x}_{y}.png")
    def test_square_equal_max_tile_dimension(self, mock_get_levels):
        # For a 4x4 image and max_tile_dimension = 4 we expect three saved tiles.
        image = create_image_mock(4, 4, self.mock_save)
        produce_tiles(image, "path", 4)

        # Verify that .save was called 3 times.
        self.assertEqual(self.mock_save.call_count, 3)
        # Expected calls: one per level, with file paths "path/0/0_0.png", "path/1/0_0.png", "path/2/0_0.png"
        expected_calls = ["path/0/0_0.png", "path/1/0_0.png", "path/2/0_0.png"]
        actual_calls = [args[0] for args, kwargs in self.mock_save.call_args_list]
        self.assertEqual(actual_calls, expected_calls)

    @patch("src.produce_tiles.get_number_of_levels_for_image", return_value=3)
    @patch("src.produce_tiles.prepare_level_directory", new=lambda path, level: f"{path}/{level}")
    @patch("src.produce_tiles.get_image_name", new=lambda x, y: f"{x}_{y}.png")
    def test_square_double_max_tile_dimension(self, mock_get_levels):
        # TODO: Write this test
        self.fail("TODO: Write this test")

if __name__ == "__main__":
    unittest.main()
