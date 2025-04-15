import sys
import os
from .image import Image
from .utilities import setup_output_dir
from .produce_tiles import produce_tiles

OUTPUT_DIRECTORY = "./tiled-image"
MAX_TILE_DIMENSION_PIXELS = 256

def parse_args(args):
    """Parse and validate command line arguments."""
    if not args:
        raise ValueError("Must pass path to image as first argument to script.")
    
    image_path = args[0]
    if not os.path.exists(image_path):
        raise ValueError(f"Path {image_path} does not exist. Please check the path and try again.")
    
    return image_path

def main():
    """Main entry point for the image tiling script."""
    try:
        image_path = parse_args(sys.argv[1:])
        setup_output_dir(OUTPUT_DIRECTORY)
        image = Image.open(image_path)
        produce_tiles(image, OUTPUT_DIRECTORY, MAX_TILE_DIMENSION_PIXELS)
    except Exception as e:
        print(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main() 