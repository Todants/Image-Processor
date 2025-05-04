from django.db import models


class ProcessedImage(models.Model):
    filename = models.CharField(max_length=255)
    result = models.IntegerField()
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.filename} - {self.result} - {self.upload_time}"
