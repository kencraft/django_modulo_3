from django.db import models

# NOTE: Para poder utilizar el modelo "user" que viene por defecto en Django,
# Debemos importarlo previamente:

from django.contrib.auth.models import User

# Create your models here.


class Comic(models.Model):
    '''
    Esta clase hereda de Django models.Model y crea una tabla llamada
    e_commerce_comic. Las columnas toman el nombre especificado de cada objeto.
    '''
    id = models.BigAutoField(db_column='ID', primary_key=True)
    marvel_id = models.PositiveIntegerField(
        verbose_name='marvel ids', default=1, unique=True)
    title = models.CharField(
        verbose_name='titles', max_length=120, default='')
    description = models.TextField(
        verbose_name='descriptions', default='')
    price = models.FloatField(
        verbose_name='prices', max_length=5, default=0.00)
    stock_qty = models.PositiveIntegerField(
        verbose_name='stock qty', default=0)
    picture = models.URLField(
        verbose_name='pictures', default='')

    class Meta:
        '''
        Con "class Meta" podemos definir atributos de nuestras entidades como el nombre de la tabla.
        '''
        db_table = 'e_commerce_comics'

    def __str__(self):
        '''
        La función __str__ cumple la misma función que __repr__ en SQL Alchemy, 
        es lo que retorna cuando llamamos al objeto.
        '''
        return f'{self.id}'

class Wish_list(models.Model):
    user_id = models.IntegerField(verbose_name='Usuario')
    comic_id= models.ForeignKey(Comic, 
                                 verbose_name='Comic',
                                 on_delete=models.DO_NOTHING,
                                 default=1, blank=True
                                 )
    favorite=models.BooleanField(default=False)
    cart=models.BooleanField(default=False)
    wished_qty=models.PositiveIntegerField(default=0)
    buied_qty=models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'e_commerce_wish_list'

    def __str__(self):
        return f'{self.user_id} - {self.comic_id.title}'