from django.db import models

# Create your models here.
class Details(models.Model):
    title_part = models.CharField('Название детали', max_length=50)
    description_part = models.CharField('Описание детали', max_length=250)
    cost_part = models.IntegerField('Цена')
    presence_part = models.BooleanField('Есть ли в наличии?')
    link_picture = models.TextField('Ссылка на картинку', default='')

    def __str__(self):
        return self.title_part

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'