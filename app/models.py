from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


# Size validator
def validate_file_size(file):
    """Validator to limit video size"""
    max_size_mb = 49 * 10214
    if file.size > max_size_mb:
        raise ValidationError(f"The maximum file size that can be uploaded is 50MB")


# Create your models here.
class Category(models.Model):
    """This model is for the video category"""
    name = models.CharField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Video(models.Model):
    """This model is for video"""
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 help_text="What category does this video belong to?")
    title = models.CharField(max_length=150, help_text="This video is a short title!", unique=True)
    description = models.TextField(blank=True, help_text="Description for the video!")
    video_content = models.FileField(upload_to="videos/",
                                     validators=[
                                         FileExtensionValidator(
                                             allowed_extensions=['mp4', 'mov', 'avi', 'mkv', 'flv', 'wmv', 'webm'],
                                             message="File format is wrong!"
                                         ),
                                         validate_file_size
                                     ],
                                     help_text="Please upload *.mp4, *.mov, *.avi, *.mkv, *.flv, *.wmv "
                                               "and *.webm format files."
                                     )

    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
