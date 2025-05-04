import random
import time
from django.core.files.storage import default_storage
from ..models import ProcessedImage


class ImageProcessor:
    @staticmethod
    def process_image(file):
        """Основная логика обработки изображения"""
        # Сохраняем файл
        filename = default_storage.save(file.name, file)

        # Имитируем обработку (20 секунд)
        time.sleep(1)

        # Генерируем случайный результат
        result = random.randint(1, 1000)

        # Сохраняем в БД
        record = ProcessedImage.objects.create(
            filename=filename,
            result=result
        )

        return {
            'filename': filename,
            'result': result,
            'record': record
        }
