from django.db import models

# Create your models here.

class Food(models.Model):
    food_name = models.CharField('Название блюда', max_length=60)
    photo = models.FileField('Фото блюда', upload_to= 'media/')
    # ingredients = models.ForeignKey('Ingredients', on_delete=models.CASCADE,
    #                                 related_name='Состав блюда')
    description = models.CharField('Описание блюда', max_length=250)


class Comment(models.Model):
    author = models.ForeignKey('account.User',on_delete=models.CASCADE,
                               related_name= 'author_comment')
    food = models.ForeignKey(Food,on_delete=models.CASCADE,related_name='food_comment')
    text = models.CharField('Комментарий', max_length=500)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)




