import math
import os
from .image import Image
from .utilities import get_image_name, prepare_level_directory

def get_number_of_levels_for_image(width: int, height: int) -> int:
    max_dimension = max(width, height)
    return math.ceil(1 + math.log10(max_dimension))

def produce_tiles(
        image: Image,
        output_path: str,
        max_tile_dimension: int,
):
    width = image.width
    height = image.height
    max_dimension = max(width, height)
    number_of_levels = get_number_of_levels_for_image(width, height)

    print(f"Number of levels expected: {number_of_levels}")

    for tile_level in range(number_of_levels):
        # because tileLevels start at 0 and not 1 we need to subtract 1 in order to have 1*1 pixel at the lowest level
        # and the levelMaxDimension at the highest level equal to the full resolution of the image
        level_max_dimension = math.ceil(
            max_dimension / 2 ** (number_of_levels - 1 - tile_level)
        )
        tile_level_directory = prepare_level_directory(output_path, tile_level)

        # TODO: should handle rectangles to get ratio of sides
        level_width = level_max_dimension
        level_height = level_max_dimension

        resized = image.resize(level_width, level_height)

        # TODO: if the max dimension is greater than the maximum allowed tile size cut it up into tiles
        if level_max_dimension >= max_tile_dimension:
            extracted = resized.extract(
                0, 0, max_tile_dimension, max_tile_dimension
            )
            extracted.save(os.path.join(tile_level_directory, get_image_name(0, 0)))
        else:
            resized.save(os.path.join(tile_level_directory, get_image_name(0, 0)))
