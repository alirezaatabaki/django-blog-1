from django.db import models
from django.utils import timezone

from extensions.utils import jalali_converter


class Article(models.Model):
    STATUS_CHOICES = [
        ('d', 'پیش‌نویس'),
        ('p', 'منتشر شده')
    ]
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ')
    description = models.TextField(verbose_name='متن مقاله')
    thumbnail = models.ImageField(upload_to='images', verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت ')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله‌ها'

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = 'تاریخ انتشار'
