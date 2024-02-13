from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(models.Model):
    username=models.CharField(
        verbose_name='юзернаме',
        unique=True,
        blank=True
    )
    phone_number=models.CharField(
        verbose_name='номер телефона',
        unique=True,
        max_length=20,
        null=False
    )
    first_name=models.CharField(
        verbose_name='имя',
        unique=False,
        max_length=120,
        null=False
    )

    class Meta:
        verbose_name='пользователь'
        verbose_name_plural='пользователи'

    def __str__(self) -> str:
        return f'{self.first_name} | {self.phone_number}'


class Material(models.Model):
    name=models.CharField(
        verbose_name='название',
        max_length=120        
    )

    class Meta:
        verbose_name='материал'
        verbose_name_plural='материалы'

    def __str__(self) -> str:
        return f'{self.name}'


class CityCountry(models.Model):
    city=models.CharField(
        verbose_name='город',
        max_length=120,
        Null=True
    )
    country=models.CharField(
        verbose_name='страна',
        max_length=120
    )

    class Meta:
        verbose_name='место производства'
        verbose_name_plural='места производства'

    def __str__(self) -> str:
        if len(self.city) >=1:
            return f'{self.country}, {self.city}'
        return f'{self.country}'
        


class Stul(models.Model):
    name=models.CharField(
        verbose_name='название',
        max_length=120
    )
    materials=models.ManyToManyField(
        to=Material,
        verbose_name='материалы',
    )
    made_in=models.ForeignKey(
        to=CityCountry,
        related_name='сделано в',
        verbose_name='место производства',
        on_delete=models.CASCADE,
    )
    height=models.DecimalField(
        verbose_name='высота',
        decimal_places=2,
        max_digits=10
    )
    width=models.DecimalField(
        verbose_name='ширина',
        decimal_places=2,
        max_digits=10
    )
    deep=models.DecimalField(
        verbose_name='глубина',
        decimal_places=2,
        max_digits=10
    )
    cost=models.DecimalField(
        verbose_name='цена',
        decimal_places=2,
        max_digits=12,
        null=False
    )

    class Meta:
        verbose_name='стул'
        verbose_name_plural='стулья'

    def __str__(self) -> str:
        return f'{self.name} | {self.cost}'
    


class Stol(models.Model):
    name=models.CharField(
        verbose_name='название',
        max_length=120
    )
    materials=models.ManyToManyField(
        to=Material,
        verbose_name='материалы',
    )
    made_in=models.ForeignKey(
        to=CityCountry,
        related_name='сделано в',
        verbose_name='место производства',
        on_delete=models.CASCADE,
    )
    height=models.DecimalField(
        verbose_name='высота',
        decimal_places=2,
        max_digits=10
    )
    width=models.DecimalField(
        verbose_name='ширина',
        decimal_places=2,
        max_digits=10
    )
    deep=models.DecimalField(
        verbose_name='глубина',
        decimal_places=2,
        max_digits=10
    )
    cost=models.DecimalField(
        verbose_name='цена',
        decimal_places=2,
        max_digits=12,
        null=False
    )
    is_transformer= models.BooleanField(
        verbose_name='раздвижной или нет',
        default=False
    )

    class Meta:
        verbose_name='стул'
        verbose_name_plural='стулья'

    def __str__(self) -> str:
        return f'{self.name} | {self.cost}'
    


