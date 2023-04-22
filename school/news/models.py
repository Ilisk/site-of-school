from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):

    Th = 'Techonology'
    Cb = 'Celebrity'
    CHOICES = [
        (Th, "Techonology"),
        (Cb, "Celebrity"),

    ]
    name = models.CharField(max_length=200, verbose_name='Название', null='')
    datetime = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
    categories = models.CharField(max_length=20, choices=CHOICES, verbose_name='Категория', null='')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(verbose_name='Изображение', upload_to="media", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'