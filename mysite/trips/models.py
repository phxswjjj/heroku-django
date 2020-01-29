from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.


class PostTime(models.Model):
    time_start = models.TimeField()
    time_keep_hour = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return '{} + {}H'.format(self.time_start.strftime('%H:%M'), self.time_keep_hour)


class PostLocation(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location


class PostLocationTimeShip(models.Model):
    location = models.ForeignKey(PostLocation, on_delete=models.CASCADE)
    time = models.ForeignKey(PostTime, on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.location, self.time)


class User(models.Model):
    USER_TYPE_CHOICE = (
        ('CB', '社團'),
        ('GUEST', '球友')
    )

    name = models.CharField(max_length=3)
    user_type = models.CharField(
        max_length=5, choices=USER_TYPE_CHOICE, default=USER_TYPE_CHOICE[0][0], verbose_name='身份')
    login_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='profile', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{}-{}'.format(self.user_type, self.name)


class Post(models.Model):
    schedule_at = models.DateField(verbose_name='活動日期')
    location_time = models.ForeignKey(
        PostLocationTimeShip, related_name='posts', on_delete=models.CASCADE, verbose_name='活動時間')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='created_posts', on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        User, related_name='modified_posts', on_delete=models.CASCADE)
