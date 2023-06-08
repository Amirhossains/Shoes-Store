from django.db import models
from django.utils.translation import gettext_lazy as _

class ShoesModel(models.Model):
    masculine = 1
    feminine = 2
    genderTuple = (
        (masculine, _('masculine')),
        (feminine, _('feminine'))
    )
    gender = models.IntegerField(verbose_name=_('gender'), choices=genderTuple, default=masculine)
    mark = models.CharField(verbose_name=_('shoes mark'), max_length=30)
    size = models.PositiveIntegerField(verbose_name=_('size'), default=35)
    color = models.CharField(verbose_name=_('color'), max_length=30)
    isAvailable = models.BooleanField(verbose_name=_('is available'), default=True)
    price = models.PositiveBigIntegerField(verbose_name=_('price'), default=100000)
    discount = models.CharField(verbose_name=_('discount'), max_length=10)
    count = models.PositiveIntegerField(verbose_name=_('count'), blank=True, null=True)
    discription = models.TextField(max_length=500, blank=True)
    categoryImage = models.ImageField(verbose_name=_('image'), upload_to='shoes/')
    createdTime = models.DateTimeField(verbose_name=_('created time'), auto_now=True)
    updatedTime = models.DateTimeField(verbose_name=_('updated time'), auto_now_add=True)

    class Meta:
        db_table = 'shoes'
        verbose_name = _('shoes')
        verbose_name_plural = _('shoes')

    def __str__(self):
        return self.mark

class CommentModel(models.Model):
    shoes = models.ForeignKey(to=ShoesModel, related_name='shoes', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name=_('title'), blank=True)
    text = models.TextField(max_length=700, verbose_name=_('text'))
    like = models.BooleanField(null=True, help_text=_('Yes means you liked the shoes and No means you did not lik the shoes.'))
    createdTime = models.DateTimeField(verbose_name=_('created time'), auto_now=True)
    updatedTime = models.DateTimeField(verbose_name=_('updated time'), auto_now_add=True)

    class Meta:
        db_table = 'comments'
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return self.text

