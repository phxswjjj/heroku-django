from django.contrib import admin

from .models import Post, User, PostTime, PostLocation, PostLocationTimeShip

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('schedule_at', 'location_time',
                    'created_at', 'modified_at')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_type')


@admin.register(PostTime)
class PostTimeAdmin(admin.ModelAdmin):
    list_display = ('time_start', 'time_keep_hour')


@admin.register(PostLocation)
class PostLocationAdmin(admin.ModelAdmin):
    list_display = ('location',)


@admin.register(PostLocationTimeShip)
class PostLocationTimeShipAdmin(admin.ModelAdmin):
    list_display = ('location', 'time')
