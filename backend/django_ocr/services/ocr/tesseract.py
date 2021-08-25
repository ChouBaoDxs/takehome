import typing

import pytesseract
from PIL import ImageFile

from .base import BaseOcrService


class TesseractOcrService(BaseOcrService):
    @classmethod
    def parse_letter(cls, image: ImageFile) -> (typing.List[str], typing.Optional[Exception]):
        try:
            result_str = pytesseract.image_to_string(image)
            letter_list = []
            for character in result_str:
                if character.isalpha():
                    letter_list.append(character)
            return letter_list, None
        except Exception as e:
            return [], e
