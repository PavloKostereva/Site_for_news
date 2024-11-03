from django.db import models
#міграція- зв'язок між проектом і базою даних
# для роботи і створення таблиць в базі даних
class Article(models.Model):
    title = models.CharField('Назва', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=250, default='')
    full_text = models.TextField('Стаття')
    date= models.DateTimeField('Дата публікації')
    def __str__(self):
        #return f'Новина:{self.title}'
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'



    class Meta:
        verbose_name= 'Новина'
        verbose_name_plural= 'Новини'