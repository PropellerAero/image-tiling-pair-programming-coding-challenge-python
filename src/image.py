from PIL import Image as PILImage

class Image:
    def __init__(self, image: PILImage.Image):
        self.image = image
        self.width, self.height = image.size

    def resize(self, width: int, height: int) -> 'Image':
        """Resizes an image to be 'inside' the bounding box of width and height, preserving dimensions."""
        resized_image = self.image.copy()
        resized_image.thumbnail((width, height), PILImage.Resampling.LANCZOS)
        return Image(resized_image)

    def extract(self, left: int, top: int, width: int, height: int) -> 'Image':
        """Extracts a region from the image."""
        if left + width > self.width or top + height > self.height:
            raise ValueError("Invalid extract")

        cropped_image = self.image.crop((left, top, left + width, top + height))
        return Image(cropped_image)

    def save(self, path: str) -> None:
        """Saves the image to the specified path."""
        self.image.save(path)

    @classmethod
    def open(cls, path: str) -> 'Image':
        """Creates an ImageHandler instance from an image file."""
        image = PILImage.open(path)
        return cls(image)
