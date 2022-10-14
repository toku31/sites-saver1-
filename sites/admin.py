from django.contrib import admin

from sites.models import Site, Review, Tag, Category

admin.site.register(Site)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Category)