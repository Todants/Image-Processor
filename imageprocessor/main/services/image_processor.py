import random
import time
from django.core.files.storage import default_storage
from ..models import ProcessedImage


class ImageProcessor:
    @staticmethod
    def process_image(file):
        """Основная логика обработки изображения"""
        filename = default_storage.save(file.name, file)

        time.sleep(20)

        result = random.randint(1, 1000)

        record = ProcessedImage.objects.create(
            filename=filename,
            result=result
        )

        return {
            'filename': filename,
            'result': result,
            'record': record
        }
