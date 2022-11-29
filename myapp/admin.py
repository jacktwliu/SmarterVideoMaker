from django.contrib import admin
from myapp import models
# Register your models here.
admin.site.register(models.Document)
admin.site.register(models.News)
admin.site.register(models.SendFeedback)
admin.site.register(models.Messageboard)