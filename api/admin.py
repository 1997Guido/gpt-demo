from django.contrib import admin

# Register your models here.


from .models import QueryCategory, DatabaseExplanation

admin.site.register(QueryCategory)
admin.site.register(DatabaseExplanation)