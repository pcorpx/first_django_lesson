from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['image_preview', ]
    fields = ['image', 'image_preview', 'position']
    extra = 0

    def image_preview(self, obj):
        html = format_html('<img src="{url}" height=200px />',
                           url=obj.image.url)
        return html


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
