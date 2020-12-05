from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        'Name',
        max_length=30
    )
    description = models.TextField(
        'Description',
        blank=True
    )
    created = models.DateTimeField(
        'Created',
        auto_now_add=True
    )
    modified = models.DateTimeField(
        'Modified',
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Favourite(models.Model):
    title = models.CharField(
        'Title',
        max_length=20
    )
    description = models.TextField(
        'Description',
        blank=True
    )
    rank = models.SmallIntegerField(
        'Ranking',
    )
    meta = JSONField(
        'Metadata',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='categories'
    )
    created = models.DateTimeField(
        'Created Date',
        auto_now_add=True
    )
    modified = models.DateTimeField(
        'Modified Date',
        auto_now=True
    )
    audit = JSONField(
        'Audit Log',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title + '--' + str(self.rank)


def save_favorite(sender, instance, **kwargs):
    print('starting')
    fav = instance
    try:
        favs = Favourite.objects.filter(
            rank__gte=fav.rank, 
            category=fav.category
            ).update(rank=F('rank') + 1)
        print(favs)
        # pre_save.disconnect(save_favorite, sender=sender)
        for f in favs:
            rank = f.rank
            rank += 1
            Favourite.objects.filter(id=f.id).update(rank=rank)
            print(f.rank)
        # post_save.connect(save_favorite, sender=sender)
        print('ending')
    except Favourite.DoesNotExist:
        pass

pre_save.connect(save_favorite, sender=Favourite)