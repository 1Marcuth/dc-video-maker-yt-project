from PIL.Image import Image as ImageObject
from pydantic import validate_arguments

class ImageMaker:
    _bg: ImageObject

    @validate_arguments
    def save(self, file_path: str) -> None:
        (self._bg
            .convert("RGB")
            .save(file_path, quality=100))

    def get(self) -> ImageObject:
        return self._bg