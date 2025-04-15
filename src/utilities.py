import os
import shutil

def setup_output_dir(path: str) -> None:
    """Sets up the output directory, clearing it if it exists."""
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def prepare_level_directory(output_path: str, level: int) -> str:
    """Creates and returns the path for a specific tile level directory."""
    tile_level_directory = os.path.join(output_path, str(level))
    os.makedirs(tile_level_directory)
    return tile_level_directory

def get_image_name(x: int, y: int) -> str:
    """Returns the filename for a tile at coordinates (x, y)."""
    return f"{x}_{y}.png" 