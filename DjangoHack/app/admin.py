from django.contrib import admin

# Register your models here.
from .models import review_source,review
admin.site.register(review_source)
admin.site.register(review)
