from django.contrib import admin

# Register your models here.
from models import ObjectItem, Transport, Transform, Storage, ProductChain, Extracts

admin.site.register(ObjectItem)
admin.site.register(Extracts)
admin.site.register(Transport)
admin.site.register(Transform)
admin.site.register(Storage)
admin.site.register(ProductChain)
