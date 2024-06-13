from django.contrib import admin
from .models import Category, Video
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """To display these categories in the admin panel"""
    list_display = ['pk', 'name', 'created', 'updated', 'published']
    list_display_links = ('pk', 'name')
    list_editable = ('published',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """This is to output the video model information in the admin panel"""
    list_display = ['pk', 'category', 'title', 'get_video', 'description', 'uploaded', 'updated', 'published']
    list_display_links = ('pk', 'title')
    list_editable = ('published',)

    def get_video(self, video):
        """This function is to show video in admin panel"""
        if video.video_content:
            return mark_safe(
                f'<video width="120" height="80" controls><source src="{video.video_content.url}" '
                f'type="video/mp4">'
                f'Your browser does not support the video tag.</video>')
        return "No video file"

    get_video.short_description = "Video"
