import typing

from PIL import ImageFile


class BaseOcrService:
    @classmethod
    def parse_letter(cls, image: ImageFile) -> (typing.List[str], typing.Optional[Exception]):
        raise NotImplementedError('`parse_letter()` must be implemented.')
