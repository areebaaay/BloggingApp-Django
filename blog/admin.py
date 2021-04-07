from django.contrib import admin
from .models import Post, Contact
# Register your models here.

#registering our model with the admin site
admin.site.register(Post)

admin.site.register(Contact)
