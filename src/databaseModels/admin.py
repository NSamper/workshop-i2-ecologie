from django.contrib import admin

# Register your models here.
from databaseModels.models import ObjectItem, Transport, Transform, Storage, ProductChain

admin.site.register(ObjectItem)
admin.site.register(Transport)
admin.site.register(Transform)
admin.site.register(Storage)
admin.site.register(ProductChain)
