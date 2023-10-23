from django.contrib.auth import get_user_model
from django.db import models

from cats.constans import AchievementLimit, CatLimit

User = get_user_model()


class Achievement(models.Model):
    name = models.CharField(
        max_length=AchievementLimit.MAX_LEN_NAME.value
    )

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(
        max_length=CatLimit.MAX_LEN_NAME.value
    )
    color = models.CharField(
        max_length=CatLimit.MAX_LEN_COLOR.value
    )
    birth_year = models.IntegerField()
    owner = models.ForeignKey(
        User,
        related_name='cats',
        on_delete=models.CASCADE
    )
    achievements = models.ManyToManyField(
        Achievement,
        through='AchievementCat'
    )
    image = models.ImageField(
        upload_to='cats/images/',
        null=True,
        default=None
    )

    def __str__(self):
        return self.name


class AchievementCat(models.Model):
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE
    )
    cat = models.ForeignKey(
        Cat,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.achievement} {self.cat}'
